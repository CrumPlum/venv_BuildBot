from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('start')
b2 = KeyboardButton('commands')
b3 = KeyboardButton('socials')

kb_client = ReplyKeyboardMarkup()

kb_client.add(b1).add(b2).add(b3)
