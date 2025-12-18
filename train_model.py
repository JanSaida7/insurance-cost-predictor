import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import joblib

# 1. Load Data
df = pd.read_csv('insurance.csv')

# 2. Preprocessing
# Label Encoding
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})

# One-Hot Encoding for Region
# We use get_dummies but we need to ensure we know the column order for the Django app
# To make it robust for this simple project, we will manually encode or stick to a specific order
# Regions: southwest, southeast, northwest, northeast
# Let's use get_dummies and print the columns to ensure we match in Django
df = pd.get_dummies(df, columns=['region'], drop_first=True)

print("Features after encoding:")
print(df.columns.tolist())

# Features and Target
X = df.drop('charges', axis=1)
y = df['charges']

# 3. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluation
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Model Performance:")
print(f"R^2 Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# 6. Save Model
joblib.dump(model, 'model_linear_reg.pkl')
print("Model saved to model_linear_reg.pkl")

# Save the columns to a file so we know the order for Django
import json
with open('model_columns.json', 'w') as f:
    json.dump(X.columns.tolist(), f)
print("Model columns saved to model_columns.json")
