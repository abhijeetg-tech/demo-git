import streamlit as st

st.title("This is a simple Streamlit App to display an image")
st.header("Welcome to the demo app!, we're going to display an image")
st.subheader("This app demonstrates basic Streamlit feature to display an image")
st.write("Let's display an image of a big cat!")

from PIL import Image
img = Image.open("lion.avif")
st.image(img, caption="A big cat", use_column_width=True)

# Load images
img1 = Image.open("lion.avif")
img2 = Image.open("lion.avif")
img3 = Image.open("lion.avif")

# Create 3 columns
col1, col2, col3 = st.columns(3)

# Display images in each column
with col1:
    st.image(img1, caption="Lion", use_container_width=True)

with col2:
    st.image(img2, caption="Lion", use_container_width=True)

with col3:
    st.image(img3, caption="Lion", use_container_width=True)