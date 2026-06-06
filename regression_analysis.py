import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# ==========================================
# TASK 1: LOAD AND CLEAN DATASET
# ==========================================
# Load the marketing dataset
df = pd.read_csv('85334965-5736-457a-b8d4-a077e6872f84 (2).csv')

print("--- Checking for Missing Values ---")
print(df.isnull().sum())

# Drop rows with missing values to ensure statistical clean inputs
df_clean = df.dropna()
print(f"\nData successfully cleaned. Rows remaining: {df_clean.shape[0]}")

# Show structural overview
print("\n--- Cleaned Dataset Sample ---")
print(df_clean.head())
