from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.base_request import BaseRequest


class RecaptchaV3ProxylessRequest(BaseRequest, ABC):
    website_url: str
    website_key: str
    type: str = Field(default="RecaptchaV3TaskProxyless")
    min_score: float | None = Field(default=None, ge=0.1, le=0.9)
    page_action: str | None = Field(default=None)

    def get_task_dict(self) -> dict[str, str | int]:
        return self.model_dump(by_alias=True, exclude_none=True)
