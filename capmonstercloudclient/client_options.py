from pydantic import BaseModel, Field


class ClientOptions(BaseModel):
    api_key: str
    service_url: str = Field(default="https://api.capmonster.cloud")
    default_soft_id: int = Field(default=55)
    client_timeout: float = Field(default=20.0)
