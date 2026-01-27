import pandas as pd
import joblib

# Load model
model = joblib.load("model/crop_model.pkl")

# Sample input with column names
sample_df = pd.DataFrame(
    [[90, 42, 43, 20.87, 82, 6.5, 202]],
    columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
)

# Predict
prediction = model.predict(sample_df)[0]
print("Predicted Crop:", prediction)
