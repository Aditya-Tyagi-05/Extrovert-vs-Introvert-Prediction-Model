import streamlit as st
import pandas as pd
import pickle
import warnings


warnings.filterwarnings("ignore")


@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

st.title("🧠 Personality Type Predictor")
st.markdown("Enter the following details to predict whether the person is an **Introvert** or **Extrovert**.")

with st.form("input_form"):
    
    time_spent_alone = st.slider("Time Spent Alone (hrs/day)", 0.0, 24.0, 4.0)
    social_event_attendance = st.slider("Social Event Attendance (per month)", 0.0, 30.0, 4.0)
    going_outside = st.slider("How often do you go outside? (times/week)", 0.0, 14.0, 6.0)
    friends_circle_size = st.slider("Number of Friends", 0.0, 100.0, 13.0)
    post_frequency = st.slider("Social Media Post Frequency (per week)", 0.0, 20.0, 5.0)

    
    stage_fear = st.radio("Do you have stage fear?", ["Yes", "No"], horizontal=True)
    drained = st.radio("Do you feel drained after socializing?", ["Yes", "No"], horizontal=True)

    
    binary_map = {"Yes": 1, "No": 0}
    stage_fear_val = binary_map[stage_fear]
    drained_val = binary_map[drained]

    submitted = st.form_submit_button("Predict")


if submitted:
    input_data = pd.DataFrame([{
        'Time_spent_Alone': time_spent_alone,
        'Stage_fear': stage_fear_val,
        'Social_event_attendance': social_event_attendance,
        'Going_outside': going_outside,
        'Drained_after_socializing': drained_val,
        'Friends_circle_size': friends_circle_size,
        'Post_frequency': post_frequency
    }])

    prediction = model.predict(input_data)[0]
    label = "Introvert" if prediction == 1 else "Extrovert"
    st.success(f"🎉 Predicted Personality Type: **{label}**")


st.markdown(
    "<hr style='margin-top:50px;'>"
    "<p style='text-align: center; color: grey;'>Created by Aadi</p>",
    unsafe_allow_html=True
)
