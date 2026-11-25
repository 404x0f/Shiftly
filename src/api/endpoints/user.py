from fastapi import APIRouter, HTTPException, status

from src.core.dependencies import SessionDep
from src.crud.user import user_crud
from src.schemas.user import UserCreate

router = APIRouter(
    prefix='/user',
)


@router.post('/registration')
async def registration(
    data: UserCreate,
    session: SessionDep,
):
    if await user_crud.get_by_telegram_id_or_none(data.telegram_id, session):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )
    else:
        return await user_crud.create_user(data.telegram_id,
                                           data.username,
                                           data.hourly_rate,
                                           session)