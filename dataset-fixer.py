import pandas as pd

NAME = '23-2021_04_07_Coperchi_merged'

df = pd.read_csv(f'./inf-dataset-merge/{NAME}.csv')

# Convert columns to datetime
df[' Start_Time'] = pd.to_datetime(df[' Start_Time'], format='%d-%m-%Y %H:%M:%S')
df[' End_Time'] = pd.to_datetime(df[' End_Time'], format='%d-%m-%Y %H:%M:%S')

# Calculate elapsed time
df['Elapsed_Time'] = (df[' End_Time'] - df[' Start_Time']).dt.components['seconds']#total_seconds()

df = df.drop(columns=[' Start_Time', ' End_Time'])

# Assuming you have a DataFrame named 'df'
df_normalized = (df - df.min()) / (df.max() - df.min())

df_normalized.to_csv(f'./inf-dataset-merge-fixed/{NAME}.csv', index=False)