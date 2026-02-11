import streamlit as st
import pandas as pd
import pickle

def load_model():
    with open('xgb_car_price_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

st.title("Car Price Prediction App")

st.write("Enter the car details to predict the selling price.")

km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=1000000, value=50000)
milage = st.number_input("Mileage (km/l)", min_value=2, max_value=100, value=15)
age = st.number_input("Age of the Car (years)", min_value=0, max_value=20, value=5)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric"])

fuel_encoding = {
    "Petrol": [1, 0, 0],
    "Diesel": [0, 1, 0],
    "Electric": [0, 0, 1]}

petrol, diesel, electric = fuel_encoding[fuel_type]

input_df = pd.DataFrame([[km_driven, milage, age, petrol, diesel, electric]],
                        columns=['km_driven', 'mileage', 'age', 'Petrol', 'Diesel', 'Electric'])

st.dataframe(input_df)

if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.write(f"Predicted Selling Price is: ₹{prediction:,.2f}")