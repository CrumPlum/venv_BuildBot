# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮 -- 🗳️ 🏠 👷🏼
#import json, time, random
import time

from aiogram.utils import executor
from helper_init import dp, bot


from handlers import client, menu
client.register_handlers(dp)
menu.register_handlers(dp)


TOKEN = '5269574080:AAHaas4dFEG75FV1UE0uIsRUk1zWV0Ej-P0'





 
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    while True:  # запускаем бесконечный цикл
        try:  # пробуем наладить связь с сервером Telegram
            bot.polling(none_stop=True)  # polling отправляет запросы на сервара
        except Exception as e:  # если произойдет ошибка, то
            time.sleep(3)  # подождать 3 секунды
            print(e)  # и вывести logi ошибки в консоль компьютера

#//////////////////////////////////////////////////////////////////////////////////////////    
