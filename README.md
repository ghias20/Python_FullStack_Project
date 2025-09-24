# Smart Fitness Tracker

Smart Fitness Tracker is a Python-based application that helps users log and track their workouts. Users can register, record exercises with duration and calories burned, and view reports such as total workouts, calories burned, and popular exercises. The app uses Supabase/PostgreSQL as the backend to store user and workout data, and Streamlit as FrameWork.

## Features

- **User Management**:
Register new users with name, email, age, and gender
View user profiles
- **Workout Logging**:
Record workouts with exercise type, duration, calories burned, and date
Update or delete workout entries
- **Reports & Tracking**:
View all workouts for a user
Track total calories burned over time
Filter workouts by date or exercise type
- **Search & Analytics**:
Search workouts by exercise or date
Identify most frequent exercises

## Project Structure
SmartFitnessTracker/
|
|---src/            #core application logic
|   |---logic.py    #Business logic and task
operations
|    |---db.py      #Database operations
|
|----api/           #Backend API
|    |__main.py     #FASTAPI endpoints
|----frontend/      #Frontend application
!       |__app.py   #Streamlit web interface
|
|____requirements.txt #Python Dependencies
|
|____README.md  #Project documentation
|
|____.env   #Python Variables


##  Quick Start

### Prerequisites

- Python 3.8 or higher
- A Supabase account
- Git(Push, Cloning)

### 1. Clone or Download the Project
# Option 1: Clone with Git
git clone <repository-url>

# Option 2 : Download and extract the ZIP file

### 2. Install Dependencies

# Install all required Python Packages
pip install -r requirements.txt

### 3. Set Up Supabase Database

1.Create a Supabase Project

2.Create the Task Table

-Go to the SQL Editor in your Supabase dashboard
- RUn this SQL command: 
 ``` sql
 CREATE TABLE fitness_tracker (
    id serial PRIMARY KEY,
    name text NOT NULL,
    email text UNIQUE NOT NULL,
    age int,
    gender text,
    exercise text,
    duration_minutes int,
    calories_burned int,
    workout_date date DEFAULT CURRENT_DATE
);
 ```
3. **Get Your Credentials:
### 4. Configure Environment Variables

1. Create a `.env` file in the project root

2. Add your Supabase credentials to`.env`:
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here

**Example**
SUPABASE_URL=https://abcdefghijklmnop.supabase.co
SUPABASE_KEY=eyJh....

### 5. Run the Application

### Streamlit Frontend
streamlit run frontend/app.py

The app will open in your browser at `http://localhost:0000`
## FastAPI Backend

cd api
python main.py
The API will be available at `http://localhost:8000`

## How to Use

## Technical Details

## technologies Used

- **Frontend**: Streamlit(Python web framework)
- **Backend**: FastAPI (Python REST API framework)
- **Database**: Supabase(PostgreSQL-based backend-as-a-service)
- **Language**: Python 3.8+

### Key Components

1. **`src/db.py`**: Database operations 
    - Handles all CRUD operations with supabase

2. **`src/logic.py`**: Business logic
    - Task validation and processing
3. **`api/main.py`**: Backend API endpoints
    - Provides FastAPI endpoints for frontend to interact with the database
4. **`frontend/app.py`**: Streamlit web interface
    - Implements the user interface
5. **`requirements.txt`**: Python dependencies
    - Lists all required packages
6. **`README.ms`**: Project Documentation
    - Provides project overview, features, setup instructions, and usage guide
7. **`.env`**: Environment variables
    - Stores sensitive credentials such as Supabase URL and API key

## Troubleshooting

## Common Issues

## Future Enhancements

## Support

If you encounter any issues or have questions:
Contact:
    - Ph.no : 9550622686
    - email-id : pashaghias@gmail.com