from abc import ABC

from pydantic import field_validator

from capmonstercloudclient.requests.data_dome_custom_task_request_base import (
    DataDomeCustomTaskRequestBase,
)


class DataDomeCustomTaskProxylessRequest(DataDomeCustomTaskRequestBase, ABC):
    metadata: dict[str, str]

    @field_validator("metadata")
    @classmethod
    def validate_metadata(cls, value: dict[str, str]) -> dict[str, str]:
        if value.get("datadomeCookie") is None:
            raise ValueError("Expect that datadomeCookie will be defined.")
        if value.get("captchaUrl") and value.get("htmlPageBase64"):
            raise ValueError("Expected only one of [captchaUrl, htmlPageBase64]")
        if value.get("captchaUrl"):
            if not isinstance(value.get("captchaUrl"), str):
                raise ValueError(
                    f'Expect that type imagesUrls array will be <str>, got {type(value.get("captchaUrl"))}'
                )
            return {i: value[i] for i in value if i != "htmlPageBase64"}
        if value.get("htmlPageBase64"):
            if not isinstance(value.get("htmlPageBase64"), str):
                raise ValueError(
                    f'Expect that type imagesUrls array will be <str>, got {type(value.get("htmlPageBase64"))}'
                )
            return {i: value[i] for i in value if i != "captchaUrl"}
        raise ValueError("Expected one of [captchaUrl, htmlPageBase64]")

    def get_task_dict(self) -> dict[str, str | int | bool]:
        task = {
            "type": self.type,
            "class": self.captcha_class,
            "websiteURL": self.website_url,
            "metadata": self.metadata,
        }
        if self.user_agent is not None:
            task["userAgent"] = self.user_agent
        if self.domains is not None:
            task["domains"] = self.domains
        return task
