from src import db
def register_user(name, email, age, gender):
    existing = db.get_user_by_name(name)
    if existing:
        return f"User with name({name}) already exists."
    return db.register_user(name, email, age, gender)
def get_user_details(name):
    user = db.get_user_by_name(name)
    if not user:
        return f"No user found with name({name})."
    return user[0]
def add_work(name, email, age, gender, exercise, duration_minutes, calories_burned):
    if duration_minutes<=0 or calories_burned<=0:
        return "Duration and calories burned must be greater than zero."
    return db.add_workout(name, email, age, gender, exercise, duration_minutes, calories_burned)
def update_workout(id: int, updates: dict):
    return db.update_workout(id, updates)
def delete_workout(id: int):
    return db.delete_workout(id)

def get_user_workouts(name: str):
    return db.get_user_workouts(name)
def get_total_calories(name: str):
    return db.get_total_calories(name)
def get_most_frequent_exercise(name: str):
    return db.get_most_frequent_exercise(name)
def filter_workouts_by_exercise(name: str, exercise: str):
    return db.filter_workouts_by_exercise(name, exercise)
def search_workouts_by_date(name: str, date: str):
    return db.search_workouts_by_date(name, date)