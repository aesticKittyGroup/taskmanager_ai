from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from logger import Logger
from bot.handlers.main_keyboards import start_keyboard
from taskmanager_api import TaskManagerAPI

logger = Logger.getinstance()
router = Router()



tm = TaskManagerAPI

@router.message(CommandStart())
async def start(message: Message):
    logger.info("Приветсвенное сообщение")
    users = await tm.get_users()
    user_id = message.chat.id
    user = await tm.get_user_info(user_id)
    if not user:
        await tm.add_new_user(user_id, message.from_user.username, message.from_user.first_name)
    logger.info(f"users {users}")
    await message.answer("hello world",reply_markup=start_keyboard())

@router.message(F.text == "Посмотреть задачи")
async def check_tasks(message: Message):
    logger.info(f"check_tasks, user_id: {message.chat.id}")
    user_id = message.chat.id
    await message.answer(f"{user_id}\nВаши задачи: (Задачи)")
    

@router.message(F.text == "Статистика")
async def user_info(message: Message):
    logger.info(f"user_info, user_id: {message.chat.id}")
    await message.answer("Ваша статиситика:\nВыполнено заданий: 000\nНевыполненых заданий: 000")
    

@router.message(F.text == "Редактировать задачи")
async def edit_tasks(message: Message):
    logger.info(f"edit_tasks, user_id: {message.chat.id}")
    await message.answer(f"Ваши задачи: ...\nКакую задачу вы хотите изменить?")
    


    
    