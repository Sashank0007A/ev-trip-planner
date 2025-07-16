# ml_model/train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("ml_model/battery_data.csv")

X = df[["distance_km", "elevation_gain_m", "weight_kg", "avg_speed", "ac_on"]]
y = df["battery_used_percent"]

# Split & train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "ml_model/battery_model.pkl")

print("✅ Model trained and saved.")
