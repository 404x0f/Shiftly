from datetime import date as DateType
from datetime import time

from pydantic import BaseModel, ConfigDict


class ShiftBase(BaseModel):
    date: DateType
    start_time: time
    end_time: time


class ShiftCreate(ShiftBase):
    telegram_id: int


class ShiftResponse(ShiftBase):
    model_config = ConfigDict(from_attributes=True)
