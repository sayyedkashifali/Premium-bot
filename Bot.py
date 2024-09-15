from pyrogram import Client, filters

app = Client("my_bot", bot_token="YOUR_BOT_API_TOKEN")

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Hello! I am your new bot.")

app.run()
