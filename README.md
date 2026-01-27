🌾 AI Crop Recommendation System
📌 Project Overview

The AI Crop Recommendation System is a machine learning–based application that suggests the most suitable crop to grow based on soil nutrients and environmental conditions.
The system helps farmers and agricultural planners make data-driven decisions to improve crop selection efficiency.

This project focuses only on crop recommendation, not crop yield prediction.

🎯 Objectives

Recommend the best crop based on soil and weather parameters

Provide a simple and user-friendly interface using Streamlit

Use a trained machine learning model for accurate predictions

Display crop name along with its representative image

🧠 How It Works

User enters soil and climate details (N, P, K, temperature, humidity, pH, rainfall)

The trained ML model predicts the most suitable crop

The application displays:

Recommended crop name

Crop image (loaded from CSV)

🛠️ Technology Stack

Programming Language: Python

Machine Learning: Scikit-learn

Data Processing: Pandas, NumPy

Web Framework: Streamlit

Model Storage: Joblib

Dataset: CSV files

📂 Project Structure
ai-crop-recommendation/
│
├── app.py                  # Streamlit application
├── model/
│   └── crop_model.pkl      # Trained ML model
├── data/
│   ├── crop_data.csv       # Training dataset
│   └── crop_images.csv    # Crop name and image URLs
├── requirements.txt        # Required Python libraries
├── README.md               # Project documentation
└── venv/                   # Virtual environment (optional)

📊 Input Parameters

Nitrogen (N)

Phosphorus (P)

Potassium (K)

Temperature (°C)

Humidity (%)

Soil pH

Rainfall (mm)

📈 Output

✅ Recommended crop name

🌱 Crop image displayed on screen

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/ai-crop-recommendation.git
cd ai-crop-recommendation

2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit app
streamlit run app.py

📌 Key Features

Simple and interactive UI

Fast crop prediction

No paid APIs required

Fully offline ML model

Beginner-friendly project structure

⚠️ Limitations

Recommendations depend on dataset quality

No real-time weather integration

Crop yield prediction is not included

🔮 Future Enhancements

Add regional language support

Integrate real-time weather APIs

Improve model accuracy with more data

Mobile-friendly UI

👨‍💻 Author

Bala Krishna
AI & Data Engineering Enthusiast

📜 License

This project is for educational purposes only.

If you want, I can also:
