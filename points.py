# Simple points system
user_points = {}

def check_points(client, callback_query):
    user_id = callback_query.from_user.id
    points = user_points.get(user_id, 0)
    callback_query.message.reply(f"You have {points} points.")

def add_points(user_id, points):
    if user_id not in user_points:
        user_points[user_id] = 0
    user_points[user_id] += points
