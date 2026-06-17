# Neural Network Clinical Diagnostics — Cirrhosis Risk Evaluation

## 📌 Discovery Phase Workflow & Code Implementation
To meet clinical safety guidelines and avoid algorithmic bias, raw dataset inputs underwent exact vector handling transformations:
- **Missing Value Purge:** All patient rows with incomplete or "NA" markers were dropped to guarantee clean mathematical processing streams.
- **Leakage Prevention:** `ID`, `Drug`, and `N_Days` columns were omitted entirely. Leaving `N_Days` (survival timeline) in place would create artificial accuracy inflation by leaking timeline context.
- **Strict Manual Binary Encoding:** Gender mapping rules were written explicitly to avoid unstable automatic categorical variations:
  ```python
  X_raw['Sex'] = X_raw['Sex'].map({'F': 1, 'M': 0})
  X_raw['Ascites'] = X_raw['Ascites'].map({'Y': 1, 'N': 0})
  X_raw['Hepatomegaly'] = X_raw['Hepatomegaly'].map({'Y': 1, 'N': 0})
