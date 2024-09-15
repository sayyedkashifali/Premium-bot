from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import points
import ids
import premium
import config  # Import the config module

app = Client("my_bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

# Start command with menu buttons
@app.on_message(filters.command("start"))
def start(client, message):
    buttons = [[
        InlineKeyboardButton("Buy Instagram ID", callback_data="buy_id"),
        InlineKeyboardButton("Check Points", callback_data="check_points")
    ], [
        InlineKeyboardButton("Premium Features", callback_data="premium")
    ]]
    message.reply("Welcome to the bot!", reply_markup=InlineKeyboardMarkup(buttons))

# Handling button presses
@app.on_callback_query()
def handle_callback(client, callback_query):
    if callback_query.data == "buy_id":
        ids.buy_instagram_id(client, callback_query)  # Call function from ids.py
    elif callback_query.data == "check_points":
        points.check_points(client, callback_query)  # Call function from points.py
    elif callback_query.data == "premium":
        premium.handle_premium(client, callback_query)  # Call function from premium.py

app.run()
