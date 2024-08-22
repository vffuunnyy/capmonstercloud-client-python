from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.recaptcha_v2_request_base import RecaptchaV2RequestBase


class RecaptchaV2ProxylessRequest(RecaptchaV2RequestBase, ABC):
    type: str = Field(default="NoCaptchaTaskProxyless")

    def get_task_dict(self) -> dict[str, str | int]:
        return self.model_dump(by_alias=True, exclude_none=True)
