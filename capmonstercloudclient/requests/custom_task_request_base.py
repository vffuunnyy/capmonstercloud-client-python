from abc import ABC

from capmonstercloudclient.requests.base_request import BaseRequest


class CustomTaskRequestBase(BaseRequest, ABC):
    captcha_class: str  # Class(subtype) of ComplexImageTask
    type: str = "CustomTask"  # Recognition task type
    website_url: str  # Address of a webpage with captcha
    user_agent: str | None = None  # It is required that you use a signature of a modern browser
    domains: list[str] | None = (
        None  # Collection with base64 encoded images. Must be populated if <see cref="ImageUrls"/> not.
    )
