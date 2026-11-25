from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.models.shift import Shift
from src.crud.user import user_crud
from src.schemas.shift import ShiftCreate, ShiftResponse


class CRUDShift:
    _get_statement = select(Shift).options(
        selectinload(Shift.user),
    )

    async def create_shift(
        self,
        obj_in: ShiftCreate,
        session: AsyncSession,
    ) -> ShiftResponse:
        """Создание новой смены."""
        shift = Shift(
            user_id = await user_crud.get_user_id_by_telegram_id(
                obj_in.telegram_id, session=session
            ),
            date=obj_in.date,
            start_time=obj_in.start_time,
            end_time=obj_in.end_time
        )
    
        session.add(shift)
        await session.commit()

        return ShiftResponse.model_validate(shift)


shift_crud = CRUDShift()