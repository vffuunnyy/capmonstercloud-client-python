from abc import ABC

from pydantic import Field, field_validator

from capmonstercloudclient.exceptions import (
    NumbersImagesErrors,
    TaskNotDefinedError,
    ZeroImagesErrors,
)
from capmonstercloudclient.requests.complex_image_task_base import ComplexImageTaskRequestBase


class FunCaptchaComplexImageTaskRequest(ComplexImageTaskRequestBase, ABC):
    captcha_class: str = Field(default="funcaptcha")
    metadata: dict[str, str]

    @field_validator("metadata")
    @classmethod
    def validate_metadata(cls, value: dict[str, str]) -> dict[str, str]:
        if value.get("Task") is None:
            raise TaskNotDefinedError("Expect that task will be defined.")
        return value

    @field_validator("images_urls")
    @classmethod
    def validate_urls_array(cls, value: list[str] | tuple[str]) -> list[str] | tuple[str]:
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
    def validate_images_array(cls, value: list[str] | tuple[str]) -> list[str] | tuple[str]:
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

    def get_task_dict(self) -> dict[str, str | int | bool]:
        task = {"type": self.task_type, "class": self.captcha_class}

        # fill with images
        if self.images_base64 is None and self.images_urls is None:
            raise ZeroImagesErrors(
                "Expect at least one of array(imageBase64 or imageUrls) to contain images."
            )

        if self.images_urls is not None:
            task["imageUrls"] = self.images_urls

        if self.images_base64 is not None:
            task["imagesBase64"] = self.images_base64

        task["metadata"] = self.metadata

        if self.user_agent is not None:
            task["userAgent"] = self.user_agent

        if self.website_url is not None:
            task["websiteUrl"] = self.website_url

        return task
