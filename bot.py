from pyrogram import Client, filters
from flask import Flask
import threading

# Flask app
app_flask = Flask(__name__)

# Pyrogram Bot configuration
api_id = 27317700  # Replace with your API ID
api_hash = "de1077f45e29e6abebcd2b9dd196be1d"  # Replace with your API Hash
bot_token = "7335984411:AAGwpqyCseguoIBo5wlW-Uqzos3NuCUiLcQ"  # Replace with your Bot Token

# Pyrogram Client
bot = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Telegram Bot Command Handler for /start
@bot.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("Hello! This bot is powered by Flask and Pyrogram. How can I help you today?")

# Flask route for health check or any simple route
@app_flask.route('/')
def index():
    return "Bot is running on Flask!"

# Function to run the Flask app
def run_flask():
    app_flask.run(host='0.0.0.0', port=8080)

# Function to run the bot
def run_bot():
    bot.run()

if __name__ == "__main__":
    # Running Flask app and Telegram bot in separate threads
    t1 = threading.Thread(target=run_flask)
    t2 = threading.Thread(target=run_bot)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
