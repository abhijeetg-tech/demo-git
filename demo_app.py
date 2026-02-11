import streamlit as st

st.title("This is a simple Streamlit App")
st.header("Welcome to the demo app!")
st.subheader("This app demonstrates basic Streamlit features.")

#Widgets

#Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing Widget")

#Button
if st.button("Click Here"):
    st.write("Button Clicked!")

#Function to calculate square of a number
def sqr(num):
    return num * num

num = st.number_input("Enter a number:", value=0)

if st.button("Calculate the square"):
    result = sqr(num)
    st.write(f"The square of {num} is {result}")