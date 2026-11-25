from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    telegram_id: int
    username: str
    hourly_rate: int | None = None


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
