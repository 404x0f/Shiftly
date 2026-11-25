from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Мои смены",
        callback_data="my_shifts",
    )
    builder.button(
        text="Создать смену",
        callback_data="create_shift",
    )
    builder.button(
        text="Мой профиль",
        callback_data="my_profile",
    )
    builder.button(
        text="Настройки",
        callback_data="settings",
    )

    builder.adjust(2)

    return builder.as_markup()