from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.base_request import BaseRequest


class RecaptchaV2RequestBase(BaseRequest, ABC):
    website_url: str
    website_key: str
    data_s_value: str | None = Field(default=None, alias="recaptchaDataSValue")
    user_agent: str | None = Field(default=None)
    cookies: str | None = Field(default=None)
