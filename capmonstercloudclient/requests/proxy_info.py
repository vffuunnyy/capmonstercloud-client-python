from pydantic import BaseModel

from capmonstercloudclient.requests.enums import ProxyTypes


class ProxyInfo(BaseModel):
    proxy_type: ProxyTypes
    proxy_address: str
    proxy_port: int
    proxy_login: str
    proxy_password: str
