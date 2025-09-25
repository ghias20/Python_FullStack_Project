from src import db

class SmartFitnessTracker:
    def __init__(self, email: str):
        self.email = email
        self.user = db.get_user_by_email(email)
        if not self.user:
            self.user_id = None
        else:
            self.user_id = self.user["user_id"]

    def register_user(name, email, age, gender):
        existing = db.get_user_by_email(email)
        if existing:
            return f"User with email({email}) already exists."
        return db.register_user(name, email, age, gender)

    def get_user_details(self):
        if not self.user:
            return f"No user found with email({self.email})."
        return self.user

    def add_work(self, exercise, duration_minutes, calories_burned):
        if duration_minutes <= 0 or calories_burned <= 0:
            return "Duration and calories burned must be greater than zero."
        if not self.user_id:
            return f"No user found with email({self.email}). Please register first."
        return db.add_workout(self.user_id, exercise, duration_minutes, calories_burned)

    def update_workout(self, workout_id: int, updates: dict):
        return db.update_workout(workout_id, updates)

    def delete_workout(self, workout_id: int):
        return db.delete_workout(workout_id)

    def get_user_workouts(self):
        if not self.user_id:
            return f"No user found with email({self.email})."
        return db.get_user_workouts(self.user_id)

    def get_total_calories(self):
        if not self.user_id:
            return f"No user found with email({self.email})."
        return db.get_total_calories(self.user_id)

    def get_most_frequent_exercise(self):
        if not self.user_id:
            return f"No user found with email({self.email})."
        return db.get_most_frequent_exercise(self.user_id)
