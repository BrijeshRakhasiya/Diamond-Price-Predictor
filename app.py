import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('./notebook/diamond_model.pkl')
scaler = joblib.load('./notebook/scaler.pkl')

st.title("💎 Diamond Price Prediction")

# Feature Inputs
carat = st.number_input("Carat", min_value=0.0, max_value=5.0, step=0.01)
depth = st.number_input("Depth (%)", min_value=0.0, max_value=100.0, step=0.1)
table = st.number_input("Table (%)", min_value=0.0, max_value=100.0, step=0.1)
x = st.number_input("Length (x in mm)", min_value=0.0, max_value=10.0, step=0.1)
y = st.number_input("Width (y in mm)", min_value=0.0, max_value=10.0, step=0.1)
z = st.number_input("Height (z in mm)", min_value=0.0, max_value=10.0, step=0.1)

# Categorical (Encoded)
cut = st.selectbox("Cut Quality", options=[
    ("Fair", 1),
    ("Good", 2),
    ("Very Good", 3),
    ("Premium", 4),
    ("Ideal", 5)
])

color = st.selectbox("Color Grade", options=[
    ("D", 1),
    ("E", 2),
    ("F", 3),
    ("G", 4),
    ("H", 5),
    ("I", 6),
    ("J", 7)
])

clarity = st.selectbox("Clarity", options=[
    ("I1", 1),
    ("SI2", 2),
    ("SI1", 3),
    ("VS2", 4),
    ("VS1", 5),
    ("VVS2", 6),
    ("VVS1", 7),
    ("IF", 8)
])

# Predict
if st.button("Predict 💰"):
    input_data = np.array([[carat, depth, table, x, y, z, cut[1], color[1], clarity[1]]])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    st.success(f"Estimated Diamond Price: 💲{prediction:,.2f}")
