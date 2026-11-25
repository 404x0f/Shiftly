from fastapi import APIRouter, HTTPException, status

from src.core.dependencies import SessionDep
from src.crud.user import user_crud
from src.schemas.user import UserCreate

router = APIRouter(
    prefix='/user',
)

@router.get('/{telegram_id}')
async def get_user_by_telegram_id(
    telegram_id: int,
    session: SessionDep,
):
    user = await user_crud.get_by_telegram_id_or_none(telegram_id, session)
    if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
    return user

@router.post('/registration')
async def registration(
    data: UserCreate,
    session: SessionDep,
):
    if await user_crud.get_by_telegram_id_or_none(data.telegram_id, session):
        return {
            'is_new': False,
            'message': 'User already exists',
        }
    else:
        await user_crud.create_user(data.telegram_id,
                                    data.username,
                                    data.hourly_rate,
                                    session)
        return {
            'is_new': True,
            'message': 'Registration successful',
        }