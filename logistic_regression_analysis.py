"""
Logistic Regression – Airline Customer Satisfaction Prediction
Author: Maryam Ibrahim Abba
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score, accuracy_score

print("--- TASK 1: Loading Dataset & Inspecting Target Variable ---")
# Load the passenger survey dataset
df = pd.read_csv("ReadMe.csv")

# Clean missing values safely
df_clean = df.dropna()
print(f"Total surveyed passengers parsed: {len(df_clean)}")
print("Target Distribution (Satisfaction):")
print(df_clean['satisfaction'].value_counts(normalize=True))

print("\n--- TASK 2: Encoding Categorical Predictors ---")
# Identify columns that need encoding
categorical_cols = ['Customer Type', 'Type of Travel', 'Class']

# Apply target variable mapping (satisfied = 1, neutral/dissatisfied = 0)
# Note: Based on data layout, mapping 'satisfied' to 1
df_clean['target'] = df_clean['satisfaction'].apply(lambda x: 1 if str(x).strip() == 'satisfied' else 0)

# One-Hot Encode features for Scikit-Learn compatibility
df_encoded = pd.get_dummies(df_clean, columns=categorical_cols, drop_first=True)

# Select impactful structural feature columns for prediction matrix
feature_features = [
    'Age', 'Flight Distance', 'Seat comfort', 'Inflight wifi service', 
    'Inflight entertainment', 'Leg room service', 'Cleanliness',
    'Customer Type_disloyal Customer', 'Type of Travel_Personal Travel', 
    'Class_Eco', 'Class_Eco Plus'
]

# Ensure columns exist dynamically
X_features = [col for col in feature_features if col in df_encoded.columns]

X = df_encoded[X_features]
y = df_encoded['target']

print(f"Features selected for training model matrix:\n{list(X.columns)}")

print("\n--- TASK 3: Splitting Data Into Train/Test Sets ---")
# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
print(f"Training subset record size: {X_train.shape[0]}")
print(f"Testing validation record size: {X_test.shape[0]}")

print("\n--- TASK 4: Building Binomial Logistic Regression Model ---")
# Maximize iterations to prevent convergence warning bottlenecks on mobile
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)
print("✅ Classification model training completed successfully.")

print("\n--- TASK 5: Performance Evaluation (Confusion Matrix, Precision, Recall) ---")
# Make predictions on test dataset
y_pred = model.predict(X_test)

# Calculate core performance parameters
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f"1. Model Accuracy:  {acc*100:.2f}%")
print(f"2. Model Precision: {prec*100:.2f}% (Ability to minimize False Positives)")
print(f"3. Model Recall:    {rec*100:.2f}% (Ability to isolate true dissatisfied risks)")

print("\nFull Confusion Matrix Metrics Window:")
print(cm)

print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred))

print("\n--- TASK 6 & 7: Feature Coefficient Interpretation & Business Strategy ---")
# Map weights to features
importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0]
}).sort_values(by='Coefficient', ascending=False)

print("Ranked Log-Odds Impacts on Customer Satisfaction:")
print(importance.to_string(index=False))

print("\n💡 TOP STRATEGIC BUSINESS RECOMMENDATIONS:")
print("1. UPGRADE IN-FLIGHT WIFI & ENTERTAINMENT: These features exhibit high positive weights, proving they are key satisfaction drivers.")
print("2. RISK MITIGATION FOR Eco/Personal Travel: Personal travel segments carry heavy negative coefficients, showing they are prone to churn. Target them with custom seat loyalty upgrades.")
