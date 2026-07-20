import streamlit as st
import numpy as np
import joblib

# ===============================
# LOAD AI MODEL
# ===============================
model = joblib.load("fck_ai_model.pkl")

# ===============================
# PAGE CONFIGURATION
# ===============================
st.set_page_config(
    page_title="AI-Based Concrete Strength Prediction",
    layout="centered"
)

# ===============================
# TITLE
# ===============================
st.title("AI-Based Concrete Strength Prediction Tool")
st.write(
    "Prediction of Concrete Compressive Strength using "
    "Rebound Hammer (RN) and Ultrasonic Pulse Velocity (UPV)"
)

st.info(
    "Applicable for concrete strength prediction using "
    "Rebound Hammer and UPV test results."
)

# ===============================
# USER INPUTS
# ===============================
st.header("Input Parameters")

RN = st.number_input(
    "Rebound Number (RN)",
    min_value=10.0,
    max_value=60.0,
    value=30.0,
    step=0.5
)

UPV = st.number_input(
    "UPV (km/s)",
    min_value=2.0,
    max_value=6.0,
    value=4.0,
    step=0.1
)

# ===============================
# PREDICT BUTTON
# ===============================
if st.button("Predict Concrete Strength"):

    X = np.array([[RN, UPV]])

    fck = model.predict(X)[0]

    st.success(
        f"Predicted Concrete Compressive Strength = {fck:.2f} MPa"
    )

    # ===============================
    # CONCRETE QUALITY
    # ===============================
    if UPV >= 4.5:
        quality = "Excellent"

    elif UPV >= 3.5:
        quality = "Good"

    elif UPV >= 3.0:
        quality = "Medium"

    else:
        quality = "Poor"

    st.subheader("Concrete Quality")

    st.write(f"**Quality : {quality}**")

    # ===============================
    # SUMMARY
    # ===============================
    st.subheader("Prediction Summary")

    st.table(
        {
            "Parameter": [
                "Rebound Number (RN)",
                "UPV (km/s)",
                "Predicted Strength (MPa)",
                "Concrete Quality"
            ],
            "Value": [
                RN,
                UPV,
                round(fck, 2),
                quality
            ]
        }
    )