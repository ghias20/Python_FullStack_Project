from fastapi import FastAPI, HTTPException
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.logic import SmartFitnessTracker

# ----- App Setup -----
app = FastAPI(title="Smart Fitness Tracker API", version="1.0")

# ----- Allow frontend access -----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----- Create a single instance of SmartFitnessTracker -----
fitness_tracker = SmartFitnessTracker()

# ----- Data Models -----
class UserRegistration(BaseModel):
    name: str
    email: str
    age: int
    gender: str

class Workout(BaseModel):
    exercise: str
    duration_minutes: int
    calories_burned: int

class WorkoutUpdate(BaseModel):
    exercise: str | None = None
    duration_minutes: int | None = None
    calories_burned: int | None = None

# ----- Routes -----
@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Fitness Tracker API!"}

@app.post("/user/register")
def register_user(user: UserRegistration):
    result = fitness_tracker.register_user(user.name, user.email, user.age, user.gender)
    if isinstance(result, str):
        raise HTTPException(status_code=400, detail=result)
    return result

@app.get("/user")
def get_user(email: str):
    result = fitness_tracker.get_user_details(email)
    if isinstance(result, str):
        raise HTTPException(status_code=404, detail=result)
    return result

@app.post("/user/workout")
def add_workout(email: str, workout: Workout):
    result = fitness_tracker.add_work(email, workout.exercise, workout.duration_minutes, workout.calories_burned)
    if isinstance(result, str):
        raise HTTPException(status_code=400, detail=result)
    return result

@app.get("/user/workouts")
def get_workouts(email: str):
    result = fitness_tracker.get_user_workouts(email)
    if isinstance(result, str):
        raise HTTPException(status_code=404, detail=result)
    return result

@app.put("/user/workout/{workout_id}")
def update_workout(workout_id: int, updates: WorkoutUpdate):
    update_data = {k: v for k, v in updates.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update.")
    result = fitness_tracker.update_workout(workout_id, update_data)
    if not result:
        raise HTTPException(status_code=404, detail="Workout not found.")
    return result

@app.delete("/user/workout/{workout_id}")
def delete_workout(workout_id: int):
    result = fitness_tracker.delete_workout(workout_id)
    if not result:
        raise HTTPException(status_code=404, detail="Workout not found.")
    return {"detail": "Workout deleted successfully."}

@app.get("/user/total_calories")
def total_calories(email: str):
    result = fitness_tracker.get_total_calories(email)
    if isinstance(result, str):
        raise HTTPException(status_code=404, detail=result)
    return {"total_calories": result}

@app.get("/user/most_frequent_exercise")
def most_frequent_exercise(email: str):
    result = fitness_tracker.get_most_frequent_exercise(email)
    if isinstance(result, str):
        raise HTTPException(status_code=404, detail=result)
    return {"most_frequent_exercise": result}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0",port=8000, reload=True)