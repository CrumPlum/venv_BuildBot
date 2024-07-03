# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️
#from telegram import Update
#import telebot


import config
import json, time, random
#bot = telebot.TeleBot(config.TOKEN) 

#//////////////////////////////////////////////////////////////////////////////////////////
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token = config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Hello")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

#//////////////////////////////////////////////////////////////////////////////////////////    
#создаем config.py и пишем там: TOKEN = 'TOKEN'


# @bot.message_handler(commands=['start']) # /start
# def start(message):
#     bot.send_message(message.chat.id, f'Hi-hello🙃, You stared BuildOnTon bot\nGame&chill!😉\nPress /commands for a list of commands', parse_mode='Markdown')

# @bot.message_handler(commands=['commands']) # /most important commands 
# def commands(message):
#     bot.send_message(message.chat.id, f'commands:\n/getmyid\n/socials\n', parse_mode='Markdown')

# @bot.message_handler(commands=['getmyid'])  # пример создание команды, вызывать с именем /getmyid
# def getmyid(message):
#     ID = message.chat.id
#     bot.send_message(message.chat.id, f'Ваш user ID: {ID}', parse_mode='Markdown')  # получили ID пользователя и вывели на экран через f-строку

# #Открываем файл socials.md в режиме чтения
# with open('socials.md', 'r') as file:
#     # Читаем содержимое файла
#     content = file.read()
# @bot.message_handler(commands=['socials']) # /socials
# def socials(message):
#     bot.send_message(message.chat.id, content, parse_mode='Markdown', disable_web_page_preview=True)


# # Проверяем, что данный файл запущен как основная программа, а не импортирован как модуль
# if __name__ == '__main__':
#     while True:  # запускаем бесконечный цикл
#         try:  # пробуем наладить связь с сервером Telegram
#             bot.polling(none_stop=True)  # polling отправляет запросы на сервара
#         except Exception as e:  # если произойдет ошибка, то
#             time.sleep(3)  # подождать 3 секунды
#             print(e)  # и вывести logi ошибки в консоль компьютера



