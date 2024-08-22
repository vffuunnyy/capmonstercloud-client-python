from abc import ABC

from pydantic import field_validator

from capmonstercloudclient.requests.data_dome_custom_task_request_base import (
    DataDomeCustomTaskRequestBase,
)
from capmonstercloudclient.requests.proxy_info import ProxyInfo


class DataDomeCustomTaskRequest(DataDomeCustomTaskRequestBase, ProxyInfo, ABC):
    metadata: dict[str, str]

    @field_validator("metadata")
    @classmethod
    def validate_metadata(cls, value: dict[str, str]) -> dict[str, str]:
        if value.get("datadomeCookie") is None:
            raise TypeError("Expect that datadomeCookie will be defined.")
        if value.get("captchaUrl") and value.get("htmlPageBase64"):
            raise TypeError("Expected only one of [captchaUrl, htmlPageBase64]")
        if value.get("captchaUrl"):
            if not isinstance(value.get("captchaUrl"), str):
                raise TypeError(
                    f'Expect that type imagesUrls array will be <str>, got {type(value.get("captchaUrl"))}'
                )
            return {i: value[i] for i in value if i != "htmlPageBase64"}
        if value.get("htmlPageBase64"):
            if not isinstance(value.get("htmlPageBase64"), str):
                raise TypeError(
                    f'Expect that type imagesUrls array will be <str>, got {type(value.get("htmlPageBase64"))}'
                )
            return {i: value[i] for i in value if i != "captchaUrl"}
        raise TypeError("Expected one of [captchaUrl, htmlPageBase64]")

    def get_task_dict(self) -> dict[str, str | int | bool]:
        task = {
            "type": self.type,
            "class": self.captcha_class,
            "websiteURL": self.website_url,
            "proxyType": self.proxy_type,
            "proxyAddress": self.proxy_address,
            "proxyPort": self.proxy_port,
            "proxyLogin": self.proxy_login,
            "proxyPassword": self.proxy_password,
            "domains": self.domains,
            "metadata": self.metadata,
        }
        if self.user_agent is not None:
            task["userAgent"] = self.user_agent
        if self.domains is not None:
            task["domains"] = self.domains
        return task
