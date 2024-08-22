from abc import ABC

from capmonstercloudclient.requests.base_request import BaseRequest


class ComplexImageTaskRequestBase(BaseRequest, ABC):
    captcha_class: str  # Class(subtype) of ComplexImageTask
    task_type: str = "ComplexImageTask"  # Recognition task type
    website_url: str | None = None  # Address of a webpage with captcha
    images_urls: list[str] | None = (
        None  # Collection with image urls. Must be populated if <see cref="ImagesBase64"/> not.
    )
    images_base64: list[str] | None = (
        None  # Collection with base64 encoded images. Must be populated if <see cref="ImageUrls"/> not.
    )
    user_agent: str | None = None  # It is required that you use a signature of a modern browser
