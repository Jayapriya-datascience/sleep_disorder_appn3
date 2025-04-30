import streamlit as st
import pickle
import numpy as np
import os
import joblib


# CSS for Multi-Color Blinking Effect
multi_color_blink_css = """
<style>
@keyframes colorBlink {
    0% {color: red;}
    25% {color: green;}
    50% {color: blue;}
    75% {color: orange;}
}
.color-blink {
    animation: colorBlink 1s infinite;
    text-align: center;
    font-weight: bold;
}
</style>
"""
st.markdown(multi_color_blink_css, unsafe_allow_html=True)

# Load Model and Scaler
model_path = os.path.join("model9", "trained_model9.pkl")
scaler_path = os.path.join("model9", "scaler9.pkl")

if not os.path.exists(model_path):
    st.error(f"❌ Model file not found! Expected at: {model_path}")
    st.stop()
if not os.path.exists(scaler_path):
    st.error(f"❌ Scaler file not found! Expected at: {scaler_path}")
    st.stop()

with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

try:
    scaler = joblib.load(scaler_path)
    if not hasattr(scaler, "transform"):
        raise TypeError("Loaded scaler is not valid.")
except Exception as e:
    st.error(f"❌ Error loading scaler: {e}")
    st.stop()

# App Title
st.markdown("""
<div style="background-color:#e6f2ff; padding:10px; border-radius:10px;">
<h2 class="color-blink">💤 Sleep Disorder Prediction App</h2>
</div>
""", unsafe_allow_html=True)

st.write("🌙 Enter your details to check for sleep disorder risk.")

# Input Fields
st.title("Personal Information")
age = st.number_input("Age", min_value=10, max_value=100, value=25)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
gender = {"Male": 0, "Female": 1, "Other": 2}[gender]

occupation = st.selectbox("Occupation", ["Nurse", "Doctor", "Engineer", "Lawyer", "Teacher", "Accountant", "Salesperson", "Student", "Others"])
occupation = {"Nurse": 0, "Doctor": 1, "Engineer": 2, "Lawyer": 3, "Teacher": 4, "Accountant": 5, "Salesperson": 6, "Student": 7, "Others": 8}[occupation]

height = st.number_input("Height (cm)", 100, 250, 170)
weight = st.number_input("Weight (kg)", 30, 200, 70)

if height > 0 and weight > 0:
    bmi = weight / ((height / 100) ** 2)
    if bmi < 18.5:
        bmi_category = 0
    elif 18.5 <= bmi < 24.9:
        bmi_category = 1
    elif 25 <= bmi < 29.9:
        bmi_category = 2
    else:
        bmi_category = 3
    st.text_input("BMI Category", value=["Underweight", "Normal", "Overweight", "Obese"][bmi_category], disabled=True)

# Sleep Details
st.title("Sleep Details")
sleep_duration = st.slider("Sleep Duration (hours)", 1.0, 12.0, 7.0)
quality_of_sleep = st.slider("Quality of Sleep (1-10)", 1, 10, 5)
st.session_state.sleep_details = {'quality_of_sleep': quality_of_sleep}  # Store it in session state
st.write()
st.markdown("""
<div style="color:blue;">
Quality of Sleep (1-10)<br>
- 1-3: Poor Sleep Quality (Frequent disturbances)  <br>
- 4-6: Fair Sleep Quality (Light sleep, not refreshing)  <br>
- 7-8: Good Sleep Quality (Mostly uninterrupted, refreshing)  <br>
- 9-10: Excellent Sleep Quality (Deep, restorative sleep)  
</div>
""", unsafe_allow_html=True)

physical_activity = st.number_input("Physical Activity Level", 0, 100, value=30,step=10)
st.write()
st.write("""
<div style="color:blue;">
Physical Activity Level (Rating 0-100)<br>
- 0: No Physical Activity  <br>
- 10-30: Low Activity (Sedentary)<br>  
- 31-60: Moderate Activity (Light exercise)<br>  
- 61-80: High Activity (Regular exercise)  <br>
- 81-100: Very High Activity (Intense daily exercise) 
</div>
""", unsafe_allow_html=True)

