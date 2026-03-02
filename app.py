import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("stroke_model.pkl")

st.title("🧠 Stroke Risk Prediction System")

gender = st.selectbox("Gender", ["Female", "Male", "Other"])
age = st.number_input("Age", min_value=1, max_value=120)
hypertension = st.selectbox("Hypertension", ["No", "Yes"])
heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
ever_married = st.selectbox("Ever Married", ["No", "Yes"])
work_type = st.selectbox("Work Type", ["Never worked","Govt job","Private","Self-employed","Children"])
residence = st.selectbox("Residence Type", ["Rural", "Urban"])
avg_glucose = st.number_input("Average Glucose Level", min_value=40.0, max_value=300.0)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0)
smoking = st.selectbox("Smoking Status", ["Never smoked","Formerly smoked","Smokes","Unknown"])

gender_map = {"Female":0,"Male":1,"Other":2}
work_map = {"Never worked":0,"Govt job":1,"Private":2,"Self-employed":3,"Children":4}
smoking_map = {"Never smoked":0,"Formerly smoked":1,"Smokes":2,"Unknown":3}

if st.button("Predict Stroke Risk"):
    input_df = pd.DataFrame([{
        "gender": gender_map[gender],
        "age": age,
        "hypertension": 1 if hypertension=="Yes" else 0,
        "heart_disease": 1 if heart_disease=="Yes" else 0,
        "ever_married": 1 if ever_married=="Yes" else 0,
        "work_type": work_map[work_type],
        "Residence_type": 1 if residence=="Urban" else 0,
        "avg_glucose_level": avg_glucose,
        "bmi": bmi,
        "smoking_status": smoking_map[smoking]
    }])

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Stroke! Consult doctor.")
    else:
        st.success("✅ No Stroke Risk Detected.")
