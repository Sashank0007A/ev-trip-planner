CREATE TABLE ev_models (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    model_name VARCHAR(100),
    battery_capacity_kWh FLOAT,
    range_km INT,
    weight_kg INT,
    vehicle_type VARCHAR(50)
);
