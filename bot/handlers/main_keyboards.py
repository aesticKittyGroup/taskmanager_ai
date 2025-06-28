from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Посмотреть задачи"), 
                                              KeyboardButton(text="Статистика")], 
                                             [KeyboardButton(text="Редактировать задачи"),
                                              KeyboardButton(text="Удалить задачу")]], resize_keyboard=True)
    return keyboard