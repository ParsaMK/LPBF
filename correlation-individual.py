import pandas as pd

# Specify the file you want to save the output to
NAME = '23-2021_04_07_Coperchi_merged'
output_file = f'./individual-correlation/{NAME}.txt'

merged_df = pd.read_csv(f'./inf-dataset-merge-fixed-normalized/{NAME}.csv')

non_numeric_columns = merged_df.select_dtypes(exclude=['number']).columns

# Drop non-numeric columns if you don't need them
merged_df.drop(non_numeric_columns, axis=1, inplace=True)

# Assuming merged_df is your DataFrame
# Calculate the correlation matrix
correlation_matrix = merged_df.corr()

# Get the correlation values for the 'Area' column
area_correlation = correlation_matrix['Area'].drop('Area')  # Drop self-correlation

# Display columns with their correlation to the Area column
print("Here are the columns and their correlation to the 'Area' column:")
print(area_correlation.sort_values(ascending=False))
print('************************************************************')

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Prepare your data
X = merged_df.drop('Area', axis=1)  # Features
y = merged_df['Area']  # Target variable

# Optionally, convert categorical variables to dummy variables if any
X = pd.get_dummies(X, drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestRegressor(random_state=42)

# Fit the model
model.fit(X_train, y_train)

# Get feature importances
importances = model.feature_importances_

# Create a DataFrame to hold feature names and their importance scores
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': importances})

# Sort the DataFrame by importance
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

# Display the features and their importance scores
print("Here are the features and their importance scores:")
print(feature_importance)
print('************************************************************')

# Open the file in write mode
with open(output_file, 'w') as file:
    # Write the first part (correlation to Area)
    file.write("Here are the columns and their correlation to the 'Area' column:\n")
    file.write(area_correlation.sort_values(ascending=False).to_string() + '\n')
    file.write('************************************************************\n')
    
    # Write the feature importance section
    file.write("Here are the features and their importance scores:\n")
    file.write(feature_importance.to_string() + '\n')
    file.write('************************************************************\n')

