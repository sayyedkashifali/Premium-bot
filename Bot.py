from pyrogram import Client, filters

app = Client("my_bot", bot_token="7525512389:AAHmt4CO_2DwQkAAYnARrfVG0H_3FaWpYkk")

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Hello! I am your new bot.")

app.run()
