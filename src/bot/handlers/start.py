import httpx
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.bot.api.client import api_client
from src.bot.keyboards.main_menu import get_main_menu
from src.bot.states.registration import RegistrationStates

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    telegram_user = message.from_user

    if telegram_user is None:
        return None # TODO: Поменять это!!!

    await state.clear()

    try:
        user = await api_client.get_user(telegram_user.id)
    except httpx.HTTPStatusError as exc:
        await message.answer(
            f"Ошибка API: {exc.response.status_code}"
        )
        return

    except httpx.RequestError:
        await message.answer(
            "Сервис временно недоступен. Попробуй позже."
        )
        return

    if user is not None:
        await message.answer(
            text=(
                f"С возвращением, {telegram_user.first_name}!\n"
                "Выбери действие:"
            ),
            reply_markup=get_main_menu(),
        )
        return

    await state.update_data(
        telegram_id=telegram_user.id,
        username=telegram_user.username,
    )

    await state.set_state(
        RegistrationStates.waiting_for_hourly_rate
    )

    await message.answer(
        text=(
            f"Привет, {telegram_user.first_name}!\n\n"
            "Давай зарегистрируемся.\n"
            "Введи свою часовую оплату."
        )
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

    except httpx.HTTPStatusError as exc:
        await message.answer(
            f"Ошибка регистрации: {exc.response.status_code}"
        )
        return

    except httpx.RequestError:
        await message.answer(
            "Сервис временно недоступен. Попробуй позже."
        )
        return

    await state.clear()

    await message.answer(
        text=(
            "Регистрация успешно завершена!\n"
            "Добро пожаловать в Shiftly."
        ),
        reply_markup=get_main_menu(),
    )