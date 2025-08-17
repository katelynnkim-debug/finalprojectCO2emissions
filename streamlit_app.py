import streamlit as st
from PIL import Image
import os

st.title("CO₂ Dashboard (Notebook Preview) 🌍")
st.write("The Republic of Korea's CO₂ Emissions Change in Time and Compared with the Rest of the World")

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/Top10t.png?raw=true"
st.image(image_url, caption="Top 10 CO2 Emission Producing Countries", use_container_width=True)
st.write("💙💚💛 The dark blue color at the start of South Korea's plot at 1945 and its gradual blend into a lighter greenish yellow color as the year approaches 2014 clearly shows that the country only started emitting large amounts of CO2 emissions in 1945, towards the end of World War II, and started a steady incline of even more copious amounts of CO2 emissions until 2014, where South Korea has now caught up to most of the other top 10 CO2 emission-producing countries, as seen by the common shade of lighter greenish yellow.")

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/CO2_world.png?raw=true"
st.image(image_url, caption="World CO2 Emissions Per Year (1751-2014)", use_container_width=True)
st.write("💡🚗🪨 Looking at this plot, the global CO2 emissions start picking up around the mid to late 1800s, which we can most likely attribute to the Industrial Revolution which happened around the same time. The use of coal, oil, and natural gas during the Industrial Revolution in combination with the invention of the automobile probably had a lot to do with the world's emissions taking a gradual incline. Obviously, with the influx of new inventions, the expansion of the market/consumerism, and the continuation of fossil fuel use, the increase of global CO2 emissions only became steeper as time went on. Only a century and a half later, in the 2000s, the world reached 30 million metric tonnes of CO2 emissions a year and maintained a steady increase.") 

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/CO2_temp_sk_facet%20(1).png?raw=true"
st.image(image_url, caption="South Korea's Emissions and Temperatures (1980-2014) - Facet Plot", use_container_width=True)
st.write("💨🌤❄️ This facet plot shows us both variables, emissions and temperatures, plotted with its values throughout the years (1980-2014). As the years progress, both emissions and temperatures have gone up for South Korea, showing a positive association.")

image_url = "https://github.com/katelynnkim-debug/finalprojectCO2emissions/blob/main/CO2_temp_sk_scaled%20(1).png?raw=true"
st.image(image_url, caption="South Korea's Emissions and Temperatures (1980-2014) - Linear Regression Plot", use_container_width=True)
st.write("🔥🔋📈 The positive association shown by the positive slope of the trend line in this plot corroborates the argument that increased CO₂ emissions tend to coincide with warmer conditions. However, the scatter of the plotted points indicates that other influences like natural climate variability, geographic effects, or policy changes also play a role year-to-year. Ultimately, the plot still shows a moderate positive correlation, showing that the two variables, emissions and temperatures, are likely to increase when the other does.")
