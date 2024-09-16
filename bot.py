from pyrogram import Client

api_id = 27317700  # Your API ID
api_hash = "de1077f45e29e6abebcd2b9dd196be1d"  # Your API Hash
bot_token = "7335984411:AAGwpqyCseguoIBo5wlW-Uqzos3NuCUiLcQ"  # Replace with your bot token from BotFather

# Initialize the bot with the API ID, API Hash, and Bot Token
app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message()
def handle(client, message):
    message.reply("Hello! I am your bot.")

app.run()
