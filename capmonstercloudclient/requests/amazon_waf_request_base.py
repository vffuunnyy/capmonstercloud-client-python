from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.base_request import BaseRequest


class AmazonWafRequestBase(BaseRequest, ABC):
    website_url: str
    challenge_script: str
    captcha_script: str
    website_key: str
    context: str
    iv: str
    cookie_solution: bool | None = Field(default=None)
