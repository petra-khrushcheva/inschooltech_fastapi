import datetime
import uuid

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core import Base


class Lab(Base):
    __tablename__ = "labs"

    name: Mapped[str] = mapped_column(String(200))

    tests: Mapped[list["Test"]] = relationship(back_populates="lab")


class Test(Base):
    __tablename__ = "tests"

    started_at: Mapped[datetime.datetime]
    completed_at: Mapped[datetime.datetime]
    comment: Mapped[str | None] = mapped_column(Text)
    lab_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("labs.id", ondelete="RESTRICT")
    )

    lab: Mapped["Lab"] = relationship(back_populates="tests")
    results: Mapped[list["Score"]] = relationship(  # noqa: F821
        back_populates="test"
    )

    @hybrid_property
    def duration_seconds(self):
        return int((self.completed_at - self.started_at).total_seconds())
