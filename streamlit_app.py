import streamlit as st
from PIL import Image
import os

st.title("CO₂ Dashboard (Notebook Preview) 🌍")
st.write("The Republic of Korea's CO₂ Emissions Change in Time and Compared with the Rest of the World")

image_name = st.text_input("Top10t.png", "CO2_world.png", "CO2_temp_sk.png", "CO2_temp_sk_scaled.png", "CO2_temp_sk_faceted.png")

if image_name:
    image_path = os.path.join("images", image_name)
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption=f"Loaded: {image_name}", use_column_width=True)
else: 
    st.error("Image '{image_name}' not found in the 'images' folder.")
