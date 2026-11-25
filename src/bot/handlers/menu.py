from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == "my_shifts")
async def my_shifts(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "Здесь будут твои смены."
    )


@router.callback_query(F.data == "create_shift")
async def create_shift(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "Давай создадим новую смену."
    )


@router.callback_query(F.data == "my_profile")
async def my_profile(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "Открываю твой профиль."
    )


@router.callback_query(F.data == "settings")
async def settings(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "Настройки."
    )