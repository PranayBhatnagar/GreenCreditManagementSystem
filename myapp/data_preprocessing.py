# data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(input_file, output_file):
    # Load the dataset
    data = pd.read_csv(input_file)

    # Drop unnecessary columns
    unnecessary_columns = ['Entity', 'Year', 'Latitude', 'Longitude']
    data.drop(columns=unnecessary_columns, inplace=True)

    # Handle missing values
    data.dropna(inplace=True)

    # Replace commas with periods in numerical columns and convert to float
    numerical_columns = [
        'Electricity from renewables (TWh)', 
        'Value_co2_emissions_kt_by_country', 
        'Renewables (% equivalent primary energy)', 
        'gdp_growth'
    ]

    for column in numerical_columns:
        # Check if the column contains string values before replacing commas
        if data[column].dtype == 'object':
            data[column] = data[column].str.replace(',', '.').astype(float)

    # Feature scaling
    scaler = StandardScaler()
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

    # Save the preprocessed data to a new CSV file
    data.to_csv(output_file, index=False)

    print("Data preprocessing completed.")

# Call the preprocess function
# preprocess_data("data.csv", 'preprocessed_data.csv')
