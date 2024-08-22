from pydantic import Field

from capmonstercloudclient.requests.proxy_info import ProxyInfo
from capmonstercloudclient.requests.recaptcha_v2_enterpise_request_base import (
    RecaptchaV2EnterpriseRequestBase,
)


class RecaptchaV2EnterpriseRequest(RecaptchaV2EnterpriseRequestBase, ProxyInfo):
    type: str = Field(default="RecaptchaV2EnterpriseTask")

    def get_task_dict(self) -> dict[str, str | int]:
        return self.model_dump(by_alias=True, exclude_none=True)
