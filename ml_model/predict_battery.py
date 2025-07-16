import joblib
import pandas as pd

model = joblib.load("ml_model/battery_model.pkl")

def predict_battery_usage(distance, elevation, weight, speed, ac_on):
    features = pd.DataFrame([{
        "distance_km": distance,
        "elevation_gain_m": elevation,
        "weight_kg": weight,
        "avg_speed": speed,
        "ac_on": ac_on
    }])
    predicted = model.predict(features)[0]
    return round(predicted, 2)
