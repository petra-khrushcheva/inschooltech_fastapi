from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.public.models import Test


async def get_tests(session: AsyncSession, lab_id: UUID):
#     subq = (
# ...     select(func.count(address_table.c.id))
# ...     .where(user_table.c.id == address_table.c.user_id)
# ...     .scalar_subquery()
# ... )
    stmt = select(Test).where(Test.lab_id == lab_id)


#     select(User.name, func.count(Address.id).label("count"))
# ... .join(Address)
# ... .group_by(User.name)
# ... .having(func.count(Address.id) > 1)


# ...     select(Address.user_id, func.count(Address.id).label("num_addresses"))
# ...     .group_by("user_id")
# ...     .order_by("user_id", desc("num_addresses"))
