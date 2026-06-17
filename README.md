# Naive Bayes Classification — NBA Player Longevity Prediction

## 📌 Project Overview
This project applies a probabilistic Gaussian Naive Bayes model to forecast whether an NBA rookie will achieve a career longevity of 5+ years (`target_5yrs = 1`) based on standard continuous performance statistics (shooting percentage, points volume, rebounds, assists, turnovers, and advanced efficiency metrics).

---

## 📈 Final Model Performance Metrics

- **Precision (80.00%):** Out of all players the model flagged as safe multi-year investments, 80% successfully reached the 5-year mark. 
- **Recall (55.42%):** The model caught 55.42% of the total roster pool that achieved career longevity, sacrificing some coverage to maintain reliable positive projections.

### Confusion Matrix Breakdown
- **True Negatives (TN):** 79 (Correctly identified short-career players)
- **False Positives (FP - "Busts"):** 23 (Predicted durable, but failed under 5 years)
- **False Negatives (FN - "Sleeper Talent"):** 74 (Predicted short career, but lasted 5+ years)
- **True Positives (TP):** 92 (Correctly identified long-career players)

---

## 🧠 The Naive Bayes "Independence Assumption" Analysis

### Definition
The fundamental assumption of a Naive Bayes model is that **all predictor features are conditionally independent of each other given the class label**. Mathematically, it assumes:

$$P(X_1, X_2, ..., X_n \mid Y) = \prod_{i=1}^{n} P(X_i \mid Y)$$

### Realism in Basketball Sports Analytics
In the context of competitive basketball statistics, **this assumption is highly unrealistic.** Performance indicators do not exist in isolation:
- **Total Points vs. Efficiency:** High-volume scoring output (`total_points`) is fundamentally tied to minutes on the floor and field goal metrics (`fg`).
- **Turnovers vs. Assists:** Playmakers with higher assists (`ast`) naturally carry higher usage rates, which directly drives up turnover rates (`tov`).

### Impact on Model Performance
Because the model treats these overlapping indicators as completely independent evidence, it double-counts highly correlated signals. This does not ruin its ranking capability, but it does cause the model's raw probability estimates to become extreme or overconfident near $0$ or $1$.

---

## 💼 Scouting Department Executive Summary & Strategic Insights

### When to Trust the Model
The model achieves a **high Precision rate ($80.00\%$)**. In a scouting workflow, this tool should be trusted as a conservative risk-mitigation filtering system. If the model flags a prospect as a long-term player, there is an 80% historical probability that the asset will prove durable. Use this model during tight draft constraints or free-agency selection where wasting resources on a high-salary "Bust" must be avoided.

### Limitations & When to Question It
The model has a lower **Recall rate ($55.42\%$)**. This means it generates a high number of False Negatives (74 players). It tends to reject players with unique, unbalanced profiles or lower rookie minutes. 

**Recommendation:** Do not use this model as an absolute elimination filter. If the model rejects a player, scouts should manually inspect video footage and physical metrics to ensure they are not discarding hidden "sleeper assets" who simply lacked minutes during their initial tracking cycle.
