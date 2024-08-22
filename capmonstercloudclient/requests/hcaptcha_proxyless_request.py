from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.hcaptcha_request_base import HcaptchaRequestBase


class HcaptchaProxylessRequest(HcaptchaRequestBase, ABC):
    type: str = Field(default="HCaptchaTaskProxyless")

    def get_task_dict(self) -> dict[str, str | int | bool]:
        task = {"type": self.type, "websiteURL": self.website_url, "websiteKey": self.website_key}
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
