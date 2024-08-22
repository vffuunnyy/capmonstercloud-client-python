from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.proxy_info import ProxyInfo
from capmonstercloudclient.requests.turnstile_request_base import TurnstileRequestBase


class TurnstileRequest(TurnstileRequestBase, ProxyInfo, ABC):
    type: str = Field(default="TurnstileTask")

    def get_task_dict(self) -> dict[str, str | int]:
        return self.model_dump(by_alias=True, exclude_none=True)
