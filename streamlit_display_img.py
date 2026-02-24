import streamlit as st

st.title("This is a simple Streamlit App to display an image")
st.header("Welcome to the demo app!, we're going to display an image")
st.subheader("This app demonstrates basic Streamlit feature to display an image")
st.write("Let's display an image of a big cat!")

from PIL import Image
img = Image.open("lion.jpg")
st.image(img, caption="A big cat", use_column_width=True)