import asyncio
import typing

from http import HTTPStatus
from http.client import HTTPException

import aiohttp
import aiohttp.web

from capmonstercloudclient.captcha_result import CaptchaResult
from capmonstercloudclient.client_options import ClientOptions
from capmonstercloudclient.exceptions import (
    GetBalanceError,
    GetResultError,
    GetTaskError,
    UnknownRequestInstanceError,
)
from capmonstercloudclient.get_result_timeouts import (
    GetResultTimeouts,
    get_amazon_waf_timeouts,
    get_basilisk_timeouts,
    get_datadome_timeouts,
    get_funcaptcha_timeouts,
    get_geetest_timeouts,
    get_hcaptcha_timeouts,
    get_image2_text_timeouts,
    get_recaptcha_v2_enterprise_timeouts,
    get_recaptcha_v2_timeouts,
    get_recaptcha_v3_timeouts,
    get_ten_di_timeouts,
    get_turnstile_timeouts,
)
from capmonstercloudclient.request_controller import RequestController
from capmonstercloudclient.requests import (
    REQUESTS,
    AmazonWafProxylessRequest,
    AmazonWafRequest,
    BaseRequest,
    BasiliskCustomTaskProxylessRequest,
    BasiliskCustomTaskRequest,
    DataDomeCustomTaskProxylessRequest,
    DataDomeCustomTaskRequest,
    FunCaptchaComplexImageTaskRequest,
    FuncaptchaProxylessRequest,
    FuncaptchaRequest,
    GeetestProxylessRequest,
    GeetestRequest,
    HcaptchaComplexImageTaskRequest,
    HcaptchaProxylessRequest,
    HcaptchaRequest,
    ImageToTextRequest,
    RecaptchaComplexImageTaskRequest,
    RecaptchaV2EnterpriseProxylessRequest,
    RecaptchaV2EnterpriseRequest,
    RecaptchaV2ProxylessRequest,
    RecaptchaV2Request,
    RecaptchaV3ProxylessRequest,
    TenDiCustomTaskProxylessRequest,
    TenDiCustomTaskRequest,
    TurnstileProxylessRequest,
    TurnstileRequest,
)
from capmonstercloudclient.utils import VERSION


_instance_config: (type, typing.Callable) = (
    (RecaptchaV2ProxylessRequest | RecaptchaV2Request, get_recaptcha_v2_timeouts),
    (
        RecaptchaV2EnterpriseProxylessRequest | RecaptchaV2EnterpriseRequest,
        get_recaptcha_v2_enterprise_timeouts,
    ),
    (RecaptchaV3ProxylessRequest, get_recaptcha_v3_timeouts),
    (ImageToTextRequest, get_image2_text_timeouts),
    (FuncaptchaProxylessRequest | FuncaptchaRequest, get_funcaptcha_timeouts),
    (HcaptchaProxylessRequest | HcaptchaRequest, get_hcaptcha_timeouts),
    (GeetestProxylessRequest | GeetestRequest, get_geetest_timeouts),
    (TurnstileProxylessRequest | TurnstileRequest, get_turnstile_timeouts),
    (
        RecaptchaComplexImageTaskRequest
        | HcaptchaComplexImageTaskRequest
        | FunCaptchaComplexImageTaskRequest,
        get_image2_text_timeouts,
    ),
    (DataDomeCustomTaskRequest | DataDomeCustomTaskProxylessRequest, get_datadome_timeouts),
    (TenDiCustomTaskRequest | TenDiCustomTaskProxylessRequest, get_ten_di_timeouts),
    (BasiliskCustomTaskRequest | BasiliskCustomTaskProxylessRequest, get_basilisk_timeouts),
    (AmazonWafRequest | AmazonWafProxylessRequest, get_amazon_waf_timeouts),
)


