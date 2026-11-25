from sqlalchemy import BigInteger, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
    )
    username: Mapped[str | None] = mapped_column(
        String(255),
        nullable=False,
    )
    hourly_rate: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )
    shifts: Mapped[list['Shift']] = relationship(
        back_populates='user',
    )