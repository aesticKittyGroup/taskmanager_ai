from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from logger import Logger

logger = Logger.getinstance()
router = Router()


@router.message(CommandStart())
async def start(message: Message):
    logger.info("Приветсвенное сообщение")
    await message.answer("hello world")


@router.message(Command("Какая погода сегодня"))
async def check_weather(message: Message):
    ...
    
    