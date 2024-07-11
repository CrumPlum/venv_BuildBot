from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
import sys


from aiogram import Dispatcher, types
from helper_init import dp, bot

#from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# # Получение пути к родительскому каталогу
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# # Добавление родительского каталога в sys.path
# sys.path.append(parent_dir)
# from helper_init import bot, dp

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#рабочая, без действия на кнопку
# from aiogram import types, Dispatcher
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# # Define the menu handler
# async def menu(message: types.Message):
#     keyboard = InlineKeyboardMarkup(row_width=2)
    
#     # Define the buttons
#     buttons = [
#         InlineKeyboardButton(text="👊 menu building!", callback_data="menu_building"),
#         InlineKeyboardButton(text="⚔️ GAMETY?", callback_data="gamety_info"),
#         InlineKeyboardButton(text="✉️ Invite a Friend", callback_data="invite_friend"),
#         InlineKeyboardButton(text="🧑‍💼 Your Profile", callback_data="your_profile"),
#         InlineKeyboardButton(text="🏆 Leaderboard", callback_data="leaderboard"),
#         InlineKeyboardButton(text="❌ X / TWITTER", url="https://twitter.com/gametyio"),
#         InlineKeyboardButton(text="💬 CHAT", url="https://t.me/gametyio"),
#         InlineKeyboardButton(text="🎮 Other Games", callback_data="other_games")
#     ]
    
#     # Add buttons to the keyboard
#     keyboard.add(*buttons)
    
#     # Send the message with the inline keyboard
#     await message.answer("Welcome to GAMETY ⚔️ PUNCH TO EARN 💎", reply_markup=keyboard)



# # Register the handler
# def register_handlers(dp: Dispatcher):
#     dp.register_message_handler(menu, commands="menu")
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#рабочая
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Define the menu handler
async def menu(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    
    # Define the buttons
    buttons = [
        InlineKeyboardButton(text="🏠 Start building!", callback_data="menu_building"),
        InlineKeyboardButton(text="👷🏼 How to play?", callback_data="gamety_info"),
        InlineKeyboardButton(text="✉️ Invite a Friend", callback_data="invite_friend"),
        InlineKeyboardButton(text="👤 Your Profile", callback_data="your_profile"),
        InlineKeyboardButton(text="🏆 Leaderboard", callback_data="leaderboard"),
        InlineKeyboardButton(text="✖️ X / TWITTER", url="https://twitter.com"),
        InlineKeyboardButton(text="💬 CHAT", url="https://t.me/chat"),
        #InlineKeyboardButton(text="🎮 Other Games", callback_data="other_games")
    ]
    
    # Add buttons to the keyboard
    keyboard.add(*buttons)
    
    # Send the message with the inline keyboard
    await message.answer("Welcome to how to play! Build TO EARN 🏠", reply_markup=keyboard)

# Callback query handlers
async def handle_callback(query: types.CallbackQuery):
    if query.data == "menu_building":
        await query.message.answer("🏠 Menu building")
    elif query.data == "gamety_info":
        await query.message.answer("👷🏼 How to play?")
    elif query.data == "invite_friend":
        await query.message.answer("✉️ Invite a Friend")
    elif query.data == "your_profile":
        await query.message.answer("👤 Your Profile")
    elif query.data == "leaderboard":
        await query.message.answer("🏆 Leaderboard")
    #elif query.data == "other_games":
        #await query.message.answer("Other Games")
    await query.answer()  # Acknowledge the callback query

# Register the handlers
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(menu, commands="menu")
    dp.register_callback_query_handler(handle_callback, lambda c: c.data in [
        "menu_building",
        "gamety_info",
        "invite_friend",
        "your_profile",
        "leaderboard",
        #"other_games"
    ])

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# #кнопка Menu
# urlkb = InlineKeyboardMarkup(row_width=2) # row_width=2 — 2 в ряд
# urlButton = InlineKeyboardButton(text='ccылка1', url='https://youtube.com')
# urlButton2 = InlineKeyboardButton(text='ccылка2', url='https://google.com')
# urlkb.add(urlButton, urlButton2)

# @dp.message_handler(commands='MenuTest')
# async def url_command(message : types.Message):
#     await message.answer('MenuTest', reply_markup=urlkb)
        
        
        
# executor.menuPunch_polling(dp, skip_updates=True)
