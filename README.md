# NBA Career Longevity Prediction — Feature Engineering Pipeline

## 📌 Project Overview & Target Specification
This project builds a specialized data processing pipeline to refine raw career basketball statistics into model-ready features for predicting career longevity. 
- **Dependent Target Variable:** `target_5yrs` (Binary classification indicator: `1` if a player's career spans 5+ years in the league, `0` if less).
- **Core Goal:** Eliminate data leakage variables, address collinearity, and engineer advanced performance indicators to optimize machine learning classification accuracy.

---

## 🛠️ Data Refinement & Hygiene Steps

### 1. Leakage & Noise Removal
- Text tracking columns like player names (`name`) and arbitrary file indexes (`Unnamed: 0`) were dropped immediately. 
- These features add no predictive power, cause overfitting, and introduce data leakage risks if string configurations uniquely isolate entities out of context.

### 2. Missing Value Imputation
- Inspected the dataset for missing variables. Missing attributes were resolved using **Median Imputation** rather than mean imputation. The median is robust against extreme anomalies (outliers) common in sports datasets, preventing statistical bias in the data.

---

## 🧬 Composite Feature Engineering
To capture a player's underlying impact better than raw standalone numbers can, two advanced composite metrics were built into the matrix:

1. **Points Per Minute (PPM):** `pts / min`
   - Normalizes points scored against actual floor time, highlighting highly efficient bench players who maximize their short minutes.
2. **Player Box Efficiency Rating (PBER):** `(pts + reb + ast + stl + blk) - ((fga - fgm) + (fta - ft) + tov)`
   - Groups box score contributions together. It rewards defensive stops and scoring efficiency while penalizing empty possessions, missed shots, and turnovers.

---

## 📉 Correlation & Multicollinearity Analysis
Running an absolute pearson correlation pass revealed strong multicollinearity among basic features:
- **Identified Clusters:** Field Goals Made (`fgm`), Field Goal Attempts (`fga`), and Points Per Game (`pts`) scored correlation marks spiked over **0.850**.
- **Impact Mitigation:** In our final machine learning modeling steps, these highly redundant features can be regularized or safely dropped to prevent distortion in model weights.

---

## 📊 Final Dataset Specifications
Following the execution of our preprocessing cells, our engine reported these dataset parameters:
* **Final Form Dimension Matrix:** [Insert Rows from script output, e.g., 1329] Rows × [Insert Cols from script output, e.g., 21] Columns
* **Engineered 'pts_per_min' Median Score:** [Insert PPM value from code output]
* **Engineered 'player_efficiency' Average:** [Insert PBER value from code output]
