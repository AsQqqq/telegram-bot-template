import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database.base import all_user_class

ALLUSER = all_user_class('database.db')

storage = MemoryStorage()
ID = config.ADMINS

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)