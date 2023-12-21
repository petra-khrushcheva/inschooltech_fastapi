from typing import List
from uuid import UUID
from pydantic import BaseModel

from src.indicators.schemas import Score


class Test(BaseModel):
    id: UUID
    lab_id: UUID
    duration_seconds: int
    results: List[Score]
