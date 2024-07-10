from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
import sys

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Получение пути к родительскому каталогу
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Добавление родительского каталога в sys.path
sys.path.append(parent_dir)
from helper_init import bot, dp


#KHonxa ccwnKa
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='ccылка1', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='ccылка2', url='https://google.com')
urlkb.add(urlButton, urlButton2)

@dp.message_handler(commands='ccылки')
async def url_command(message : types.Message):
    await message.answer('ccылки', reply_markup=urlkb)
        
        
        
executor.start_polling(dp, skip_updates=True)
