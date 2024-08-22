from abc import ABC

from pydantic import Field, field_validator

from capmonstercloudclient.exceptions import (
    ExtraParamsError,
    NumbersImagesErrors,
    TaskNotDefinedError,
    ZeroImagesErrors,
)
from capmonstercloudclient.requests.complex_image_task_base import ComplexImageTaskRequestBase


class HcaptchaComplexImageTaskRequest(ComplexImageTaskRequestBase, ABC):
    captcha_class: str = Field(default="hcaptcha")
    metadata: dict[str, str]
    example_image_urls: list[str] | None
    example_images_base64: list[str] | None

    @field_validator("metadata")
    @classmethod
    def validate_metadata(cls, value: dict[str, str]) -> dict[str, str]:
        if value.get("Task") is None:
            raise TaskNotDefinedError("Expect that task will be defined.")
        return value

    @field_validator("example_image_urls")
    @classmethod
    def validate_example_urls_array(cls, value: list[str] | None) -> list[str] | None:
        if value is not None:
            if not isinstance(value, list | tuple):
                raise TypeError(
                    f"Expect that type exampleImageUrls array will be <list> or <tuple>, got {type(value)}"
                )
            if len(value) > 1:
                raise NumbersImagesErrors(f"Maximum number of images in list 1, got {len(value)}")
            if not len(value):
                raise ZeroImagesErrors(f"At least one image url expected, got {len(value)}")
            # Check for each element type
            contain_types = [isinstance(x, str) for x in value]
            if not all(contain_types):
                raise TypeError(
                    f"Next images from imagesUrls array are not string: {contain_types}"
                )
        return value

    @field_validator("example_images_base64")
    @classmethod
    def validate_example_images_base64_array(cls, value: list[str] | None) -> list[str] | None:
        if value is not None:
            if not isinstance(value, list | tuple):
                raise TypeError(
                    f"Expect that type exampleImagesBase64 array will be <list> or <tuple>, got {type(value)}"
                )
            if len(value) > 1:
                raise NumbersImagesErrors(f"Maximum number of images in list 1, got {len(value)}")
            if not len(value):
                raise ZeroImagesErrors(f"At least one image base64 expected, got {len(value)}")
            # Check for each element type
            contain_types = [isinstance(x, str) for x in value]
            if not all(contain_types):
                raise TypeError(
                    f"Next images from imagesBase64 array are not string: {contain_types}"
                )
        return value

    @field_validator("images_urls")
    @classmethod
    def validate_urls_array(cls, value: list[str] | None) -> list[str] | None:
        if value is not None:
            if not isinstance(value, list | tuple):
                raise TypeError(
                    f"Expect that type imagesUrls array will be <list> or <tuple>, got {type(value)}"
                )
            if len(value) > 18:
                raise NumbersImagesErrors(f"Maximum number of images in list 18, got {len(value)}")
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
            if len(value) > 18:
                raise NumbersImagesErrors(f"Maximum number of images in list 18, got {len(value)}")
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
        task = {"type": self.task_type, "class": self.captchaClass}

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

        if self.example_image_urls and self.example_images_base64:
            raise ExtraParamsError("Expect only one of [exampleImageUrls, exampleImagesBase64]")

        if self.example_image_urls is not None:
            task["exampleImageUrls"] = self.example_image_urls

        if self.example_images_base64 is not None:
            task["exampleImagesBase64"] = self.example_images_base64

        if self.user_agent is not None:
            task["userAgent"] = self.user_agent

        if self.website_url is not None:
            task["websiteUrl"] = self.website_url

        return task
