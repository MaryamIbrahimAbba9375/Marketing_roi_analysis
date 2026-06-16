# Feature Engineering – NBA Player Longevity Preprocessing Pipeline

## 📌 Project Goals
This project implements an automated data preprocessing and feature engineering sequence using Python and `pandas`. The data environment transforms rookie performance data to optimize predictive signals tracking whether player durability spans 5+ professional years (`target_5yrs`).

## 📊 Exploration and Rationale Metrics

### 1. Target Imbalance Analysis
* **Observation:** The `target_5yrs` flag reflects a clear split (~62% positive outcomes vs ~38% negative outcomes). While there is minor imbalance, it remains safe for standard binary classification algorithms without needing synthetic resampling techniques.

### 2. Resolving Multicollinearity
* **Observation:** Running a `.corr()` matrix reveals intense linear overlap between metrics such as Games Played (`gp`) and Minutes Played (`min`). Redundant columns are safely isolated and filtered out to prevent standard model coefficients from blowing up.

### 3. Derived Composite Extraction
* **Feature Created:** Points Per Minute (PPM) $\rightarrow$ `pts / min`.
* **Rationale:** Normalizes scoring production directly against an individual's floor presence, allowing the evaluation engine to weigh player efficiency regardless of raw court time distributions.

### 4. Null Processing
* **Method:** Missing fields (such as missing shooting ratios) are programmatically handled using median imputation to keep data records intact without injecting mathematical bias.

## 🚀 Execution Guide
Run the complete pipeline:
```bash
python nba_feature_engineering.py
