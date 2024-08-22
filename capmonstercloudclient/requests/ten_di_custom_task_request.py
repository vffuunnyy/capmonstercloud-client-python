from capmonstercloudclient.requests.proxy_info import ProxyInfo
from capmonstercloudclient.requests.ten_di_custom_task_request_base import (
    TenDiCustomTaskRequestBase,
)


class TenDiCustomTaskRequest(TenDiCustomTaskRequestBase, ProxyInfo):
    def get_task_dict(self) -> dict[str, str | int]:
        return self.model_dump(by_alias=True, exclude_none=True)
