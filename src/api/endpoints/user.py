from fastapi import APIRouter

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
    return await user_crud.create_user(data, session)