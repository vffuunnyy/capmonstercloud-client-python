from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.geetest_request_base import GeetestRequestBase


class GeetestProxylessRequest(GeetestRequestBase, ABC):
    type: str = Field(default="GeeTestTaskProxyless")

    def get_task_dict(self) -> dict[str, str | int | bool]:
        task = {
            "type": self.type,
            "websiteURL": self.website_url,
            "gt": self.gt,
            "version": self.version,
        }

        if self.version == 3:
            if self.challenge is None:
                raise ValueError("Challenge value is required for 3 version Geetest.")
            task["challenge"] = self.challenge

        if self.version == 4 and self.init_parameters is not None:
            task["initParameters"] = self.init_parameters

        if self.geetest_api_server_subdomain is not None:
            task["geetestApiServerSubdomain"] = self.geetest_api_server_subdomain
        if self.geetest_get_lib is not None:
            task["geetestGetLib"] = self.geetest_get_lib
        if self.user_agent is not None:
            task["userAgent"] = self.user_agent
        return task
