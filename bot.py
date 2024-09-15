from info import API_ID, API_HASH, BOT_TOKEN
from pyrogram import Client, filters
from pyrogram.types import Message

# Initialize the bot client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Handler for /start command
@app.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    await message.reply("Hello! I'm your bot. How can I assist you today?")

# Handler for /help command
@app.on_message(filters.command("help"))
async def help_handler(client: Client, message: Message):
    await message.reply("Here are the commands you can use:\n/start - Start the bot\n/help - Get help\n/request - Request a file\n/premium - Check premium features")

# Handler for /request command
@app.on_message(filters.command("request"))
async def request_handler(client: Client, message: Message):
    await message.reply("Please provide the file ID or name you want to request.")

# Handler for /premium command
@app.on_message(filters.command("premium"))
async def premium_handler(client: Client, message: Message):
    await message.reply("Here is the list of premium features you can access.")

# Handler for incoming messages to process file requests and non-command text messages
@app.on_message(filters.text)
async def handle_text_messages(client: Client, message: Message):
    # Check if the message is not a command
    if not message.text.startswith('/'):
        if "file" in message.text.lower():
            await message.reply("It seems like you're requesting a file. Please use the /request command.")

# Additional logic for handling premium users or point systems
@app.on_message(filters.text)
async def handle_premium_users(client: Client, message: Message):
    user_id = message.from_user.id
    if is_premium_user(user_id):
        await message.reply("You are a premium user. Enjoy your features!")
    else:
        await message.reply("You are not a premium user. Upgrade to access more features.")

def is_premium_user(user_id: int) -> bool:
    # Dummy function for checking premium status
    premium_users = [123456789, 987654321]  # Example list of premium user IDs
    return user_id in premium_users

if __name__ == "__main__":
    app.run()
