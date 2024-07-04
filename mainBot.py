# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️
#from telegram import Update
#import telebot
import config #создаем config.py и пишем там: TOKEN = 'TOKEN', скрываем в .gitignore
import json, time, random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token = config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f'->DEBUG INF Chat ID: {message.chat.id}<-\nHi-hello🙃, You stared BuildOnTon bot\nGame&chill!😉\nPress /commands for a list of commands', parse_mode='Markdown')

@dp.message_handler(commands=['commands','help'])
async def commands(message: types.Message):
    await message.reply(f'/start\n/socials\n', parse_mode='Markdown')

# #Открываем файл socials.md в режиме чтения
with open('socials.md', 'r') as file:
    # Читаем содержимое файла
    content = file.read()

@dp.message_handler(commands=['socials'])
async def socials(message: types.Message):
    await message.reply(content, parse_mode='Markdown', disable_web_page_preview=True)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    while True:  # запускаем бесконечный цикл
        try:  # пробуем наладить связь с сервером Telegram
            bot.polling(none_stop=True)  # polling отправляет запросы на сервара
        except Exception as e:  # если произойдет ошибка, то
            time.sleep(3)  # подождать 3 секунды
            print(e)  # и вывести logi ошибки в консоль компьютера

#//////////////////////////////////////////////////////////////////////////////////////////    
