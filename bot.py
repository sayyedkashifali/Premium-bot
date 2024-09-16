import os
from pyrogram import Client, filters

# Fetching environment variables
api_id = os.getenv("27317700")
api_hash = os.getenv("de1077f45e29e6abebcd2b9dd196be1d")
bot_token = os.getenv("7335984411:AAGwpqyCseguoIBo5wlW-Uqzos3NuCUiLcQ")

# Initialize the bot with the environment variables
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Sample bot logic
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Welcome to the bot!")

# Run the bot
app.run()
