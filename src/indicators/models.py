import uuid
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, Text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.basemodels import Base


class Indicator(Base):
    __tablename__ = "indicators"

    name: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(Text)


class Metric(Base):
    __tablename__ = "metrics"

    name: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(Text)
    unit: Mapped[str] = mapped_column(String(200))


class IndicatorsMetric(Base):
    __tablename__ = "indicators_metrics"

    indicator_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("indicators.id", ondelete="RESTRICT")
    )
    metric_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("metrics.id", ondelete="RESTRICT")
    )

    indicator: Mapped[Indicator] = relationship(lazy="joined")
    metric: Mapped[Metric] = relationship(lazy="joined")
    reference: Mapped["Reference"] = relationship(lazy="joined")


class Reference(Base):
    __tablename__ = "references"

    min_score: Mapped[Decimal] = mapped_column(Numeric(10, 5))
    max_score: Mapped[Decimal] = mapped_column(Numeric(10, 5))
    indicator_metric_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("indicators_metrics.id", ondelete="RESTRICT")
    )


class Score(Base):
    __tablename__ = "scores"

    score: Mapped[Decimal] = mapped_column(Numeric(10, 5))
    test_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tests.id", ondelete="RESTRICT")
    )
    indicator_metric_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("indicators_metrics.id", ondelete="RESTRICT")
    )

    indicator_metric: Mapped[IndicatorsMetric] = relationship(lazy="joined")
    test: Mapped["Test"] = relationship(back_populates="results")  # noqa: F821

    @hybrid_property
    def is_within_normal_range(self) -> bool:
        return (
            self.indicator_metric.reference.min_score
            <= self.score
            <= self.indicator_metric.reference.max_score
        )

    @property
    def indicator_name(self):
        return self.indicator_metric.indicator.name

    @property
    def metric_name(self):
        return self.indicator_metric.metric.name

    @property
    def metric_unit(self):
        return self.indicator_metric.metric.unit
