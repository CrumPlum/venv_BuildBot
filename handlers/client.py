# handlers.py
from aiogram import Dispatcher, types
from helper_init import dp, bot
from keyboards import kb_client

#@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f'->DEBUG INF Chat ID: {message.chat.id}<-\nHi-hello🙃, You stared BuildOnTon bot\nGame&chill!😉\nPress /commands for a list of commands', parse_mode='Markdown')
    await bot.send_message(message.from_user.id, 'KK', replay_markup=kb_client)

#@dp.message_handler(commands=['commands','help'])
async def commands(message: types.Message):
    await message.reply(f'/start\n/socials\n', parse_mode='Markdown')


# #Открываем файл socials.md в режиме чтения
with open('socials.md', 'r') as file:
    # Читаем содержимое файла
    content = file.read()

#@dp.message_handler(commands=['socials'])
async def socials(message: types.Message):
    await message.reply(content, parse_mode='Markdown', disable_web_page_preview=True)

def register_handlers(dp : Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(commands, commands=['commands','help'])
    dp.register_message_handler(socials, commands=['socials'])