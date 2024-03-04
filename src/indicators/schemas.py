from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Score(BaseModel):
    model_config = ConfigDict(from_attributes=True, coerce_numbers_to_str=True)

    id: UUID
    score: str
    indicator_name: str
    metric_name: str
    metric_unit: str
    is_within_normal_range: bool
