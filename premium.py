premium_users = set()

def handle_premium(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in premium_users:
        callback_query.message.reply("You already have premium access.")
    elif user_points.get(user_id, 0) >= 100:  # Assume 100 points for premium
        user_points[user_id] -= 100  # Deducting points
        premium_users.add(user_id)  # Adding user to premium
        callback_query.message.reply("You now have premium access.")
    else:
        callback_query.message.reply("You don't have enough points.")