# Health Details
st.title("Health Details")
stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)
st.write()
st.write("""
<div style="color:blue;">
Stress Level (0-10)<br>
- 0: No Stress <br> 
- 1-3: Low Stress  <br>
- 4-6: Moderate Stress<br>  
- 7-8: High Stress  <br>
- 9-10: Extreme Stress  
</div>
""", unsafe_allow_html=True)

heart_rate = st.number_input("Heart Rate (bpm)", 40, 120, value=70)
# Daily Steps with Increase Button
daily_steps = st.number_input("Daily Steps (0-10000)", 0, 10000, value=5000,step=100)
st.write()
st.write("""
<div style="color:blue;">
Daily Steps : The average number of steps the individual takes per day
</div>
""", unsafe_allow_html=True)

systolic = st.number_input("Systolic Blood Pressure", 80, 200, value=120)
st.write()
st.write("""
<div style="color:blue;">
Systolic : The systolic blood pressure of the individual in mmHg.
</div>
""", unsafe_allow_html=True)


diastolic = st.number_input("Diastolic Blood Pressure", 50, 130, value=80)
st.write()
st.write("""
<div style="color:blue;">
Diastolic:The diastolic blood pressure of the individual in mmHg.
</div>
""", unsafe_allow_html=True)



# Prepare input
input_features = np.array([[age, gender, occupation, sleep_duration, quality_of_sleep, physical_activity,
                            stress_level, bmi_category, heart_rate, daily_steps, systolic, diastolic]])

try:
    input_features_scaled = scaler.transform(input_features)
except Exception as e:
    st.error(f"Error scaling input: {e}")
    st.stop()



# Prediction
disorder_info = {
    "Insomnia": ("Difficulty falling or staying asleep.", "Reduce caffeine, maintain a sleep schedule, try relaxation techniques."),
    "Sleep Anxiety": ("Anxiety-related sleep disturbances.", "Practice meditation, avoid screens before bed."),
    "Obstructive Sleep Apnea": ("Airway blockage during sleep.", "Lose weight, avoid alcohol, consider CPAP."),
    "Hypertension-related Sleep Issues": ("Linked to high blood pressure.", "Monitor BP, reduce salt."),
    "Restless Leg Syndrome": ("Uncontrollable urge to move legs.", "Exercise, avoid caffeine."),
    "Narcolepsy": ("Sudden sleep attacks.", "Maintain sleep schedule."),
    "General Sleep Disorder": ("Mild sleep disturbances.", "Avoid heavy meals, caffeine, and alcohol near bedtime.")
}

if st.button("🔍 Predict"):
    prediction = model.predict(input_features_scaled)
    st.session_state.prediction = prediction
    possible_disorders = []

 # ✅ Add this healthy override here
    if (bmi_category in [0, 1] and 8 <= sleep_duration <= 8.5 and
    quality_of_sleep >= 7 and stress_level <= 3 and
    systolic <= 130 and diastolic <= 85):
        
        st.success("✅ No disorder detected based on your healthy parameters! Keep maintaining your lifestyle.")
        st.session_state.possible_disorders = []
        st.subheader("🛌 Tips for Healthy Sleep")
        st.write("1. Maintain a consistent sleep schedule.")
        st.write("2. Create a relaxing bedtime routine.")
        st.write("3. Exercise regularly.")
        st.write("4. Keep your room cool, dark, and quiet.")
        st.write("5. Manage stress before sleep.")
    else:
        # existing logic to find possible disorders
        if sleep_duration < 6 or quality_of_sleep < 3:
            possible_disorders.append("Insomnia")
        if stress_level > 5:
            possible_disorders.append("Sleep Anxiety")
        if bmi_category == 3 and heart_rate > 90:
            possible_disorders.append("Obstructive Sleep Apnea")
        if systolic > 140 or diastolic > 90:
            possible_disorders.append("Hypertension-related Sleep Issues")
        if daily_steps < 3000 and physical_activity < 20:
            possible_disorders.append("Restless Leg Syndrome")
        if sleep_duration > 9 or stress_level > 3:
            possible_disorders.append("Narcolepsy")
        if not possible_disorders:
            possible_disorders.append("General Sleep Disorder")

        st.session_state.possible_disorders = possible_disorders
        st.warning(f"🛏️ **Possible Sleep Disorders:** {', '.join(possible_disorders)}")

        for disorder in possible_disorders:
            st.subheader(f"🩺 {disorder}")
            st.write(f"🔹 **Definition:** {disorder_info[disorder][0]}")
            st.write(f"💡 **Tips:** {disorder_info[disorder][1]}")



