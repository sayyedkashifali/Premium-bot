# Available Instagram IDs for sale
instagram_ids = ["@insta_1", "@insta_2", "@insta_3"]

def buy_instagram_id(client, callback_query):
    user_id = callback_query.from_user.id
    if user_points.get(user_id, 0) >= 50:  # Assume 50 points needed to buy an ID
        user_points[user_id] -= 50  # Deducting points
        if instagram_ids:
            sold_id = instagram_ids.pop(0)
            callback_query.message.reply(f"Your Instagram ID is {sold_id}.")
        else:
            callback_query.message.reply("No Instagram IDs available.")
    else:
        callback_query.message.reply("You don't have enough points.")
