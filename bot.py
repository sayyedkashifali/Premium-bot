import os
from pyrogram import Client
from flask import Flask
import threading

# API credentials
api_id = 27317700
api_hash = "de1077f45e29e6abebcd2b9dd196be1d"
bot_token = "7335984411:AAGwpqyCseguoIBo5wlW-Uqzos3NuCUiLcQ"

# Create the Flask app for the dummy web server
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

# Start Flask server in a separate thread to avoid blocking the bot
def run_server():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# Start the Telegram bot
telegram_app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

def start_bot():
    telegram_app.run()

# Run both the Flask app and Telegram bot
if __name__ == "__main__":
    threading.Thread(target=run_server).start()
    start_bot()
