# ⚡ EV Trip Planner

An AI-powered Electric Vehicle (EV) trip planner that helps users check if their selected EV can complete a trip based on real-time GPS route distance and battery prediction.

---

## 🚀 Features

- Select real Indian EV models (Tata Nexon EV, MG ZS EV, Kia EV6, etc.)
- Enter source & destination using natural location names
- Get real GPS distance and time via OpenRouteService
- Predict battery usage using machine learning
- Check if the trip is possible with current battery %
- Clean GUI built using PyQt6

---

## 🛠️ Tech Stack

- Python
- PyQt6
- MySQL
- scikit-learn
- OpenRouteService API
- pandas

---

## 📁 Folder Structure

ev_trip_planner/
├── db/ # SQL scripts to create and populate EV model table
├── gui/ # PyQt6 GUI code
├── ml_model/ # Machine learning code and saved model
├── route_fetcher/ # GPS route fetching using openrouteservice
├── Screenshots/ # UI screenshots
└── ev_env/ # ❌ DO NOT upload this to GitHub (add to .gitignore)

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/ev-trip-planner.git
cd ev-trip-planner

2. Create and Activate Virtual Environment

python3 -m venv ev_env
source ev_env/bin/activate  # For macOS/Linux

3. Install Required Libraries

pip install PyQt6 pandas scikit-learn openrouteservice mysql-connector-python

4. Setup MySQL Database
Make sure MySQL server is running, then:


mysql -u root -p < db/ev_models.sql
mysql -u root -p < db/populate_ev_models.sql
This creates ev_trip_db and populates real EV model data.

5. Train the ML Model

python ml_model/train_model.py

▶️ How to Run the App

python gui/ev_trip_gui.py

Then:

Select an EV model
Enter source, destination, and current battery %
Click “🧠 Plan Trip” to get result

Replace "your_actual_api_key_here" in route_fetcher/fetch_route.py with your OpenRouteService key.
