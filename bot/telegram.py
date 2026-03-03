from aiogram import Bot, Dispatcher

from config.settings import settings

bot_instance = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()