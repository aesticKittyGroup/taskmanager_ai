from bot.start import start_bot
import asyncio
from logger import Logger

logger = Logger.getinstance()

# pg_config = PostgreConfig(host="localhost", port=5432, username="postgres", password="pass", db_name="taskmanager_db")
# redis_config = RedisConfig(host="localhost", port=6379, db=1)

if __name__ == "__main__":
    logger.info("Бот запущен")
    asyncio.run(start_bot())
    logger.info("Бот остановлен")

