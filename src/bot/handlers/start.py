import httpx
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.bot.api.client import api_client

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    telegram_user = message.from_user

    data = {
        "telegram_id": telegram_user.id,
        "username": telegram_user.username,
    }

    try:
        await api_client.registration_user(data=data)

        await message.answer(
            text=f"Привет, {telegram_user.username}!"  # TODO: Обязательно заменить на файл с текстами для бота!!!
        )

    except httpx.HTTPStatusError as exc:
        await message.answer(
            text=f"Ошибка регистрации: {exc.response.status_code}"
        )

    except httpx.RequestError:
        await message.answer(
            text="Сервис временно недоступен. Попробуй позже."
        )