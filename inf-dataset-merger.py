import pandas as pd
from sklearn.preprocessing import MinMaxScaler

FILE_NAME = '23-2021_04_07_Coperchi'

# Load the two CSV files into DataFrames
df1 = pd.read_csv(f'./datasets/{FILE_NAME}/{FILE_NAME}.csv')
df2 = pd.read_csv(f'./Inferences/{FILE_NAME}_inference.csv')

df1['LayerID'] = df1['LayerID'].astype(str)
df2['LayerID'] = df2['LayerID'].astype(str)

# Merge the DataFrames on the 'LayerID' column (this performs an inner join by default)
merged_df = pd.merge(df1, df2, on='LayerID')

# # Specify the column you want to normalize
# column_to_normalize = 'Area'

# # Initialize the scaler
# scaler = MinMaxScaler()

# # Perform min-max normalization on the specified column
# merged_df[column_to_normalize] = scaler.fit_transform(merged_df[[column_to_normalize]])

merged_df.to_csv(f'./inf-dataset-merge/{FILE_NAME}_merged.csv', index=False)

# Print the normalized DataFrame
# print(merged_df)