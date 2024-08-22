from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.base_request import BaseRequest


class HcaptchaRequestBase(BaseRequest, ABC):
    website_url: str
    website_key: str
    is_invisible: bool | None = Field(default=None)
    data: str | None = Field(default=None)
    user_agent: str | None = Field(default=None)
    cookies: str | None = Field(default=None)
    fallback_to_actual_ua: bool | None = Field(default=None)
