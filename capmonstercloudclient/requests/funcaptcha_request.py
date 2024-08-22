from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.funcaptcha_request_base import FuncaptchaRequestBase
from capmonstercloudclient.requests.proxy_info import ProxyInfo


class FuncaptchaRequest(FuncaptchaRequestBase, ProxyInfo, ABC):
    type: str = Field(default="FunCaptchaTask")

    def get_task_dict(self) -> dict[str, str | int | bool]:
        task = {
            "type": self.type,
            "websiteURL": self.website_url,
            "websitePublicKey": self.website_public_key,
            "proxyType": self.proxy_type,
            "proxyAddress": self.proxy_address,
            "proxyPort": self.proxy_port,
            "proxyLogin": self.proxy_login,
            "proxyPassword": self.proxy_password,
        }
        if self.funcaptcha_api_js_subdomain is not None:
            task["funcaptchaApiJSSubdomain"] = self.funcaptcha_api_js_subdomain
        if self.data is not None:
            task["data"] = self.data
        return task
