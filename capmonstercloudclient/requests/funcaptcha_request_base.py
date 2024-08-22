from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.base_request import BaseRequest


class FuncaptchaRequestBase(BaseRequest, ABC):
    website_url: str
    website_public_key: str
    funcaptcha_api_js_subdomain: str | None = Field(default=None)
    data: str | None = Field(default=None)
