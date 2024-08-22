from abc import ABC, abstractmethod

from pydantic import BaseModel, Field
from pydantic.alias_generators import to_camel


BaseModel.model_config["arbitrary_types_allowed"] = True
BaseModel.model_config["populate_by_name"] = True
BaseModel.model_config["alias_generator"] = to_camel


class BaseRequest(BaseModel, ABC):
    no_cache: bool = Field(default=False)

    @abstractmethod
    def get_task_dict(self) -> dict[str, str | int | bool]:
        pass
