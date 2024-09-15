from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time
import config  # Import the config module to use environment variables

# Initialize the bot using environment variables from config
app = Client(
    "my_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! I am your bot.")

@app.on_message(filters.command("help"))
async def help(client, message):
    await message.reply("How can I assist you?")

@app.on_message()
async def handle_message(client, message):
    try:
        # Your message handling logic
        pass
    except FloodWait as e:
        print(f"FloodWait exception caught: Waiting for {e.x} seconds.")
        time.sleep(e.x)
        # Optionally retry the operation after waiting
        # You may need to handle retry logic based on your specific needs

if __name__ == "__main__":
    app.run()
