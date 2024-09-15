from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import config
import time

# Initialize the bot using environment variables from config.py
app = Client(
    "my_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# Handle the /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! Welcome to the bot.")

# Handle other messages
@app.on_message(filters.text)
async def handle_message(client, message):
    try:
        # Your main logic goes here
        await message.reply(f"Received: {message.text}")

    # Catch FloodWait exception and sleep for the required time
    except FloodWait as e:
        print(f"FloodWait detected. Sleeping for {e.x} seconds.")
        time.sleep(e.x)

if __name__ == "__main__":
    app.run()
