from aiogram import Bot, Dispatcher

from src.bot.handlers.start import router as start_router
from src.core.settings import settings

bot = Bot(token=settings.telegram_bot_token)
dp = Dispatcher()

dp.include_router(start_router)
