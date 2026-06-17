# TikTok Engagement Pulse — Discovery-to-Action Strategy Analysis

## 📌 Discovery Phase Overview
This project applies the Discovery-to-Action (DTA) framework to raw, irregularly-sampled TikTok view count streams. By applying datetime indexing and daily (`'D'`) mean resampling, we established a balanced, sequential timeline free from empty timestamp gaps. 

A classical additive `seasonal_decompose` was implemented to strip away random variations, separating the structural timeline components into **Trend**, **Seasonality**, and **Residuals**.

---

## 🔬 Technical Phase: Stationarity Hypothesis Summary
To ensure mathematical compliance for future forecasting networks, we tested the daily view count series using the **Augmented Dickey-Fuller (ADF) Test**:

* **Null Hypothesis ($H_0$):** The timeline data contains a unit root (it is non-stationary and exhibits structural drift).
* **Alternative Hypothesis ($H_a$):** The series is stationary (its mean, variance, and autocovariance remain constant over time).

### Statistical Output Analysis:
* **ADF Test Statistic:** `-1.1402`
* **Computed $p$-value:** `6.987e-01` ($> 0.05$)
* **Critical Value Threshold (5%):** `-2.884`

### Strategic Conclusion:
Because our $p$-value is well above the significance alpha of `0.05`, we **fail to reject the null hypothesis ($H_0$)**. The raw timeline is **non-stationary** due to a clear upward growth trend. 
* **Next Preprocessing Steps:** A first-order differencing pass ($\Delta Y_t = Y_t - Y_{t-1}$) must be applied to stabilize the mean variance before launching formal mathematical prediction engines.

---

## 🚀 Action Phase: Content Optimization & Strategic Recommendations

### 📅 1. Optimal Content Posting Schedule
Analysis of the isolated **Seasonal Component** reveals a distinct 7-day recurring loop:
* **Peak Performance Window:** Thursdays and Fridays show the highest positive seasonal velocity variations, indicating strong audience activity.
* **Operational Action:** Schedule high-priority brand campaigns and organic video uploads for **Thursday mornings** to capture maximum organic algorithm traffic.
* **Platform Maintenance Window:** Mondays and Tuesdays demonstrate negative seasonal weights. This represents the optimal window to push backend code patches or run routine maintenance with minimal channel disruption.

### 📈 2. Foundations for Advanced Predictive Modeling
This exploratory breakdown establishes the specific tuning numbers needed to build high-accuracy **ARIMA/SARIMA** statistical models:
* **The Autoregressive Term ($p$):** Configured by mapping autocorrelation thresholds.
* **The Integrated Term ($d$):** Set to `1` because our ADF test demonstrated that a single differencing step is required to achieve stationarity.
* **The Moving Average Term ($q$):** Determined from partial autocorrelation spikes to capture shock adjustments from random viral trends.
* **The Seasonal Grid ($P, D, Q)_s$:** Set to an explicit seasonal lag component of $s=7$ to capture the weekly recurring cycle.
