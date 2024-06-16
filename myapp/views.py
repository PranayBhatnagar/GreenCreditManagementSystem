# myapp/views.py

from django.shortcuts import render
from django.http import JsonResponse
import joblib
import pandas as pd
from .forms import PredictionForm
from .models import PredictionInput
from .data_preprocessing import preprocess_data

model = joblib.load('../best_multivariate_model.joblib')

def index(request):
    form = PredictionForm()
    return render(request, 'index.html', {'form': form})
    
# Assuming 'data' is your preprocessed DataFrame excluding non-numeric columns
data = pd.read_csv('C:\\Users\\Dell\\myproject\\myapp\\data\\preprocessed_data.csv')
X_test = data.drop(columns=['Entity', 'Year', 'Latitude', 'Longitude'])  # Features for prediction

def predict(request):
    if request.method == 'POST':
        try:
            # Parse input data received from the client-side form
            data = request.POST.dict()
            
            # Define the list of features expected by the model
            expected_features = [
            'Electricity_from_renewables', 
            'Value_co2_emissions_kt_by_country', 
            'renewables_percentage',
            'gdp_growth'
        ]

            
            # Check if all expected features are present in the input data
            missing_features = [feature for feature in expected_features if feature not in data]
            if missing_features:
                error_message = f"The following features are missing in the input data: {', '.join(missing_features)}"
                return JsonResponse({"error": error_message}, status=400)  # HTTP status code 400 for bad request
            
            # Prepare the data for input to your model
            input_data = pd.DataFrame([data], columns=expected_features)
            input_data.fillna(0, inplace=True)  # Replace NaN values with 0
            
            # Ensure columns are in the correct order and matching model's expectations
            input_data = input_data[X_test.columns]  # Assuming X_test has the correct columns
            
            # Perform prediction using the loaded model
            prediction = model.predict(input_data)
            
            # Format the prediction as a dictionary
            prediction_result = {
                "Electricity_from_renewables": prediction[0][0],
                "Value_co2_emissions_kt_by_country": prediction[0][1],
                "renewables_percentage": prediction[0][2],
                "gdp_growth": prediction[0][3]
                # Add other predictions as needed
            }
            print(prediction_result)
            
            # Return the prediction as JSON response
            return JsonResponse(prediction_result)
        
        except Exception as e:
            # If an error occurs, return an error message as JSON response
            return JsonResponse({"error": str(e)}, status=500)  # HTTP status code 500 for internal server error
    
    return JsonResponse({"error": "Invalid request method"}, status=400)
