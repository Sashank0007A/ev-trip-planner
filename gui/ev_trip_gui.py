import sys
import os

# Add root folder to Python path so route_fetcher & ml_model can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton,
    QTextEdit, QLineEdit
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class EVTripPlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EV Trip Planner - Smart AI Trip Estimator")
        self.setGeometry(100, 100, 650, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.font = QFont("Arial", 12)

        self.add_widgets()
        self.connect_to_db()

    def add_widgets(self):
        # EV Model Dropdown
        self.ev_label = QLabel("Select EV Model")
        self.ev_label.setFont(self.font)
        self.ev_dropdown = QComboBox()
        self.layout.addWidget(self.ev_label)
        self.layout.addWidget(self.ev_dropdown)

        # Fetch EV Details Button
        self.fetch_button = QPushButton("Select")
        self.fetch_button.clicked.connect(self.fetch_ev_details)
        self.layout.addWidget(self.fetch_button)

        # EV Details Display (blank1)
        self.ev_details_box = QTextEdit()
        self.ev_details_box.setReadOnly(True)
        self.ev_details_box.setPlaceholderText("EV specifications will appear here...")
        self.layout.addWidget(self.ev_details_box)

        # Source
        self.source_label = QLabel("Source")
        self.source_label.setFont(self.font)
        self.source_input = QLineEdit()
        self.layout.addWidget(self.source_label)
        self.layout.addWidget(self.source_input)

        # Destination
        self.dest_label = QLabel("Destination")
        self.dest_label.setFont(self.font)
        self.dest_input = QLineEdit()
        self.layout.addWidget(self.dest_label)
        self.layout.addWidget(self.dest_input)

        # Battery Input
        self.battery_label = QLabel("Current Battery %")
        self.battery_label.setFont(self.font)
        self.battery_input = QLineEdit()
        self.layout.addWidget(self.battery_label)
        self.layout.addWidget(self.battery_input)

        # Plan Trip Button
        self.plan_button = QPushButton("Plan Trip")
        self.plan_button.clicked.connect(self.plan_trip)
        self.layout.addWidget(self.plan_button)

        # Trip Result Display (blank2)
        self.trip_result_box = QTextEdit()
        self.trip_result_box.setReadOnly(True)
        self.trip_result_box.setPlaceholderText("Trip analysis will appear here...")
        self.layout.addWidget(self.trip_result_box)

    def connect_to_db(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sashank07",  # Update if needed
                database="ev_trip_db"
            )
            self.cursor = self.conn.cursor()
            self.load_ev_models()
        except mysql.connector.Error as err:
            self.ev_details_box.setText(f"DB Error:\n{err}")

    def load_ev_models(self):
        try:
            self.cursor.execute("SELECT model_name FROM ev_models;")
            models = self.cursor.fetchall()
            for model in models:
                self.ev_dropdown.addItem(model[0])
        except Exception as e:
            self.ev_details_box.setText(f"Model load error: {e}")

    def fetch_ev_details(self):
        selected_model = self.ev_dropdown.currentText()
        query = "SELECT battery_capacity_kWh, range_km, weight_kg, vehicle_type FROM ev_models WHERE model_name = %s"
        self.cursor.execute(query, (selected_model,))
        result = self.cursor.fetchone()
        if result:
            battery, range_km, weight, vtype = result
            self.ev_details_box.setText(
                f"EV Model: {selected_model}\n\n"
                f"Battery: {battery} kWh\n"
                f"Range: {range_km} km\n"
                f"Weight: {weight} kg\n"
                f"Type: {vtype}"
            )
        else:
            self.ev_details_box.setText("EV details not found.")
    
    def add_widgets(self):
        spacing = 10  # spacing between elements

    # 🔹 EV Section
        self.ev_label = QLabel("Select EV Model")
        self.ev_label.setFont(self.font)
        self.layout.addWidget(self.ev_label)
        self.layout.addSpacing(spacing)

        self.ev_dropdown = QComboBox()
        self.layout.addWidget(self.ev_dropdown)
        self.layout.addSpacing(spacing)

        self.fetch_button = QPushButton("Select EV")
        self.fetch_button.setStyleSheet("padding: 6px; font-weight: bold;")
        self.fetch_button.clicked.connect(self.fetch_ev_details)
        self.layout.addWidget(self.fetch_button)
        self.layout.addSpacing(spacing)
    
    # EV Specs Output Box (blank1)
        self.ev_details_box = QTextEdit()
        self.ev_details_box.setReadOnly(True)
        self.ev_details_box.setFixedHeight(130)
        self.ev_details_box.setStyleSheet("QTextEdit { background-color: #000000; color: #ffffff; padding: 6px; font: 12pt 'Courier New'; }")
        self.ev_details_box.setPlaceholderText("EV specifications will appear here...")
        self.layout.addWidget(self.ev_details_box)
        self.layout.addSpacing(spacing * 2)

    # 🔹 Trip Input Section
        self.source_label = QLabel("Source")
        self.source_label.setFont(self.font)
        self.source_input = QLineEdit()
        self.layout.addWidget(self.source_label)
        self.layout.addWidget(self.source_input)
        self.layout.addSpacing(spacing)

        self.dest_label = QLabel("Destination")
        self.dest_label.setFont(self.font)
        self.dest_input = QLineEdit()
        self.layout.addWidget(self.dest_label)
        self.layout.addWidget(self.dest_input)
        self.layout.addSpacing(spacing)

        self.battery_label = QLabel("Current Battery %")
        self.battery_label.setFont(self.font)
        self.battery_input = QLineEdit()
        self.layout.addWidget(self.battery_label)
        self.layout.addWidget(self.battery_input)
        self.layout.addSpacing(spacing)

        self.plan_button = QPushButton("Plan Trip")
        self.plan_button.setStyleSheet("padding: 6px; font-weight: bold; background-color: #4CAF50; color: white;")
        self.plan_button.clicked.connect(self.plan_trip)
        self.layout.addWidget(self.plan_button)
        self.layout.addSpacing(spacing)

    # Trip Result Output Box (blank2)
        self.trip_result_box = QTextEdit()
        self.trip_result_box.setReadOnly(True)
        self.trip_result_box.setFixedHeight(200)
        self.trip_result_box.setStyleSheet("QTextEdit { background-color: #000000; color: #ffffff; padding: 6px; font: 12pt 'Courier New'; }")
        self.trip_result_box.setPlaceholderText("Trip analysis will appear here...")
        self.layout.addWidget(self.trip_result_box)




    def plan_trip(self):
        from route_fetcher.fetch_route import get_route_distance_time
        from ml_model.predict_battery import predict_battery_usage

        selected_model = self.ev_dropdown.currentText()
        source = self.source_input.text().strip()
        dest = self.dest_input.text().strip()
        battery_str = self.battery_input.text().strip()

        if not source or not dest or not battery_str:
            self.trip_result_box.setText("⚠️ Please enter all required fields.")
            return

        try:
            battery_percent = float(battery_str)
        except ValueError:
            self.trip_result_box.setText("⚠️ Battery % must be a number.")
            return

        if battery_percent <= 0 or battery_percent > 100:
            self.trip_result_box.setText("⚠️ Enter battery % between 1 and 100.")
            return

        # Get GPS distance & duration
        API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjIyNzQ5MGJiMjY4MTQ1YjU4OGNiZDVjNTZkMDFkNTBjIiwiaCI6Im11cm11cjY0In0="
        distance_km, duration_min = get_route_distance_time(source, dest, API_KEY)

        if distance_km is None:
            self.trip_result_box.setText("Invalid source or destination. Please check spelling.")
            return

        # Get EV weight
        self.cursor.execute("SELECT weight_kg FROM ev_models WHERE model_name = %s", (selected_model,))
        result = self.cursor.fetchone()
        if not result:
            self.trip_result_box.setText("EV model not found.")
            return

        ev_weight = result[0]

        # Predict battery usage
        elevation_gain = 400
        avg_speed = 60
        ac_on = 1
        predicted_usage = predict_battery_usage(distance_km, elevation_gain, ev_weight, avg_speed, ac_on)

        # Smart decision logic
        if predicted_usage <= 100:
            if battery_percent >= predicted_usage:
                status = (
                    f"Trip possible!\n"
                    f"Estimated battery usage: {predicted_usage}%"
                )
            else:
                status = (
                    f"Trip not possible with current charge.\n"
                    f"You need at least {predicted_usage}% battery."
                )
        else:
            status = (
                f"This trip is too long for this EV’s full battery range.\n"
                f"Even 100% battery won't be enough."
            )

        # Display result
        self.trip_result_box.setText(
            
            f"EV Model: {selected_model}\n"
            f"From: {source} → To: {dest}\n"
            f"Distance: {distance_km:.2f} km\n"
            f"Duration: {duration_min:.1f} mins\n\n"
            f"Battery Available: {battery_percent}%\n"
            f"{status}"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EVTripPlanner()
    window.show()
    sys.exit(app.exec())
