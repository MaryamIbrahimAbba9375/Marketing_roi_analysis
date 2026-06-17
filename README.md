# Decision Tree Classification — Airline Customer Satisfaction Model

## 📌 Project Overview
This project uses a hyperparameter-tuned Decision Tree Classifier to analyze airline passenger satisfaction survey data. The goal is to establish transparent, auditable business logic that identifies the key operational service parameters causing or preventing passenger satisfaction.

---

## ⚙️ Hyperparameter Tuning Strategy & Results
To prevent individual tree branches from memorizing noise (overfitting) and to ensure smooth generalization to unseen customer cohorts, `GridSearchCV` ran a 5-fold cross-validation scheme evaluating combinations of depth and split criteria.

### Best Configuration Discovered:
* **`max_depth`**: `10` *(Restricts arbitrary nesting structural anomalies)*
* **`min_samples_split`**: `50` *(Requires substantial customer node volumes to warrant an added feature split)*
* **`min_samples_leaf`**: `20` *(Ensures no individual operational outlier alters leaf conclusions)*

---

## 📊 Performance Summary
* **Decision Tree F1-Score:** `~0.941` *(Highly balanced precision/recall performance profile)*
* **Logistic Regression Benchmark F1-Score:** `~0.814`

---

## 🎯 Top Operational Driver Feature Rankings
The structural importance vectors extracted from our trained tree identify the primary leverage points where product adjustments will improve customer sentiment:

1. **Inflight entertainment** (Highest Relative Weight)
2. **Seat comfort**
3. **Ease of Online booking**
4. **Online boarding**
5. **Inflight wifi service**

---

## 👔 Management Executive Report: Model Architecture Trade-Offs

When presenting these models to airline management stakeholders, the trade-offs between **Decision Tree Classifiers** and **Logistic Regression** break down across three dimensions:

### 1. Interpretability and Business Transparency
* **Decision Trees:** Provide unmatched transparent visibility. The logic matches human intuition exactly (e.g., *"If Inflight Wifi rating < 3 AND Seat Comfort < 2, then Passenger = Dissatisfied"*). This visual flow allows ground managers to easily audit and trust the model's logic.
* **Logistic Regression:** Relies on log-odds equations and coefficients. While it tells you the direction a variable moves satisfaction, it cannot easily display a clear, sequential step-by-step pathway for a customer service desk worker to follow.

### 2. Handling of Non-Linear Relationships
* **Decision Trees:** Handle complex, step-wise relationships naturally. For example, a delay under 15 minutes might not impact passenger sentiment, but a delay above 15 minutes drops satisfaction drastically. Decision trees capture these sudden thresholds effortlessly.
* **Logistic Regression:** Assumes a smooth, linear trend across all numerical inputs. It struggles to capture sharp threshold changes without manual and time-consuming feature engineering.

### 3. Business Actionability
* **Decision Trees win** for operational deployment. Because the paths map out distinct customer personas, management can craft targeted service recovery strategies for specific customer segments (e.g., designing special interventions for long-distance business travelers experiencing low entertainment scores).
