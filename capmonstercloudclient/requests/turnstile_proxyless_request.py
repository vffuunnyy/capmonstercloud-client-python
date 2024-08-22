from abc import ABC

from pydantic import Field

from capmonstercloudclient.requests.turnstile_request_base import TurnstileRequestBase


class TurnstileProxylessRequest(TurnstileRequestBase, ABC):
    type: str = Field(default="TurnstileTaskProxyless")

    def get_task_dict(self) -> dict[str, str | int]:
        return self.model_dump(by_alias=True, exclude_none=True)
