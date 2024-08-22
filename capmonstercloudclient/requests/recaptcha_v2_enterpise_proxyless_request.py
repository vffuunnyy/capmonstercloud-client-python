from pydantic import Field

from capmonstercloudclient.requests.recaptcha_v2_enterpise_request_base import (
    RecaptchaV2EnterpriseRequestBase,
)


class RecaptchaV2EnterpriseProxylessRequest(RecaptchaV2EnterpriseRequestBase):
    type: str = Field(default="RecaptchaV2EnterpriseTaskProxyless")

    def get_task_dict(self) -> dict[str, str | int]:
        return self.model_dump(by_alias=True, exclude_none=True)
