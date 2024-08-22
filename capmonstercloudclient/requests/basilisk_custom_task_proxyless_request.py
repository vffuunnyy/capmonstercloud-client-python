from abc import ABC

from capmonstercloudclient.requests.basilisk_custom_task_tequest_base import (
    BasiliskCustomTaskRequestBase,
)


class BasiliskCustomTaskProxylessRequest(BasiliskCustomTaskRequestBase, ABC):
    def get_task_dict(self) -> dict[str, str | int | bool]:
        task = {
            "type": self.type,
            "class": self.captcha_class,
            "websiteURL": self.website_url,
            "websiteKey": self.website_key,
        }
        if self.user_agent is not None:
            task["userAgent"] = self.user_agent
        return task
