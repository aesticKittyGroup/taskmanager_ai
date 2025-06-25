from aiogram import Bot, Dispatcher
from bot.handlers import routers

async def start_bot():
    bot = Bot(token="7429942015:AAHhCsWHuYHnPO1B6ocdtoYnhng5BwRI0j0")
    dp = Dispatcher()
    for r in routers:
        dp.include_router(r)
        
    await dp.start_polling(bot)    