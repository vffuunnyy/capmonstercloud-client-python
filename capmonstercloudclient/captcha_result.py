from typing import Any

from pydantic import BaseModel


class CaptchaResult(BaseModel):
    solution: dict[str, str] | None = None

    def __eq__(self, other: Any) -> bool:
        return self.solution == other

    def __ne__(self, other: Any) -> bool:
        return self.solution != other
