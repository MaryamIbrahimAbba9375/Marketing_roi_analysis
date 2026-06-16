
"""
Feature Engineering – NBA Player Longevity Prediction
Author: Maryam Ibrahim Abba
"""

import pandas as pd
import numpy as np

print("==========================================================")
print("👉 TASK 1: LOADING DATASET & ISOLATING TARGET VARIABLE")
print("==========================================================")
# Load the raw NBA player stats
df = pd.read_csv("ReadMe.csv")
print(f"Initial Dataset Shape: {df.shape}")

# Define the target variable explicitly
target_col = 'target_5yrs'
print(f"Target variable '{target_col}' distribution:")
print(df[target_col].value_counts(normalize=True))

print("\n==========================================================")
print("👉 TASK 2: DROPPING NON-PREDICTIVE COLUMNS (NOISE REDUCTION)")
print("==========================================================")
# The 'name' column and un-named index columns add noise and cause data leakage
cols_to_drop = ['name']
# Drop un-named structural index columns if they exist
unnamed_cols = [col for col in df.columns if 'Unnamed' in col or col == '']
cols_to_drop.extend(unnamed_cols)

df_reduced = df.drop(columns=cols_to_drop, errors='ignore')
print(f"Dataset shape after dropping non-predictive columns: {df_reduced.shape}")

print("\n==========================================================")
print("👉 TASK 3: CORRELATION ANALYSIS (REDUNDANCY CHECK)")
print("==========================================================")
# Calculate the correlation matrix for numeric features
corr_matrix = df_reduced.corr().abs()

# Identify features that are highly correlated with each other (threshold > 0.90)
print("Highly correlated feature pairs (Correlation > 0.90):")
upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > 0.90) and column != target_col]

for col in to_drop:
    # Find what it's highly correlated with
    correlated_with = upper_tri.index[upper_tri[col] > 0.90].tolist()
    print(f" - '{col}' is highly correlated with {correlated_with}")

# Drop highly redundant features to combat multicollinearity
df_no_multicollinearity = df_reduced.drop(columns=to_drop)
print(f"Dataset shape after removing multicollinear variables: {df_no_multicollinearity.shape}")

print("\n==========================================================")
print("👉 TASK 4: CREATING NEW COMPOSITE FEATURES")
print("==========================================================")
# Engineer a derived metric: Points Per Minute (PPM) to track true scoring efficiency
# Adding a small epsilon (1e-5) to prevent division-by-zero errors
df_no_multicollinearity['points_per_minute'] = df_no_multicollinearity['pts'] / (df_no_multicollinearity['min'] + 1e-5)

# Engineer a second derived metric: True Shooting Attempts Estimate or Total Rebounds Per Game
if 'oreb' in df_no_multicollinearity.columns and 'dreb' in df_no_multicollinearity.columns:
    df_no_multicollinearity['total_rebounds'] = df_no_multicollinearity['oreb'] + df_no_multicollinearity['dreb']

print("Successfully engineered composite features: ['points_per_minute']")
print(df_no_multicollinearity[['pts', 'min', 'points_per_minute']].head())

print("\n==========================================================")
print("👉 TASK 5: HANDLING MISSING VALUES (ML-READINESS)")
print("==========================================================")
# Check for null values across features
null_counts = df_no_multicollinearity.isnull().sum()
print("Null counts per column before cleaning:")
print(null_counts[null_counts > 0])

# Safely impute or drop missing values (since it's a minor fraction of the data, median imputation prevents leakage)
for col in df_no_multicollinearity.columns:
    if df_no_multicollinearity[col].isnull().sum() > 0:
        median_val = df_no_multicollinearity[col].median()
        df_no_multicollinearity[col] = df_no_multicollinearity[col].fillna(median_val)

print("\nFinal clean dataset check: Any missing values remaining? ", df_no_multicollinearity.isnull().values.any())
print(f"Final Model-Ready Dataset Shape: {df_no_multicollinearity.shape}")

# Export clean engineered dataset to CSV format for reproducibility
df_no_multicollinearity.to_csv("clean_nba_feature_engineered.csv", index=False)
print("✅ Saved 'clean_nba_feature_engineered.csv' successfully.")
