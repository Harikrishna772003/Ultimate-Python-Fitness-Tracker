import streamlit as st
import pandas as pd
import numpy as np
import random
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# --- Page Configuration ---
st.set_page_config(
    page_title="🔥 Personal Fitness Tracker",
    page_icon="💪",
    layout="wide"
)

# --- Motivational Quotes ---
MOTIVATIONAL_QUOTES = [
    "💥 Keep pushing, you're stronger than you think! 💪",
    "🔥 Every drop of sweat is a step closer to your goal! 🚀",
    "🏆 Consistency beats motivation. Stay committed! 🎯",
    "🌟 Your only limit is you. Keep moving forward! ⏳",
    "🥇 Small progress is still progress. Keep going! 🙌"
]

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
        body {
            background-color: #1E1E1E;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        [data-testid="stAppViewContainer"] {
            background: url('https://source.unsplash.com/1600x900/?fitness,workout') no-repeat center center fixed;
            background-size: cover;
        }
        .stTextInput>div>div>input, .stNumberInput>div>div>input {
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .stRadio>div>label {
            color: white;
            font-weight: bold;
        }
        .centered-button {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        .stButton>button {
            background-color: #FF5733 !important;
            color: white !important;
            font-size: 20px;
            padding: 10px;
            border-radius: 10px;
            width: 50%;
            text-align: center;
            display: block;
        }
        .stButton>button:hover {
            background-color: #C70039 !important;
        }
        .result-box {
            background: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: #FFC300;
            margin-top: 20px;
        }
        .footer {
            text-align: center;
            font-size: 16px;
            color: #FFD700;
            margin-top: 20px;
            padding: 10px;
            background: rgba(0, 0, 0, 0.7);
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

# --- Load and Prepare Data ---
@st.cache_data
def load_and_prepare_data():
    calories = pd.read_csv("calories.csv")
    exercise = pd.read_csv("exercise.csv")

    df = exercise.merge(calories, on="User_ID").drop(columns="User_ID")
    df["BMI"] = df["Weight"] / ((df["Height"] / 100) ** 2)
    df["BMI"] = df["BMI"].round(2)
    df = df[["Gender", "Age", "BMI", "Duration", "Heart_Rate", "Body_Temp", "Calories"]]
    df = pd.get_dummies(df, drop_first=True)

    return df

# --- Train Model ---
@st.cache_resource
def train_model(df):
    X = df.drop("Calories", axis=1)
    y = df["Calories"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    model = RandomForestRegressor(n_estimators=1000, max_features=3, max_depth=6)
    model.fit(X_train, y_train)

    return model, X_train.columns

# --- Load Model ---
data = load_and_prepare_data()
model, feature_columns = train_model(data)

# --- Page Title ---
st.markdown("<h1 style='text-align: center; color: #FFC300;'>🔥 Personal Fitness Tracker 🔥</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #FFD700;'>Enter Your Details to Estimate Calories Burned</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- User Input Form ---
with st.form("user_input_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("🎂 Enter Your Age (10-100)", min_value=10, max_value=100, value=30)
        bmi = st.number_input("⚖️ Enter Your BMI (15.0-40.0)", min_value=15.0, max_value=40.0, value=22.5, step=0.1)
        duration = st.number_input("⏳ Exercise Duration (min) (0-35)", min_value=0, max_value=35, value=15)

    with col2:
        heart_rate = st.number_input("❤️ Heart Rate (bpm) (60-130)", min_value=60, max_value=130, value=80)
        body_temp = st.number_input("🌡️ Body Temperature (°C) (36.0-42.0)", min_value=36.0, max_value=42.0, value=37.0, step=0.1)
        gender = st.radio("⚤ Select Gender", ["Male", "Female"], horizontal=True)

    # --- Centered Submit Button ---
    st.markdown("<div class='centered-button'>", unsafe_allow_html=True)
    submit_button = st.form_submit_button("🔥 Predict Calories Burned")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Convert Inputs & Predict ---
if submit_button:
    try:
        gender_value = 1 if gender == "Male" else 0  

        # Prepare input data
        user_data = {
            "Age": age,
            "BMI": bmi,
            "Duration": duration,
            "Heart_Rate": heart_rate,
            "Body_Temp": body_temp,
            "Gender_male": gender_value,
        }

        df = pd.DataFrame([user_data])
        df = df.reindex(columns=feature_columns, fill_value=0)  # Ensure correct column order
        prediction = model.predict(df)

        # Select a random motivational quote
        slogan = random.choice(MOTIVATIONAL_QUOTES)

        st.markdown(f"""
            <div class='result-box'>
                🔥 Estimated Calories Burned: <b>{round(prediction[0], 2)} kcal</b> 🔥
                <br><br>
                <i>{slogan}</i>
            </div>
        """, unsafe_allow_html=True)

        # Slow balloon animation
        time.sleep(0.5)
        st.balloons()

        # --- App Designed Footer After the Result ---
        st.markdown("<div class='footer'>🔥 App Designed by <b>T.HARIKRISHNA</b></div>", unsafe_allow_html=True)

    except ValueError:
        st.error("❌ Please enter valid numerical values for all fields.")
