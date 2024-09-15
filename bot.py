from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_TOKEN  # Import your token from config file

app = Client("my_bot", bot_token=7525512389:AAHmt4CO_2DwQkAAYnARrfVG0H_3FaWpYkk)

user_points = {}  # For storing user points
premium_users = set()  # For storing premium users
instagram_ids = []  # Instagram IDs list, can be loaded from a file

# Load Instagram IDs from a file
with open("ids.txt", "r") as f:
    instagram_ids = f.read().splitlines()

# Start command and menu buttons
@app.on_message(filters.command("start"))
def start(client, message):
    buttons = [[
        InlineKeyboardButton("Buy Instagram ID", callback_data="buy_id"),
        InlineKeyboardButton("Check Points", callback_data="check_points")
    ], [
        InlineKeyboardButton("Premium Features", callback_data="premium")
    ]]
    message.reply("Welcome to the bot!", reply_markup=InlineKeyboardMarkup(buttons))

# Handling callback queries from buttons
@app.on_callback_query()
def handle_button(client, callback_query):
    user_id = callback_query.from_user.id

    if callback_query.data == "buy_id":
        if user_points.get(user_id, 0) >= 50:
            if instagram_ids:
                sold_id = instagram_ids.pop(0)  # Sell first available ID
                with open("ids.txt", "w") as f:
                    f.write("\n".join(instagram_ids))  # Update the file
                callback_query.message.reply(f"Your Instagram ID: {sold_id}")
            else:
                callback_query.message.reply("No IDs available right now.")
        else:
            callback_query.message.reply("You don't have enough points.")
    
    elif callback_query.data == "check_points":
        points = user_points.get(user_id, 0)
        callback_query.message.reply(f"You have {points} points.")
    
    elif callback_query.data == "premium":
        if user_id in premium_users:
            callback_query.message.reply("You already have premium access.")
        elif user_points.get(user_id, 0) >= 100:
            premium_users.add(user_id)
            user_points[user_id] -= 100
            callback_query.message.reply("Premium access unlocked!")
        else:
            callback_query.message.reply("You don't have enough points for premium.")

# Add points manually (for testing)
@app.on_message(filters.command("add_points"))
def add_points(client, message):
    user_id = message.from_user.id
    user_points[user_id] = user_points.get(user_id, 0) + 10
    message.reply(f"Points added! You now have {user_points[user_id]} points.")

app.run()
