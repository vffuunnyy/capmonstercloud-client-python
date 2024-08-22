from abc import ABC

from capmonstercloudclient.requests.base_request import Field
from capmonstercloudclient.requests.custom_task_request_base import CustomTaskRequestBase


class TenDiCustomTaskRequestBase(CustomTaskRequestBase, ABC):
    type: str = Field(default="CustomTask")
    captcha_class: str = Field(default="TenDI", alias="class")
    website_key: str = Field()
