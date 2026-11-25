import httpx
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.bot.api.client import api_client
from src.bot.states.registration import RegistrationStates

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    telegram_user = message.from_user

    if telegram_user is None:
        return None # TODO: Поменять это!!!

    await state.update_data(
        telegram_id=telegram_user.id,
        username=telegram_user.username,
    )

    await state.set_state(RegistrationStates.waiting_for_hourly_rate)

    await message.answer(
        text=f'Привет, {telegram_user.username}!\n'
             'Для продолжения работы нужно ввести вашу часовую оплату.'
    )

@router.message(RegistrationStates.waiting_for_hourly_rate)
async def process_hourly_rate(message: Message, state: FSMContext):
    if not message.text or not message.text.isdigit():
        await message.answer('Пожалуйста, числом.')
        return

    hourly_rate = int(message.text)

    user_data = await state.get_data()

    data = {
        **user_data,
        'hourly_rate': hourly_rate,
    }

    try:
        await api_client.registration_user(data=data)
        await message.answer(
            text='Успешно!'
        )

    except httpx.HTTPStatusError as exc:
        await message.answer(
            text=f"Ошибка регистрации: {exc.response.status_code}"
        )

    except httpx.RequestError:
        await message.answer(
            text="Сервис временно недоступен. Попробуй позже."
        )