import asyncio
from bot.telegram import dp, bot_instance

import bot.commands
from db.init_db import init_db

async def main():
    print("start bot")
    init_db()
    await dp.start_polling(bot_instance)

asyncio.run(main())