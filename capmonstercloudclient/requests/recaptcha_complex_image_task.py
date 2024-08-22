from abc import ABC

from pydantic import Field, field_validator

from capmonstercloudclient.exceptions import (
    NumbersImagesErrors,
    TaskNotDefinedError,
    ZeroImagesErrors,
)
from capmonstercloudclient.requests.complex_image_task_base import ComplexImageTaskRequestBase


class RecaptchaComplexImageTaskRequest(ComplexImageTaskRequestBase, ABC):
    metadata: dict[str, str]
    captcha_class: str = Field(default="recaptcha", alias="class")

    @field_validator("metadata")
    @classmethod
    def validate_metadata(cls, value: dict[str, str]) -> dict[str, str]:
        if value.get("Task") is None and value.get("TaskDefinition") is None:
            raise TaskNotDefinedError(
                "Expect at least one of value(Task or TaskDefinition) will be filled."
            )
        if value.get("Grid") is None:
            raise TaskNotDefinedError('Expect that "Grid" value will be filled(3x3, 4x4, 1x1).')
        return value

    @field_validator("images_urls")
    @classmethod
    def validate_urls_array(cls, value: list[str] | None) -> list[str] | None:
        if value is not None:
            if not isinstance(value, list | tuple):
                raise TypeError(
                    f"Expect that type imagesUrls array will be <list> or <tuple>, got {type(value)}"
                )
            if len(value) > 1:
                raise NumbersImagesErrors(f"Maximum numbers images in list 1, got {len(value)}")
            if not len(value):
                raise ZeroImagesErrors(f"At least one image url expected, got {len(value)}")
            # Check for each element type
            contain_types = [isinstance(x, str) for x in value]
            if not all(contain_types):
                raise TypeError(
                    f"Next images from imagesUrls array are not string: {contain_types}"
                )
        return value

    @field_validator("images_base64")
    @classmethod
    def validate_images_array(cls, value: list[str] | None) -> list[str] | None:
        if value is not None:
            if not isinstance(value, list | tuple):
                raise TypeError(
                    f"Expect that type imagesBase64 array will be <list> or <tuple>, got {type(value)}"
                )
            if len(value) > 1:
                raise NumbersImagesErrors(f"Maximum numbers images in list 1, got {len(value)}")
            if not len(value):
                raise ZeroImagesErrors(f"At least one image base64 expected, got {len(value)}")
            # Check for each element type
            contain_types = [isinstance(x, str) for x in value]
            if not all(contain_types):
                raise TypeError(
                    f"Next images from imagesBase64 array are not string: {contain_types}"
                )
        return value

    def get_task_dict(self) -> dict[str, str | int]:
        if self.images_base64 is None and self.images_urls is None:
            raise ZeroImagesErrors(
                "Expect at least one of array(imageBase64 or imageUrls) to contain images."
            )

        return self.model_dump(by_alias=True, exclude_none=True)
