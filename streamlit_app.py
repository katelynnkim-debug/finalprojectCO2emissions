import streamlit as st
from PIL import Image
import os

st.title("CO₂ Dashboard (Notebook Preview) 🌍")
st.write("The Republic of Korea's CO₂ Emissions Change in Time and Compared with the Rest of the World")

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/Top10t.png?raw=true"
st.image(image_url, caption="Top 10 CO2 Emission Producing Countries", use_container_width=True)

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/CO2_world.png?raw=true"
st.image(image_url, caption="World CO2 Emissions Per Year (1751-2014)", use_container_width=True)

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/CO2_temp_sk_scaled.png?raw=true"
st.image(image_url, caption="South Korea's Emissions and Temperatures (1980-2014) - Linear Regression Plot", use_container_width=True)

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/CO2_temp_sk_facet.png?raw=true"
st.image(image_url, caption="South Korea's Emissions and Temperatures (1980-2014) - Facet Plot", use_container_width=True)
