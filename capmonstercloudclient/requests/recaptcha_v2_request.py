from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.proxy_info import ProxyInfo
from capmonstercloudclient.requests.recaptcha_v2_request_base import RecaptchaV2RequestBase


class RecaptchaV2Request(RecaptchaV2RequestBase, ProxyInfo, ABC):
    type: str = Field(default="NoCaptchaTask")

    def get_task_dict(self) -> dict:
        return self.model_dump(by_alias=True, exclude_none=True)
