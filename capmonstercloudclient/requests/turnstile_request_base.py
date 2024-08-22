from abc import ABC
from typing import Literal

from pydantic import model_validator

from capmonstercloudclient.requests.base_request import BaseRequest, Field


class TurnstileRequestBase(BaseRequest, ABC):
    website_url: str
    website_key: str
    page_action: str | None = Field(default=None)
    data: str | None = Field(default=None)
    page_data: str | None = Field(default=None)
    user_agent: str | None = Field(default=None)
    cloudflare_task_type: Literal["cf_clearance", "token"] | None = Field(default=None)
    html_page_base64: str | None = Field(default=None)

    @model_validator(mode="before")
    def validate_cloudflare_type_token(self) -> "TurnstileRequestBase":
        if (
            self.get("html_page_base64") is None
            and self.get("cloudflare_task_type") == "cf_clearance"
        ):
            raise RuntimeError(
                'Expect that "htmlPageBase64" will be filled '
                'when cloudflareTaskType is "cf_clearance"'
            )

        if self.get("cloudflare_task_type") == "token":
            for field in ["page_action", "page_data", "data"]:
                if self.get(field) is None:
                    raise RuntimeError(
                        f'Expect that "{field}" will be filled '
                        f'when "cloudflareTaskType" = "token".'
                    )

        if (
            self.get("cloudflare_task_type") is not None
            and self.get("cloudflareTaskType") in ["cf_clearance", "token"]
            and self.get("userAgent") is None
        ):
            raise RuntimeError(
                "Expect that userAgent will be filled " "when cloudflareTaskType specified."
            )

        return self
