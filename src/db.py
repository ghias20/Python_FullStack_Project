import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def register_user(name, email, age, gender):
    payload = {"name": name, "email": email, "age": age, "gender": gender}
    resp = sb.table("fitness_tracker").insert(payload).execute()
    return resp.data
def get_user_by_name(name):
    resp = sb.table("fitness_tracker").select("name, email, age, gender").eq("name", name).execute()
    return resp.data
def add_workout(name, email, age, gender, exercise, duration_minutes, calories_burned):
    payload = {"name": name,"email": email,"age": age,"gender": gender,"exercise": exercise,"duration_minutes": duration_minutes,"calories_burned": calories_burned,}
    resp = sb.table("fitness_tracker").insert(payload).execute()
    return resp.data
def update_workout(id: int, updates: dict): 
    resp = sb.table("fitness_tracker").update(updates).eq("id", id).execute()
    return resp.data
def delete_workout(id: int):
    resp = sb.table("fitness_tracker").delete().eq("id", id).execute()
    return resp.data
def get_user_workouts(name: str):
    resp = sb.table("fitness_tracker").select("id, name, exercise, duration_minutes, calories_burned").eq("name", name).execute()
    return resp.data
def get_total_calories(name: str):
    resp = sb.table("fitness_tracker").select("calories_burned").eq("name", name).execute()
    total_calories = sum(item["calories_burned"] or 0 for item in resp.data)
    return total_calories
def get_most_frequent_exercise(name: str):
    resp = sb.table("fitness_tracker").select("exercise").eq("name", name).execute()
    exercises = [item["exercise"] for item in resp.data if item["exercise"]]
    if not exercises:
        return None
    most_frequent = max(set(exercises), key=exercises.count)
    return most_frequent
def filter_workouts_by_exercise(name: str, exercise: str):
    resp = sb.table("fitness_tracker").select("id, name, exercise, duration_minutes, calories_burned").eq("name", name).eq("exercise", exercise).execute()
    return resp.data
def search_workouts_by_date(name: str, date: str):
    resp = sb.table("fitness_tracker").select("id, name, exercise, duration_minutes, calories_burned, workout_date").eq("name", name).eq("workout_date", date).execute()
    return resp.data
if __name__ == "__main__":
    while True:
        print("\n==== Smart Fitness Tracker ====")
        print("1. Register User")
        print("2. Get User Details")
        print("3. Add Workout")
        print("4. Update Workout")
        print("5. Delete Workout")
        print("6. Get User Workouts")
        print("7. Get Total Calories Burned")
        print("8. Get Most Frequent Exercise")
        print("9. Filter Workouts by Exercise")
        print("10. Search Workouts by Date")
        print("0. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            print(register_user(name, email, age, gender))

        elif choice == "2":
            name = input("Enter name: ")
            print(get_user_by_name(name))

        elif choice == "3":
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            exercise = input("Enter exercise: ")
            duration = int(input("Enter duration (minutes): "))
            calories = int(input("Enter calories burned: "))
            print(add_workout(name, email, age, gender, exercise, duration, calories))

        elif choice == "4":
            workout_id = int(input("Enter workout ID: "))
            updates = {}
            if input("Update exercise? (y/n): ") == "y":
                updates["exercise"] = input("Enter new exercise: ")
            if input("Update duration? (y/n): ") == "y":
                updates["duration_minutes"] = int(input("Enter new duration: "))
            if input("Update calories? (y/n): ") == "y":
                updates["calories_burned"] = int(input("Enter new calories: "))
            print(update_workout(workout_id, updates))

        elif choice == "5":
            workout_id = int(input("Enter workout ID: "))
            print(delete_workout(workout_id))

        elif choice == "6":
            name = input("Enter name: ")
            print(get_user_workouts(name))

        elif choice == "7":
            name = input("Enter name: ")
            print("Total Calories:", get_total_calories(name))

        elif choice == "8":
            name = input("Enter name: ")
            print("Most Frequent Exercise:", get_most_frequent_exercise(name))

        elif choice == "9":
            name = input("Enter name: ")
            exercise = input("Enter exercise: ")
            print(filter_workouts_by_exercise(name, exercise))

        elif choice == "10":
            name = input("Enter name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            print(search_workouts_by_date(name, date))

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again.")
