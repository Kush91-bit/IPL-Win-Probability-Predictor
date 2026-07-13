import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# Load Model
# -----------------------------
pipe = pickle.load(open("pipe.pkl", "rb"))

# -----------------------------
# Teams and Cities
# -----------------------------
teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata',
    'Delhi', 'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town',
    'Port Elizabeth', 'Durban', 'Centurion', 'East London',
    'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad',
    'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam',
    'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

# -----------------------------
# UI
# -----------------------------
st.set_page_config(
    page_title="IPL Win Predictor",
    page_icon="🏏",
    layout="centered"
)

st.title("🏏 IPL Win Probability Predictor")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox(
        "Select Batting Team",
        sorted(teams)
    )

with col2:
    bowling_team = st.selectbox(
        "Select Bowling Team",
        sorted(teams)
    )

selected_city = st.selectbox(
    "Select Host City",
    sorted(cities)
)

# -----------------------------
# User Inputs
# -----------------------------

target = st.number_input(
    "Target Score",
    min_value=1,
    max_value=300,
    step=1
)

col3, col4, col5, col6 = st.columns(4)

with col3:
    score = st.number_input(
        "Current Score",
        min_value=0,
        max_value=300,
        step=1
    )

with col4:
    overs = st.number_input(
        "Overs",
        min_value=0,
        max_value=19,
        step=1
    )

with col5:
    balls = st.selectbox(
        "Balls",
        [0, 1, 2, 3, 4, 5]
    )

with col6:
    wickets = st.number_input(
        "Wickets Lost",
        min_value=0,
        max_value=9,
        step=1
    )

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Probability"):

    # Validation
    if batting_team == bowling_team:
        st.error("Batting and Bowling teams cannot be the same.")
        st.stop()

    if score > target:
        st.error("Current score cannot be greater than target.")
        st.stop()

    balls_bowled = overs * 6 + balls

    if balls_bowled >= 120:
        st.error("Maximum overs allowed are 20.")
        st.stop()

    runs_left = target - score
    balls_left = 120 - balls_bowled
    wickets_left = 10 - wickets

    if balls_bowled == 0:
        crr = 0
    else:
        crr = score / (balls_bowled / 6)

    if balls_left == 0:
        rrr = 0
    else:
        rrr = runs_left / (balls_left / 6)

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets_left],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)

    loss = result[0][0]
    win = result[0][1]

    st.subheader("Win Probability")

    col7, col8 = st.columns(2)

    with col7:
        st.metric(
            label=batting_team,
            value=f"{win * 100:.2f}%"
        )

    with col8:
        st.metric(
            label=bowling_team,
            value=f"{loss * 100:.2f}%"
        )