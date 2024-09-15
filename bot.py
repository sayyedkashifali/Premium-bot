from pyrogram import Client, filters
from pyrogram.types import Message

# Initialize the bot
app = Client("my_bot")

# Example greeting logic
@app.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    await message.reply_text(f"Hello {message.from_user.first_name}, welcome to the bot!")

# Example file request handler
@app.on_message(filters.command("file"))
async def file_request(client: Client, message: Message):
    await message.reply_text("Which file would you like to request?")

# Logic for the point system
points = {}

@app.on_message(filters.command("buy"))
async def buy_item(client: Client, message: Message):
    user_id = message.from_user.id
    item = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    
    if not item:
        await message.reply_text("Please specify the item you want to buy.")
        return
    
    user_points = points.get(user_id, 0)
    
    if user_points >= 10:  # Assume each item costs 10 points
        points[user_id] -= 10
        await message.reply_text(f"You bought {item} for 10 points! Remaining points: {points[user_id]}")
    else:
        await message.reply_text("You don't have enough points to buy this item.")

# Adding points to user
@app.on_message(filters.command("addpoints"))
async def add_points(client: Client, message: Message):
    user_id = message.from_user.id
    points[user_id] = points.get(user_id, 0) + 10
    await message.reply_text(f"10 points added! You now have {points[user_id]} points.")

# Run the bot
if __name__ == "__main__":
    app.run()
