from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.public.models import Test


async def get_tests(session: AsyncSession, lab_id: UUID):
    stmt = (
        select(Test)
        .options(selectinload(Test.results))
        .filter_by(lab_id=lab_id)
    )
    tests = await session.execute(stmt)
    return tests.scalars().all()
