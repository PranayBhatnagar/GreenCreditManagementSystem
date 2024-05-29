# app.py (Backend - Flask)
from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__, template_folder='templates')


# Load the pre-trained model
model = joblib.load('best_multivariate_model.joblib')

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    input_data = request.form.to_dict()
    
    # Perform predictions using the model
    # (You need to preprocess the input data similarly to how you preprocessed the training data)
    # For simplicity, let's assume X_input is a DataFrame with preprocessed input data
    
    
    # Prepare the response
    response = {
        'prediction': prediction.tolist()  # Convert NumPy array to list
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
