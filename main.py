from bot.start import start_bot
import asyncio
from logger import Logger

logger = Logger.getinstance()

if __name__ == "__main__":
    logger.info("Бот запущен")
    asyncio.run(start_bot())
    logger.info("Бот остановлен")

