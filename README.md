# Advanced Predictive Modeling for Airline Satisfaction – XGBoost Deployment

## 📋 Project Overview
This project delivers an end-to-end predictive solution utilizing an optimized XGBoost Classifier to forecast airline passenger satisfaction. Using the Discovery-to-Action (DTA) framework, we translate technical metrics into strategic operational levers for executive leadership.

---

## 🛠️ Discovery-to-Action Framework Summary

### 1. Discovery Phase
* **Data Prep:** Cleaned missing operational data, handled delay metrics, and converted categorical attributes (e.g., Class, Travel Type) using One-Hot Encoding to ensure full compatibility with the gradient boosting algorithm.

### 2. Technical Phase (Model Comparison)
We optimized the XGBoost algorithm using `GridSearchCV` (tuning `max_depth` and `learning_rate`) and evaluated it against previous baseline iterations:

| Model Hierarchy | Accuracy | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- |
| **Decision Tree** (Baseline) | 0.892 | 0.885 | 0.871 | 0.878 |
| **Random Forest** (Ensemble) | 0.945 | 0.952 | 0.921 | 0.936 |
| **XGBoost** (Optimized) | **0.963** | **0.965** | **0.949** | **0.957** |

*Note: XGBoost outperformed prior models across all core metrics, specifically maximizing **Recall (0.949)**, which reduces critical False Negatives (dissatisfied customers flagged as satisfied).*

### 3. Action Phase & Executive Summary
* **Top Satisfaction Drivers:** The model's feature importance highlights **Inflight Wi-Fi Service**, **Online Boarding**, and **Seat Comfort** as the highest-impact drivers of positive sentiment.
* **Strategic Recommendations:** 1. Upgrade regional fleet Wi-Fi bandwidth to mitigate the primary digital friction point.
  2. Streamline the mobile check-in and online boarding user interfaces to secure early-journey satisfaction.
* **Deployment & Monitoring:** The final model artifact is structured for containerized deployment via FastAPI. We recommend setting up quarterly retraining loops alongside tools like Evidently AI to proactively monitor data drift.
