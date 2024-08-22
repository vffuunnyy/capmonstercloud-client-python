from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.hcaptcha_request_base import HcaptchaRequestBase
from capmonstercloudclient.requests.proxy_info import ProxyInfo


class HcaptchaRequest(HcaptchaRequestBase, ProxyInfo, ABC):
    type: str = Field(default="HCaptchaTask")

    def get_task_dict(self) -> dict[str, str | int | bool]:
        task = {
            "type": self.type,
            "websiteURL": self.website_url,
            "websiteKey": self.website_key,
            "proxyType": self.proxy_type,
            "proxyAddress": self.proxy_address,
            "proxyPort": self.proxy_port,
            "proxyLogin": self.proxy_login,
            "proxyPassword": self.proxy_password,
        }
        if self.is_invisible is not None:
            task["isInvisible"] = self.is_invisible
        if self.data is not None:
            task["data"] = self.data
        if self.user_agent is not None:
            task["userAgent"] = self.user_agent
        if self.cookies is not None:
            task["cookies"] = self.cookies
        if self.fallback_to_actual_ua is not None:
            task["fallbackToActualUA"] = self.fallback_to_actual_ua

        return task
