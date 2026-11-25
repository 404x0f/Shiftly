from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.models.user import User
from src.schemas.user import UserResponse


class CRUDUser:
    _get_statement = select(User).options(
        selectinload(User.shifts),
    )

    async def get_user_id_by_telegram_id(
        self,
        telegram_id: int,
        session: AsyncSession,
    ) -> int | None:
        result = await session.execute(
            select(User.id)
            .where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()

    async def get_by_telegram_id_or_none(
        self,
        telegram_id: int,
        session: AsyncSession,
    ) -> User | None:
        """Получить пользователя по телеграм id или вернуть None."""
        result = await session.execute(
            select(User)
            .where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()

    async def create_user(
        self,
        telegram_id: int,
        username: str,
        hourly_rate: int,
        session: AsyncSession,
    ) -> UserResponse:
        """Создание нового пользователя."""
        user = User(
            telegram_id=telegram_id,
            username=username,
            hourly_rate=hourly_rate
        )
    
        session.add(user)
        await session.commit()
        return UserResponse.model_validate(user)


user_crud = CRUDUser()