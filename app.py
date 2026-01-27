# app.py
import streamlit as st
import pandas as pd
import joblib

# 1️ Load trained ML model
model = joblib.load("model/crop_model.pkl")

# 2️ Load crop image data
images_df = pd.read_csv("data/crop_images.csv")

st.title("🌾 AI Crop Recommendation System ")

# 3️ Input fields for soil & weather
N = st.number_input("Nitrogen (N)", min_value=0)
P = st.number_input("Phosphorus (P)", min_value=0)
K = st.number_input("Potassium (K)", min_value=0)
temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, step=1)
ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1)

# 4️ Predict button
if st.button("Recommend Crop"):
    # Prepare input DataFrame
    input_df = pd.DataFrame([[N, P, K, temp, humidity, ph, rainfall]],
                            columns=['N','P','K','temperature','humidity','ph','rainfall'])
    
    # Predict crop
    crop = model.predict(input_df)[0]
    st.success(f" Recommended Crop: {crop}")

    # 5️Show crop image from CSV
    try:
        img_url = images_df.loc[images_df['label'] == crop, 'image_url'].values[0]
        st.subheader("🌱 Crop Image")
        st.image(img_url, width=300)
    except Exception as e:
        st.info("Image not found for this crop")

    # 6️ Optional: Simple static explanation (without AI)
    # explanation_dict = {
    #     "rice": "Rice grows well in warm and humid conditions with plenty of water.",
    #     "maize": "Maize requires well-drained soil and full sunlight.",
    #     "chickpea": "Chickpea prefers cooler temperatures and moderate rainfall.",
    #     # Add explanations for all crops if needed
    # }
    # explanation = explanation_dict.get(crop, "No explanation available for this crop.")
    # st.subheader(" Explanation")
    # st.write(explanation)
