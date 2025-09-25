import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Smart Fitness Tracker", layout="wide")
# ================= Custom Styling =================
st.markdown("""
    <style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #141E30, #243B55);
        color: #f5f5f5;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: #1B2735;
        color: white;
    }
    [data-testid="stSidebar"] .css-1v3fvcr, [data-testid="stSidebar"] .css-1d391kg {
        color: white;
    }

    /* Headings */
    h1, h2, h3 {
        color: #00D4FF !important;
        text-align: center;
        font-family: 'Trebuchet MS', sans-serif;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #00D4FF, #0077FF);
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: 0.3s;
        font-weight: bold;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #0077FF, #00D4FF);
        transform: scale(1.05);
        cursor: pointer;
    }

    /* Input fields */
    .stTextInput>div>div>input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #2A3B55;
        color: white;
        border-radius: 8px;
        border: 1px solid #00D4FF;
    }

    /* Tables */
    .stTable {
        background-color: #1E2A3A;
        border-radius: 12px;
        padding: 10px;
        color: white;
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th {
        background-color: #00D4FF;
        color: black;
        padding: 8px;
        text-align: center;
    }
    td {
        background-color: #2A3B55;
        padding: 8px;
        text-align: center;
        color: white;
    }

    /* Success & Error messages */
    .stAlert {
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
    }
    .stSuccess {
        background-color: rgba(0, 255, 100, 0.1);
        border-left: 5px solid #00FF88;
    }
    .stError {
        background-color: rgba(255, 0, 0, 0.1);
        border-left: 5px solid #FF4444;
    }

    /* Metrics style */
    [data-testid="stMetricValue"] {
        color: #00FFDD;
        font-size: 24px;
        font-weight: bold;
    }
    [data-testid="stMetricLabel"] {
        color: #f5f5f5;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Smart Fitness Tracker")

menu = ["Register User", "Add Workout", "View all Users", "View User", "View Workouts", "Update Workout", "Delete Workout","Delete User", "Statistics"]
choice = st.sidebar.selectbox("Menu", menu)

# ------------------- Register User -------------------
if choice == "Register User":
    st.subheader("Register a New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    if st.button("Register"):
        payload = {"name": name, "email": email, "age": age, "gender": gender}
        response = requests.post(f"{BASE_URL}/user/register", json=payload)
        if response.status_code == 200:
            st.success("User registered successfully!")
        else:
            st.error(response.json()["detail"]) 

# ------------------- Add Workout -------------------
elif choice == "Add Workout":
    st.subheader("Add a Workout")
    email = st.text_input("User Email")
    exercise = st.text_input("Exercise")
    duration = st.number_input("Duration (minutes)", min_value=1)
    calories = st.number_input("Calories Burned", min_value=1)
    if st.button("Add Workout"):
        payload = {"exercise": exercise, "duration_minutes": duration, "calories_burned": calories}
        response = requests.post(f"{BASE_URL}/user/workout?email={email}", json=payload)
        if response.status_code == 200:
            st.success("Workout added successfully!")
        else:
            st.error(response.json()["detail"])
# ------------------- View all Users -------------------
elif choice == "View all Users":
    st.subheader("All Registered Users")
    if st.button("Load Users"):
        response = requests.get(f"{BASE_URL}/users")
        if response.status_code == 200:
            data = response.json()
            if data:
                st.table(data)
            else:
                st.info("No users found.")
        else:
            st.error("Failed to fetch users.")

# ------------------- View Users -------------------
elif choice == "View User":
    st.subheader("View User")
    email = st.text_input("User Email")
    if st.button("Get User Details"):
        response = requests.get(f"{BASE_URL}/user?email={email}")
        if response.status_code == 200:
            data = response.json()
            st.json(data)
        else:
            st.error(response.json()["detail"])

# ------------------- View Workouts -------------------
elif choice == "View Workouts":
    st.subheader("View Workouts")
    email = st.text_input("User Email")
    if st.button("Get Workouts"):
        response = requests.get(f"{BASE_URL}/user/workouts?email={email}")
        if response.status_code == 200:
            data = response.json()
            if data:
                st.table(data)
            else:
                st.info("No workouts found.")
        else:
            st.error(response.json()["detail"])

# ------------------- Update Workout -------------------
elif choice == "Update Workout":
    st.subheader("Update Workout")
    workout_id = st.number_input("Workout ID", min_value=1)
    exercise = st.text_input("New Exercise (leave blank to skip)")
    duration = st.number_input("New Duration (minutes, leave 0 to skip)", min_value=0)
    calories = st.number_input("New Calories Burned (leave 0 to skip)", min_value=0)
    if st.button("Update"):
        payload = {}
        if exercise:
            payload["exercise"] = exercise
        if duration > 0:
            payload["duration_minutes"] = duration
        if calories > 0:
            payload["calories_burned"] = calories
        response = requests.put(f"{BASE_URL}/user/workout/{workout_id}", json=payload)
        if response.status_code == 200:
            st.success("Workout updated successfully!")
        else:
            st.error(response.json()["detail"])

# ------------------- Delete Workout -------------------
elif choice == "Delete Workout":
    st.subheader("Delete Workout")
    email = st.text_input("User Email")
    workout_id = st.number_input("Workout ID", min_value=1, step=1)

    if st.button("Delete"):
        response = requests.delete(f"{BASE_URL}/user/workout/{workout_id}?email={email}")
        if response.status_code == 200:
            st.success("Workout deleted successfully")
        else:
            st.error(response.json()["detail"])


# ------------------- Statistics -------------------
elif choice == "Statistics":
    st.subheader("User Statistics")
    email = st.text_input("User Email")
    if st.button("Get Statistics"):
        total_cal_resp = requests.get(f"{BASE_URL}/user/total_calories?email={email}")
        most_freq_resp = requests.get(f"{BASE_URL}/user/most_frequent_exercise?email={email}")
        
        if total_cal_resp.status_code == 200:
            st.write(f"**Total Calories Burned:** {total_cal_resp.json()['total_calories']}")
        else:
            st.error(total_cal_resp.json()["detail"])
        
        if most_freq_resp.status_code == 200:
            st.write(f"**Most Frequent Exercise:** {most_freq_resp.json()['most_frequent_exercise']}")
        else:
            st.error(most_freq_resp.json()["detail"])

#------------------- Delete User -------------------
elif choice == "Delete User":
    st.subheader("Delete User")
    email = st.text_input("User Email")

    if st.button("Delete User"):
        response = requests.delete(f"{BASE_URL}/user?email={email}")
        if response.status_code == 200:
            st.success(response.json()["detail"])
        else:
            st.error(response.json()["detail"])
