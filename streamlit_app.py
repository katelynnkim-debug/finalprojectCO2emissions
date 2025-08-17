import streamlit as st

st.title("CO₂ Dashboard (Notebook Preview) 🌍")
st.write("The Republic of Korea's CO₂ Emissions Change in Time and Compared with the Rest of the World")

image_folder = "plots"
image_files = [f for f in os.listdir(image_folder) if f.endswith(".png")]

for image_file in image_iles:
    image_path = os.path.join(image_folder, image_file)
    image = Image.open(image.path)

    st.subheader(f"Plot: {image_file}")
    st.image(image, use_column_width=True)
