import base64

from abc import ABC

from pydantic import Field, field_serializer

from capmonstercloudclient.requests.base_request import BaseRequest
from capmonstercloudclient.requests.enums import TextModules


class ImageToTextRequest(BaseRequest, ABC):
    image_bytes: bytes = Field(..., alias="body")
    type: str = "ImageToTextTask"
    module_name: TextModules | None = Field(default=None, alias="CapMonsterModule")
    threshold: int | None = Field(default=None, gt=0, le=100, alias="recognizingThreshold")
    case: bool | None = Field(default=None, alias="Case")
    numeric: int | None = Field(default=None, ge=0, le=1)
    math: bool | None = Field(default=None)

    @field_serializer("image_bytes")
    def serialize_body(self, value: bytes) -> str:
        return base64.b64encode(value).decode("utf-8")

    def get_task_dict(self) -> dict[str, str | int]:
        return self.model_dump(by_alias=True, exclude_none=True)
