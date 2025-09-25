from src import db
def register_user(name, email, age, gender):
    existing = db.get_user_by_email(email)
    if existing:
        return f"User with email({email}) already exists."
    return db.register_user(name, email, age, gender)

def get_user_details(name):
    user = db.get_user_by_name(name)
    if not user:
        return f"No user found with name({name})."
    return user[0]

def add_work(email, exercise, duration_minutes, calories_burned):
    if duration_minutes <= 0 or calories_burned <= 0:
        return "Duration and calories burned must be greater than zero."
    
    user = db.get_user_by_email(email)
    if not user:
        return f"No user found with email({email}). Please register first."
    
    return db.add_workout(user["user_id"], exercise, duration_minutes, calories_burned)

def update_workout(workout_id: int, updates: dict):
    return db.update_workout(workout_id, updates)

def delete_workout(workout_id: int):
    return db.delete_workout(workout_id)

def get_user_workouts(email: str):
    user = db.get_user_by_email(email)
    if not user:
        return f"No user found with email({email})."
    return db.get_user_workouts(user["user_id"])

def get_total_calories(email: str):
    user = db.get_user_by_email(email)
    if not user:
        return f"No user found with email({email})."
    return db.get_total_calories(user["user_id"])

def get_most_frequent_exercise(email: str):
    user = db.get_user_by_email(email)
    if not user:
        return f"No user found with email({email})."
    return db.get_most_frequent_exercise(user["user_id"])
