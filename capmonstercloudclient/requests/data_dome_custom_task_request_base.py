from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.custom_task_request_base import CustomTaskRequestBase


class DataDomeCustomTaskRequestBase(CustomTaskRequestBase, ABC):
    type: str = Field(default="CustomTask")
    captcha_class: str = Field(default="DataDome")
