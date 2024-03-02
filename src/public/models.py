import datetime
import uuid

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.basemodels import Base


class Lab(Base):
    __tablename__ = 'public.labs'

    name: Mapped[str] = mapped_column(String(200))


class Test(Base):
    __tablename__ = 'public.tests'

    started_at: Mapped[datetime.datetime]
    completed_at: Mapped[datetime.datetime]
    comment: Mapped[str | None] = mapped_column(Text)
    lab_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("public.labs.id", ondelete='RESTRICT')
    )

    results: Mapped[list["Score"]] = relationship()  # noqa: F821
