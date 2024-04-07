from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import get_session
from src.public.schemas import Test
from src.public.service import get_tests

router = APIRouter(prefix="/tests", tags=["Tests"])


@router.get("/tests_by_lab", response_model=List[Test])
async def get_tests_by_lab(
    lab_id: UUID, session: AsyncSession = Depends(get_session)
):
    return await get_tests(lab_id=lab_id, session=session)
