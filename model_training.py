import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the data
data = pd.read_csv('preprocessed_data.csv')

# Convert columns to numeric, handling commas
numeric_columns = data.select_dtypes(include=['object']).columns
data[numeric_columns] = data[numeric_columns].replace({',': ''}, regex=True)
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Define features and target variables
X = data.drop(columns=['Entity', 'Year', 'Latitude', 'Longitude'])  # Features (excluding non-numeric columns)
y = data[['Electricity from renewables (TWh)', 'Value_co2_emissions_kt_by_country', 'Renewables (% equivalent primary energy)', 'gdp_growth']]  # Target variables

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train multiple models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(),
    'Random Forest': RandomForestRegressor()
}

best_model = None
best_score = float('inf')  # Initialize with a high value for MSE (we want to minimize MSE)

for name, model in models.items():
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions on the testing set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model: {name}")
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")
    print("------------------------")
    
    # Update the best model if current model performs better
    if mse < best_score:
        best_model = model
        best_score = mse

# Save the best model
joblib.dump(best_model, 'best_multivariate_model.joblib')
