from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.base_request import BaseRequest


class GeetestRequestBase(BaseRequest, ABC):
    website_url: str
    gt: str
    challenge: str | None = Field(default=None)
    version: int = Field(default=3, ge=3, le=4)
    init_parameters: dict | None = Field(default=None)
    geetest_api_server_subdomain: str | None = Field(default=None)
    geetest_get_lib: str | None = Field(default=None)
    user_agent: str | None = Field(default=None)
