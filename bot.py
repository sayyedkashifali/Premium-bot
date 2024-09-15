import os
import logging
from pyrogram import Client, filters
from pyrogram.errors import ApiIdInvalid, AuthTokenInvalid

# Set up logging to see errors and bot actions
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Fetching environment variables
API_ID = os.getenv("27317700")
API_HASH = os.getenv("de1077f45e29e6abebcd2b9dd196be1d")
BOT_TOKEN = os.getenv("7335984411:AAGwpqyCseguoIBo5wlW-Uqzos3NuCUiLcQ")

# Check if required environment variables are provided
if not API_ID or not API_HASH or not BOT_TOKEN:
    raise ValueError("API_ID, API_HASH, and BOT_TOKEN must be set in environment variables!")

# Initialize the bot with proper API details
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Define a basic command handler for /start
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply("Hello! I am your bot. How can I assist you today?")

# Example handler for /help command
@app.on_message(filters.command("help") & filters.private)
async def help(client, message):
    await message.reply("I can assist you with various tasks. Try using /start to see what I can do.")

# Main entry point for the bot
if __name__ == "__main__":
    logger.info("Starting the bot...")
    try:
        app.run()
    except Exception as e:
        logger.error(f"Error while running the bot: {e}")
