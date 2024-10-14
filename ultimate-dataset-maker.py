import os
import pandas as pd
import uuid
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Function to generate a unique ID for each row
def generate_unique_id():
    return str(uuid.uuid4())  # Generates a unique ID

# Folder where your CSV files are stored
folder_path = './inf-dataset-merge'  # Replace with your folder path

# List to hold DataFrames
df_list = []

# Iterate over all CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Load the CSV file
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        
        # Generate unique IDs for each row and set as index
        df['unique_id'] = [generate_unique_id() for _ in range(len(df))]
        df.set_index('unique_id', inplace=True)  # Set the unique ID as index
        
        # Append DataFrame to the list
        df_list.append(df)

# Concatenate all DataFrames in the list into one DataFrame
combined_df = pd.concat(df_list)

# Save the combined DataFrame to a new CSV file
output_file = 'dataset'
combined_df.to_csv(f'./ultimate_dataset/{output_file}.csv')

print(f'Combined CSV saved as {output_file}')


df_normalized = combined_df.copy()
# Normalization (Min-Max Scaling)
scaler_minmax = MinMaxScaler()
df_normalized['Area'] = scaler_minmax.fit_transform(df_normalized[['Area']])
df_normalized.to_csv(f'./ultimate_dataset/{output_file}_normalized.csv')


df_standardized = combined_df.copy()
# Standardization (Z-Score Scaling)
scaler_standard = StandardScaler()
df_standardized['Area'] = scaler_standard.fit_transform(df_standardized[['Area']])

df_standardized.to_csv(f'./ultimate_dataset/{output_file}_standardized.csv')