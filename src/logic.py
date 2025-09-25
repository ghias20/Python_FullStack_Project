from src import db

class SmartFitnessTracker:
    def __init__(self):
        pass

    # ---------- User ----------
    def register_user(self, name, email, age, gender):
        existing = db.get_user_by_email(email)
        if existing:
            return f"User with email({email}) already exists."
        return db.register_user(name, email, age, gender)

    def get_user_details(self, email):
        user = db.get_user_by_email(email)
        if not user:
            return f"No user found with email({email})."
        return user

    def get_all_users(self):
        return db.get_all_users()

    def delete_user(self, email):
        user = db.get_user_by_email(email)
        if not user:
            return f"No user found with email({email})."
        return db.delete_user(user["user_id"])

    # ---------- Workouts ----------
    def add_work(self, email, exercise, duration_minutes, calories_burned):
        if duration_minutes <= 0 or calories_burned <= 0:
            return "Duration and calories burned must be greater than zero."
        user = db.get_user_by_email(email)
        if not user:
            return f"No user found with email({email}). Please register first."
        return db.add_workout(user["user_id"], exercise, duration_minutes, calories_burned)

    def update_workout(self, email, workout_id: int, updates: dict):
        user = db.get_user_by_email(email)
        if not user:
            return f"No user found with email({email})."
        return db.update_workout(workout_id, updates)

    def delete_workout(self, email, workout_id: int):
        user = db.get_user_by_email(email)
        if not user:
            return f"No user found with email({email})."
        result = db.delete_workout(user["user_id"], workout_id)
        if not result:
            return f"No workout found with id({workout_id}) for user({email})."
        return result

    def get_user_workouts(self, email):
        user = db.get_user_by_email(email)
        if not user:
            return f"No user found with email({email})."
        return db.get_user_workouts(user["user_id"])

    def get_total_calories(self, email):
        user = db.get_user_by_email(email)
        if not user:
            return f"No user found with email({email})."
        return db.get_total_calories(user["user_id"])

    def get_most_frequent_exercise(self, email):
        user = db.get_user_by_email(email)
        if not user:
            return f"No user found with email({email})."
        return db.get_most_frequent_exercise(user["user_id"])
