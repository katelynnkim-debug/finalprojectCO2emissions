import streamlit as st
from PIL import Image
import os

st.title("CO₂ Dashboard (Notebook Preview) 🌍")
st.write("The Republic of Korea's CO₂ Emissions Change in Time and Compared with the Rest of the World")

image_path = "plots"
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption = "Sample Plot", use_column_width = True)

else:
    st.warning(f"Image not found at {image_path}")
