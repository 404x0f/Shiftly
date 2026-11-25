from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.models.user import User
from src.schemas.user import UserCreate


class CRUDUser:
    _get_statement = select(User).options(
        selectinload(User.shifts),
    )

    async def create_user(
        self,
        obj_in: UserCreate,
        session: AsyncSession,
    ) -> User:
        """Создание нового пользователя."""
        result = await session.execute(
            select(User).where(
                User.telegram_id == obj_in.telegram_id
            )
        )
    
        user = result.scalar_one_or_none()
    
        if user:
            return user
    
        user = User(
            telegram_id=obj_in.telegram_id,
            username=obj_in.username,
        )
    
        session.add(user)
        await session.commit()
        await session.refresh(user)  # TODO: нужно убрать!  
        return user


user_crud = CRUDUser()