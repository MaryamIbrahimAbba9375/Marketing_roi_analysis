# Random Forest Classification — Airline Customer Satisfaction Analysis

## 📌 Project Architecture & Leakage Mitigation
To guarantee robust generalization and completely prevent data leakage during hyperparameter optimization, a rigorous **Three-Way Data Split** strategy was used:
- **Training Set (60%):** Used exclusively to fit the tree structures.
- **Validation Set (20%):** Paired with scikit-learn's `PredefinedSplit` inside `GridSearchCV` to evaluate hyperparameter choices.
- **Testing Set (20%):** Kept completely isolated until final evaluation to act as an unbiased measure of real-world performance.

---

## ⚙️ Hyperparameter Tuning Results
Using `GridSearchCV` and a `PredefinedSplit`, the model automatically identified the following optimal parameter configuration:
- **`n_estimators`**: `100` *(Combines 100 base learners to smooth variance errors)*
- **`max_depth`**: `15` *(Limits complexity to avoid memorizing training set noise)*
- **`min_samples_leaf`**: `2` *(Ensures leaves capture stable passenger clusters)*

---

## 📊 Side-by-Side Model Comparison Table

| Performance Evaluation Metric | Single Decision Tree Baseline | Optimized Random Forest Model | Performance Delta (Gain) |
| :--- | :---: | :---: | :---: |
| **Test Set Accuracy** | 92.22% | **94.84%** | **+2.62%** |
| **Precision (Positive)** | 92.38% | **95.77%** | **+3.39%** |
| **Recall (Positive)** | 93.30% | **94.76%** | **+1.46%** |
| **F1-Score (Balanced)** | 92.84% | **95.15%** | **+2.31%** |

---

## 🎯 Top Operational Customer Satisfaction Drivers
The ensemble model ranks the following structural service touchpoints as the primary drivers of customer satisfaction:
1. **Inflight entertainment** (Highest Importance Weight: ~25.3%)
2. **Seat comfort** (~15.5%)
3. **Ease of Online booking** (~7.6%)
4. **Online support** (~7.1%)
5. **Food and drink** (~4.4%)

---

## 👔 Airline Leadership Executive Briefing

### 1. The Power of Ensemble Modeling vs. Single Trees
Single Decision Trees are highly prone to **overfitting**—they tend to build deep, hyper-specific logical rules that perfectly memorize training data but fail on new passengers. 

The **Random Forest** model solves this problem through an ensemble method called **Bagging (Bootstrap Aggregating)**. It trains multiple independent trees on random subsets of data and features, then averages their predictions. This averaging cancels out individual errors, reduces model variance, and makes the system much more stable and reliable for real-world operations.

### 2. Actionable Business Recommendations
To drive maximum returns on service improvements, leadership should prioritize capital allocation around the top drivers identified by the model:
- **Upgrade In-Flight Assets:** Over 40% of passenger satisfaction is driven by the combined quality of **Inflight Entertainment** and **Seat Comfort**. Upgrading screens and seat ergonomics will yield the highest drop in negative customer reviews.
- **Streamline Digital Workflows:** Digital interactions like **Online Booking** and **Online Support** outrank on-board physical services in driving positive sentiment. Investing in mobile application stability will directly convert casual passengers into loyal customers.
