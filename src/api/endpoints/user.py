from fastapi import APIRouter
from sqlalchemy import select

from src.core.dependencies import SessionDep
from src.schemas.user import UserCreate
from src.models.user import User

router = APIRouter(
    prefix='/user',
)


@router.post('/reg')
async def registration(
    data: UserCreate,
    session: SessionDep,
):
    result = await session.execute(
        select(User).where(
            User.telegram_id == data.telegram_id
        )
    )

    user = result.scalar_one_or_none()

    if user:
        return user

    user = User(
        telegram_id=data.telegram_id,
        username=data.username,
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user