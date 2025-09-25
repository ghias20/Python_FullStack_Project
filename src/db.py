import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

# ------------------- User Management -------------------

def register_user(name, email, age, gender):
    payload = {"name": name, "email": email, "age": age, "gender": gender}
    resp = sb.table("users").insert(payload).execute()
    return resp.data

def get_user_by_name(name):
    resp = sb.table("users").select("user_id, name, email, age, gender").eq("name", name).execute()
    return resp.data

def get_user_by_email(email):
    resp = sb.table("users").select("user_id, name, email, age, gender").eq("email", email).execute()
    if resp.data:
        return resp.data[0]
    return None

def get_all_users():
    resp = sb.table("users").select("user_id, name, email, age, gender").execute()
    return resp.data

def delete_user(user_id: int):
    sb.table("workouts").delete().eq("user_id", user_id).execute()
    resp = sb.table("users").delete().eq("user_id", user_id).execute()
    return resp.data

# ------------------- Workout Management -------------------

def add_workout(user_id, exercise, duration_minutes, calories_burned):
    payload = {
        "user_id": user_id,
        "exercise": exercise,
        "duration_minutes": duration_minutes,
        "calories_burned": calories_burned
    }
    resp = sb.table("workouts").insert(payload).execute()
    return resp.data

def update_workout(workout_id: int, updates: dict):
    resp = sb.table("workouts").update(updates).eq("workout_id", workout_id).execute()
    return resp.data

def delete_workout(user_id: int, workout_id: int):
    resp = (
        sb.table("workouts")
        .delete()
        .eq("user_id", user_id)
        .eq("workout_id", workout_id)
        .execute()
    )
    return resp.data

def get_user_workouts(user_id: int):
    resp = sb.table("workouts").select(
        "workout_id, exercise, duration_minutes, calories_burned, workout_date"
    ).eq("user_id", user_id).execute()
    return resp.data

def get_total_calories(user_id: int):
    resp = sb.table("workouts").select("calories_burned").eq("user_id", user_id).execute()
    total_calories = sum(item["calories_burned"] or 0 for item in resp.data)
    return total_calories

def get_most_frequent_exercise(user_id: int):
    resp = sb.table("workouts").select("exercise").eq("user_id", user_id).execute()
    exercises = [item["exercise"] for item in resp.data if item["exercise"]]
    if not exercises:
        return None
    most_frequent = max(set(exercises), key=exercises.count)
    return most_frequent
