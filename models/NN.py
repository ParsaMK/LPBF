import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('../ultimate_dataset/dataset_normalized.csv')

# Identify numeric and categorical columns
numeric_cols = df.select_dtypes(include=['float64', 'int']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

# Include the layer number in numeric_cols if it's numeric
numeric_cols = numeric_cols.tolist()  # Keep numeric columns

# Split the dataset into features (X) and target (y)
X = df.drop(columns=['Area', 'unique_id', ' Start_Time', ' End_Time'])
y = df['Area']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.columns)

# Scale only the numeric features excluding the layer number
scaler = MinMaxScaler()
X_train_scaled = X_train[numeric_cols].copy()
X_test_scaled = X_test[numeric_cols].copy()

# Scale numeric features but exclude layer number
X_train_scaled[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
X_test_scaled[numeric_cols] = scaler.transform(X_test[numeric_cols])

# Combine scaled numeric features with the layer number
X_train_final = pd.concat([X_train_scaled, X_train[[layer_col]].reset_index(drop=True)], axis=1)
X_test_final = pd.concat([X_test_scaled, X_test[[layer_col]].reset_index(drop=True)], axis=1)

# Convert categorical features to dummy variables if needed (not shown here since no categorical features)
# Handle any categorical features as needed, similar to previous examples

# Create the neural network model
model = MLPRegressor(hidden_layer_sizes=(50, 50),  # Two hidden layers with 50 neurons each
                     activation='relu',           # Activation function
                     solver='adam',               # Optimizer
                     max_iter=1000,               # Number of iterations
                     random_state=42)

# Fit the model
model.fit(X_train_final, y_train)

# Predict on the test set
predictions = model.predict(X_test_final)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f'Mean Squared Error: {mse}')
print(f'R² Score: {r2}')