class CapMonsterClient:
    options: ClientOptions
    headers: dict[str, str]

    def __init__(self, options: ClientOptions) -> None:
        self.options = options
        self.headers = {"User-Agent": f"Zennolab.CapMonsterCloud.Client.Python/{VERSION}"}
        self._client = aiohttp.ClientSession()

    async def get_balance(self) -> dict[str, int | float | str]:
        body = {"clientKey": self.options.api_key}
        async with (
            self._client.post(
                url=self.options.service_url + "/getBalance",
                json=body,
                timeout=aiohttp.ClientTimeout(total=self.options.client_timeout),
            ) as resp,
        ):
            if resp.status != HTTPStatus.OK:
                raise HTTPException(f"Cannot create task. Status code: {resp.status}.")
            result = await resp.json(content_type=None)
            if result.get("errorId") != 0:
                raise GetBalanceError(f"Cannot get balance on reason {result!s}")
            return result

    async def solve_captcha(
        self,
        request: RecaptchaV2EnterpriseProxylessRequest
        | RecaptchaV2EnterpriseRequest
        | RecaptchaV2Request
        | RecaptchaV2ProxylessRequest
        | RecaptchaV3ProxylessRequest
        | ImageToTextRequest
        | FuncaptchaProxylessRequest
        | FuncaptchaRequest
        | HcaptchaRequest
        | HcaptchaProxylessRequest
        | GeetestProxylessRequest
        | GeetestRequest
        | TurnstileProxylessRequest
        | TurnstileRequest
        | HcaptchaComplexImageTaskRequest
        | RecaptchaComplexImageTaskRequest
        | FunCaptchaComplexImageTaskRequest
        | DataDomeCustomTaskProxylessRequest
        | DataDomeCustomTaskRequest,
    ) -> dict[str, str]:
        """
        Non-blocking method for captcha solving.

        Args:
            request : This object must be an instance of "requests", otherwise an exception will be thrown
        """
        for instance_source, get_timeouts in _instance_config:
            if isinstance(request, instance_source):
                return await self._solve(request, get_timeouts())
        rs_all = "".join("\n" + x for x in REQUESTS)
        raise UnknownRequestInstanceError(
            f'Unknown request instance "{type(request)}", '
            f"expected that request will belong next instances: {rs_all}"
        )

    async def _solve(
        self,
        request: RecaptchaV2EnterpriseProxylessRequest
        | RecaptchaV2EnterpriseRequest
        | RecaptchaV2Request
        | RecaptchaV2ProxylessRequest
        | RecaptchaV3ProxylessRequest
        | ImageToTextRequest
        | FuncaptchaProxylessRequest
        | FuncaptchaRequest
        | HcaptchaRequest
        | HcaptchaProxylessRequest
        | GeetestProxylessRequest
        | GeetestRequest
        | TurnstileProxylessRequest
        | TurnstileRequest
        | HcaptchaComplexImageTaskRequest
        | RecaptchaComplexImageTaskRequest
        | FunCaptchaComplexImageTaskRequest,
        timeouts: GetResultTimeouts,
    ) -> dict[str, str]:
        get_task_response = await self._create_task(request)
        if get_task_response.get("errorId") != 0:
            raise GetTaskError(
                f'[{get_task_response.get("errorCode")}] '
                f'{get_task_response.get("errorDescription")}.'
            )
        timer = RequestController(timeout=timeouts.timeout)
        await asyncio.sleep(timeouts.first_request_delay)
        result = CaptchaResult()
        while not timer.cancel:
            get_result_response = await self._get_task_result(get_task_response.get("taskId"))

            if get_result_response.get("errorId") != 0:
                timer.stop()
                raise GetResultError(
                    f'[{get_result_response.get("errorCode")}] '
                    f'{get_result_response.get("errorDescription")}.'
                )

            if get_result_response.get("status") == "processing":
                await asyncio.sleep(timeouts.requests_interval)
                continue

            if get_result_response.get("status") == "ready":
                timer.stop()
                result.solution = get_result_response.get("solution")
                break

        if result.solution is not None:
            return result.solution
        raise TimeoutError(
            "Failed to get a solution within the maximum "
            f"response waiting interval: {timeouts.timeout:0.1f} sec."
        )

    async def _get_task_result(self, task_id: str) -> dict[str, dict | int | str | None]:
        body = {"clientKey": self.options.api_key, "taskId": task_id}
        async with (
            self._client.post(
                url=self.options.service_url + "/getTaskResult",
                json=body,
                timeout=aiohttp.ClientTimeout(total=self.options.client_timeout),
                headers=self.headers,
            ) as resp,
        ):
            if resp.status != HTTPStatus.OK:
                if resp.status == HTTPStatus.INTERNAL_SERVER_ERROR:
                    return {"errorId": 0, "status": "processing"}
                raise HTTPException(f"Cannot grab result. Status code: {resp.status}.")
            return await resp.json(content_type=None)

    async def _create_task(self, request: BaseRequest) -> dict[str, str | int]:
        task = request.get_task_dict()
        body = {
            "clientKey": self.options.api_key,
            "task": task,
            "softId": self.options.default_soft_id,
        }
        async with (
            self._client.post(
                url=self.options.service_url + "/createTask",
                json=body,
                timeout=aiohttp.ClientTimeout(total=self.options.client_timeout),
                headers=self.headers,
            ) as resp,
        ):
            if resp.status != HTTPStatus.OK:
                raise HTTPException(f"Cannot create task. Status code: {resp.status}.")
            return await resp.json(content_type=None)
