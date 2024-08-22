from abc import ABC

from capmonstercloudclient.requests.basilisk_custom_task_tequest_base import (
    BasiliskCustomTaskRequestBase,
)
from capmonstercloudclient.requests.proxy_info import ProxyInfo


class BasiliskCustomTaskRequest(BasiliskCustomTaskRequestBase, ProxyInfo, ABC):
    def get_task_dict(self) -> dict[str, str | int | bool]:
        task = {
            "type": self.type,
            "class": self.captcha_class,
            "websiteURL": self.website_url,
            "websiteKey": self.website_key,
            "proxyType": self.proxy_type,
            "proxyAddress": self.proxy_address,
            "proxyPort": self.proxy_port,
            "proxyLogin": self.proxy_login,
            "proxyPassword": self.proxy_password,
        }
        if self.user_agent is not None:
            task["userAgent"] = self.user_agent
        return task
