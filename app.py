import pandas as pd
import numpy as np
import joblib
from flask import Flask, request, jsonify, render_template

# Load the trained XGBoost model from the pickle file
try:
    model = joblib.load('xgb_best_model.pkl')
except FileNotFoundError:
    print("Error: The 'xgb_best_model.pkl' file was not found. Please ensure it is in the same directory.")
    model = None

# Create the Flask application instance
app = Flask(__name__)

# Define the list of features your model was trained on.
# We've added 'Charging_Mode_slow' to this list.
FEATURES = [
    'Solar_Power_kW', 'Solar_Irradiance_Wm2', 'Battery_SOC_%',
    'Num_EVs_Charging', 'Charging_Duration_Min', 'Arrival_Time_Hour',
    'Departure_Time_Hour', 'Initial_Battery_SOC_%', 'Final_Battery_SOC_%',
    'Grid_Energy_Supply_kW', 'Residential_Load_kW', 'Business_Load_kW',
    'Peak_Load_Time_Hour', 'Energy_Cost_$/kWh', 'Demand_Response',
    'Total_Demand_kW', 'Available_Energy_kW', 'Charging_Mode_slow'
]

# Create a route that serves the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Create the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model file not found. Please check your server logs."}), 500

    data = request.get_json(force=True)

    if not all(feature in data for feature in FEATURES):
        return jsonify({"error": "Missing one or more required features. Please ensure all fields are filled."}), 400

    input_data = pd.DataFrame([data])
    input_data = input_data[FEATURES]

    prediction = model.predict(input_data)[0]

    return jsonify({
        'forecasted_ev_charging_load_kWh': float(prediction)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)