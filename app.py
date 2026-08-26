import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("🚢 Titanic Survival Prediction")

st.write("Enter passenger details")

# Inputs

pclass = st.selectbox(
    "Passenger Class",
    [1, 2, 3]
)

sex = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.number_input(
    "Age",
    min_value=0,
    max_value=100,
    value=25
)

sibsp = st.number_input(
    "Siblings/Spouse",
    min_value=0,
    max_value=10,
    value=0
)

parch = st.number_input(
    "Parents/Children",
    min_value=0,
    max_value=10,
    value=0
)

fare = st.number_input(
    "Fare",
    min_value=0.0,
    value=10.0
)

embarked = st.selectbox(
    "Embarked",
    ["S", "C", "Q"]
)

# Encoding

sex = 0 if sex == "Male" else 1

embarked_q = 1 if embarked == "Q" else 0
embarked_s = 1 if embarked == "S" else 0

# Predict Button

if st.button("Predict"):

    data = np.array([[
        pclass,
        sex,
        age,
        sibsp,
        parch,
        fare,
        embarked_q,
        embarked_s
    ]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success(
            "✅ Passenger Survived"
        )
    else:
        st.error(
            "❌ Passenger Did Not Survive"
        )