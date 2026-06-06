
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import scipy.stats as stats

# Load and clean the marketing dataset
file_names = ['marketing_and_sales_data_evaluate_lr.csv', '85334965-5736-457a-b8d4-a077e6872f84 (2).csv']
df = None

for name in file_names:
    if os.path.exists(name):
        df = pd.read_csv(name)
        break
if df is None:
    df = pd.read_csv(file_names[0])

df_clean = df.dropna()

# Build the OLS Regression Model
X = df_clean['TV']
y = df_clean['Sales']
X_constant = sm.add_constant(X)
model = sm.OLS(y, X_constant).fit()

# Create and save diagnostic plots
fitted_values = model.predict(X_constant)
residuals = model.resid

plt.figure(figsize=(6, 4))
sns.scatterplot(x=df_clean['TV'], y=df_clean['Sales'], alpha=0.5, color='blue')
sns.lineplot(x=df_clean['TV'], y=fitted_values, color='red', linewidth=2)
plt.tight_layout()
plt.savefig('linearity_plot.png')
plt.close()

plt.figure(figsize=(6, 4))
stats.probplot(residuals, dist="norm", plot=plt)
plt.tight_layout()
plt.savefig('qq_plot.png')
plt.close()

plt.figure(figsize=(6, 4))
plt.scatter(fitted_values, residuals, alpha=0.5, color='purple')
plt.axhline(y=0, color='red', linestyle='--')
plt.tight_layout()
plt.savefig('homoscedasticity_plot.png')
plt.close()

print("Analysis successfully completed and all diagnostic plots saved!")
