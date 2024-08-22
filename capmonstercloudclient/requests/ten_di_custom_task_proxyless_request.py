from abc import ABC

from capmonstercloudclient.requests.ten_di_custom_task_request_base import (
    TenDiCustomTaskRequestBase,
)


class TenDiCustomTaskProxylessRequest(TenDiCustomTaskRequestBase, ABC):
    def get_task_dict(self) -> dict[str, str | int]:
        return self.model_dump(by_alias=True, exclude_none=True)
