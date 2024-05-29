import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('data.csv')

# Drop unnecessary columns (if needed)
# For example, if 'Financial flows to developing countries (US $)' is not relevant to your project
data.drop(columns=['Financial flows to developing countries (US $)'], inplace=True)

# Handle missing values (if needed)
# For example, if there are missing values in any column, you can drop or impute them
data.dropna(inplace=True)

# Replace commas with periods in numerical columns
numerical_columns = ['Access to electricity (% of population)', 'Access to clean fuels for cooking', 'Renewable-electricity-generating-capacity-per-capita', 'Renewable energy share in the total final energy consumption (%)', 'Electricity from fossil fuels (TWh)', 'Electricity from nuclear (TWh)', 'Electricity from renewables (TWh)', 'Low-carbon electricity (% electricity)', 'Primary energy consumption per capita (kWh/person)', 'Energy intensity level of primary energy (MJ/$2017 PPP GDP)', 'Value_co2_emissions_kt_by_country', 'Renewables (% equivalent primary energy)', 'gdp_growth', 'gdp_per_capita', 'Land Area(Km2)', 'Latitude', 'Longitude']

for column in numerical_columns:
    # Check if the column contains string values before replacing commas
    if data[column].dtype == 'object':
        data[column] = data[column].str.replace(',', '.').astype(float)

# Feature scaling (if needed)
# For example, if you want to scale numerical features to a similar range
scaler = StandardScaler()
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# Encode categorical variables (if applicable)
# For example, if 'Entity' column contains country names, you can use one-hot encoding or label encoding

# Feature engineering (if needed)
# For example, calculate the total electricity consumption by summing fossil fuels, nuclear, and renewables

# Save the preprocessed data to a new CSV file
data.to_csv('preprocessed_data.csv', index=False)

print("Data preprocessing completed.")
