from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.funcaptcha_request_base import FuncaptchaRequestBase


class FuncaptchaProxylessRequest(FuncaptchaRequestBase, ABC):
    type: str = Field(default="FunCaptchaTaskProxyless")

    def get_task_dict(self) -> dict[str, str | int | bool]:
        task = {
            "type": self.type,
            "websiteURL": self.website_url,
            "websitePublicKey": self.website_public_key,
        }
        if self.funcaptcha_api_js_subdomain is not None:
            task["funcaptchaApiJSSubdomain"] = self.funcaptcha_api_js_subdomain
        if self.data is not None:
            task["data"] = self.data
        return task
