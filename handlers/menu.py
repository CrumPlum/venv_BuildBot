# handlers.py
from aiogram import Dispatcher, types
from helper_init import dp, bot

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor




# Define the menu handler
async def menu(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    
    # Define the buttons
    buttons = [
        InlineKeyboardButton(text="🏠 GAMETY?", callback_data="gamety_info"),
        InlineKeyboardButton(text="👥 Invite a Friend", callback_data="invite_friend"),
        InlineKeyboardButton(text="🏆 Leaderboard", callback_data="leaderboard"),
        InlineKeyboardButton(text="✖️ X / TWITTER", url="https://twitter.com/"),
        InlineKeyboardButton(text="💬 Groud \"Build_on_ton\"", url="https://t.me/build_on_ton")
    ]
    STARTPUNCHING = InlineKeyboardButton(text="👷🏼 Lets build!", web_app=WebAppInfo(url="https://crumplum.github.io/greenGarden"))
    # Add buttons to the keyboard
    keyboard.add(STARTPUNCHING).add(*buttons)
    
    # Send the message with the inline keyboard
    await message.answer("Welcome to GAMETY ⚔️ PUNCH TO EARN 💎", reply_markup=keyboard)

# Callback query handler
async def handle_callback(query: types.CallbackQuery):
    if query.data == "start_punching":
        await query.message.answer("👊 START PUNCHING")
    elif query.data == "gamety_info":
        await query.message.answer("⚔️ GAMETY? in developing 🏗")
    elif query.data == "invite_friend":
        await query.message.answer("✉️ Invite a Friend in developing 🏗")
    elif query.data == "leaderboard":
        await query.message.answer("🏆 Leaderboard in developing 🏗")
    await query.answer()  # Acknowledge the callback query

# Register the handlers
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(menu, commands="menu")
    dp.register_callback_query_handler(handle_callback, lambda c: c.data in [
        "start_punching",
        "gamety_info",
        "invite_friend",
        "leaderboard"
    ])



