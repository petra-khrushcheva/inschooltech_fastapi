from uuid import UUID
from pydantic import BaseModel


class Score(BaseModel):
    id: UUID
    score: str
    indicator_name: str
    metric_name: str
    metric_unit: str
    is_within_normal_range: bool