# PDF Download Section
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from datetime import datetime

def generate_pdf(disorders, inputs):
    path = "Sleep_Disorder_Report.pdf"
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    # Title with color
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.darkblue)
    c.drawString(200, height - 50, "Sleep Disorder Report")

    # Timestamp in top-right
    timestamp = datetime.now().strftime("%Y-%m-%d")
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.black)
    c.drawString(400, height - 20, f"Generated on: {timestamp}")

    y = height - 100

    # Input summary
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.darkgreen)
    c.drawString(50, y, "Input Summary:")
    y -= 20

    c.setFont("Helvetica", 11)
    c.setFillColor(colors.black)
    for key, value in inputs.items():
        c.drawString(60, y, f"{key}: {value}")
        y -= 15

    y -= 20
    # Disorder section
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.darkred)
    c.drawString(50, y, "Detected Disorders and Suggestions:")
    y -= 30

    for d in disorders:
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(colors.maroon)
        c.drawString(50, y, d)
        y -= 20

        c.setFont("Helvetica", 11)
        c.setFillColor(colors.black)
        c.drawString(50, y, f"Definition: {disorder_info[d][0]}")
        y -= 20
        c.drawString(50, y, f"Tips: {disorder_info[d][1]}")
        y -= 40

    # Sleep tips section
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.navy)
    c.drawString(50, y, "General Sleep Tips:")
    y -= 20

    sleep_tips = [
        "✔ Maintain a consistent sleep schedule.",
        "✔ Create a relaxing bedtime routine.",
        "✔ Stay physically active but avoid intense workouts before bed.",
        "✔ Optimize your sleep environment (dark, quiet, cool).",
        "✔ Manage stress with meditation, deep breathing."
    ]

    c.setFont("Helvetica", 11)
    c.setFillColor(colors.black)
    for tip in sleep_tips:
        c.drawString(50, y, tip)
        y -= 20


    # Add thank you message at the bottom
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.darkgreen)
    c.drawString(180, y - 20, "🙏 Thank you for using our Sleep Disorder Predictor!")

    c.save()
    return path


gender_map = {0: "Male", 1: "Female", 2: "Other"}
occupation_map = {
    0: "Doctor",
    1: "Engineer",
    2: "Teacher",
    3: "Nurse",
    4: "Lawyer",
    5: "Accountant",
    6: "Salesperson",
    7: "Manager",
    8: "Scientist",
    9: "Other"
}


user_input_data = {
    "Age": age,
    "Gender": gender_map.get(gender, "Unknown"),
    "Occupation": occupation_map.get(occupation, "Unknown"),
    "Height (cm)": height,
    "Weight (kg)": weight,
    "BMI Category": ["Underweight", "Normal", "Overweight", "Obese"][bmi_category],
    "Sleep Duration (hrs)": sleep_duration,
    "Quality of Sleep (1-10)": quality_of_sleep,
    "Physical Activity Level": physical_activity,
    "Stress Level (1-10)": stress_level,
    "Heart Rate (bpm)": heart_rate,
    "Daily Steps": daily_steps,
    "Systolic BP": systolic,
    "Diastolic BP": diastolic,
}

if "possible_disorders" in st.session_state and st.session_state.possible_disorders:
    pdf_file = generate_pdf(st.session_state.possible_disorders, user_input_data)
    with open(pdf_file, "rb") as file:
        st.download_button("📄 Download Report", data=file, file_name="Sleep_Disorder_Report.pdf", mime="application/pdf")

