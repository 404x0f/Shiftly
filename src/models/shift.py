from datetime import date as DateType
from datetime import time

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import Base


class Shift(Base):
    __tablename__ = 'shift'

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'),
        nullable=False,
    )
    date: Mapped[DateType] = mapped_column(Date, nullable=False)
    start_time: Mapped[time] = mapped_column(nullable=False)
    end_time: Mapped[time] = mapped_column(nullable=False)
    user: Mapped['User'] = relationship(
        back_populates='shifts',
    )