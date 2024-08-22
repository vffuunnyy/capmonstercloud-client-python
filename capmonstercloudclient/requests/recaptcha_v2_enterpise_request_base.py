from abc import ABC

from pydantic import Field, field_serializer

from capmonstercloudclient.requests.base_request import BaseRequest


class RecaptchaV2EnterpriseRequestBase(BaseRequest, ABC):
    website_url: str
    website_key: str
    enterprise_payload: str | None = Field(default=None)
    api_domain: str | None = Field(default=None)

    @field_serializer("enterprise_payload")
    def enterprise_payload_serializer(self, value: str | None) -> dict[str, str] | None:
        if value is not None:
            return {"s": self.enterprise_payload}
        return value
