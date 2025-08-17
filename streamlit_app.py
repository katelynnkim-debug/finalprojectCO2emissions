import streamlit as st
from PIL import Image
import os

st.title("CO₂ Dashboard (Notebook Preview) 🌍")
st.write("The Republic of Korea's CO₂ Emissions Change in Time and Compared with the Rest of the World")

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/Top10t.png"
st.image(image_url, caption="Top 10 CO2 Emission Producing Countries", use_container_width=True)
