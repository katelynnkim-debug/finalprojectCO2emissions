import streamlit as st
from PIL import Image
import os

st.title("CO₂ Dashboard (Notebook Preview) 🌍")
st.write("The Republic of Korea's CO₂ Emissions Change in Time and Compared with the Rest of the World")

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/Top10t.png?raw=true"
st.image(image_url, caption="Top 10 CO2 Emission Producing Countries", use_container_width=True)
st.write("The dark blue color at the start of South Korea's plot at 1945 and its gradual blend into a lighter greenish yellow color as the year approaches 2014 clearly shows that the country only started emitting large amounts of CO2 emissions in 1945, towards the end of World War II, and started a steady incline of even more copious amounts of CO2 emissions until 2014, where South Korea has now caught up to most of the other top 10 CO2 emission-producing countries, as seen by the common shade of lighter greenish yellow.")

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/CO2_world.png?raw=true"
st.image(image_url, caption="World CO2 Emissions Per Year (1751-2014)", use_container_width=True)

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/CO2_temp_sk_scaled.png?raw=true"
st.image(image_url, caption="South Korea's Emissions and Temperatures (1980-2014) - Linear Regression Plot", use_container_width=True)

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/CO2_temp_sk_facet.png?raw=true"
st.image(image_url, caption="South Korea's Emissions and Temperatures (1980-2014) - Facet Plot", use_container_width=True)
