from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from src.indicators.schemas import Score


class Test(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    lab_id: UUID
    duration_seconds: int
    results: List[Score]
