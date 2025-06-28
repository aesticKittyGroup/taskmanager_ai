from aiogram import Bot, Dispatcher
from bot.handlers import routers
from taskmanager_api.data.postgre_connect import PostgreConnect
from taskmanager_api.data.config import PostgreConfig

pg_config = PostgreConfig(host="localhost", port="5432", username="postgres", password="pass", db_name="taskmanager_db")

pgc = PostgreConnect(pg_config)

async def start_bot():
    await pgc.init_db()
    bot = Bot(token="7429942015:AAHhCsWHuYHnPO1B6ocdtoYnhng5BwRI0j0")
    dp = Dispatcher()
    for r in routers:
        dp.include_router(r)
        
    await dp.start_polling(bot)