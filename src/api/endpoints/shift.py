from fastapi import APIRouter

from src.core.dependencies import SessionDep
from src.crud.shift import shift_crud
from src.schemas.shift import ShiftCreate

router = APIRouter(
    prefix='/shift',
)


@router.post('/create')
async def registration(
    data: ShiftCreate,
    session: SessionDep,
):
    return await shift_crud.create_shift(data, session)