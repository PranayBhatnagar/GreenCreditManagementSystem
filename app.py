# app.py (Backend - Flask)
from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__, template_folder='templates')

# Load the pre-trained model
model = joblib.load('best_multivariate_model.joblib')

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input data received from the client-side form
        data = request.json
        # print(data)
        
      # Define the list of features expected by the model during prediction
        expected_features = [
        'Electricity from renewables (TWh)',
        'Energy intensity level of primary energy (MJ/$2017 PPP GDP)',
        'Land Area(Km2)',
        'Low-carbon electricity (% electricity)',
        'Primary energy consumption per capita (kWh/person)'
    ]

        
        # Check if all expected features are present in the input data
        missing_features = [feature for feature in expected_features if feature not in data]
        if missing_features:
            error_message = f"The following features are missing in the input data: {', '.join(missing_features)}"
            return jsonify({"error": error_message}), 400  # HTTP status code 400 for bad request
        
        # Prepare the data for input to your model
        # For example, convert data to a DataFrame and perform any necessary preprocessing
        # Assuming 'data' is a dictionary received from a POST request
        input_data = pd.DataFrame(data.values(), index=data.keys()).T

        input_data.fillna(0, inplace=True)  # Replace NaN values with 0
        
        # Perform prediction using the loaded model
        prediction = model.predict(input_data)
        print(input_data)
        # Format the prediction as a dictionary
        prediction_result = {
            "Electricity from renewables (TWh)": prediction[0],
            "Value_co2_emissions_kt_by_country": prediction[1],
            "Renewables (% equivalent primary energy)": prediction[2],
            "gdp_growth": prediction[3]
        }
        
        # Return the prediction as JSON response
        return jsonify(prediction_result)
    except Exception as e:
        # If an error occurs, return an error message as JSON response
        return jsonify({"error": str(e)}), 500  # HTTP status code 500 for internal server error

if __name__ == '__main__':
    app.run(debug=True)
