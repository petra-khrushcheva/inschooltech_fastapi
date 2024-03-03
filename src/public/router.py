from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_session
from src.public.schemas import Test
from src.public.service import get_tests
from src.users.dependencies import current_active_user as current_user

router = APIRouter(
    prefix="/tests", tags=["Tests"], dependencies=[Depends(current_user)]
)


@router.get("/tests_by_lab", response_model=List[Test])
async def get_tests_by_lab(
    lab_id: UUID, session: AsyncSession = Depends(get_session)
):
    return await get_tests(lab_id=lab_id, session=session)
