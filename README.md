# TikTok User Verification Prediction Matrix — Logistic Regression Pipeline

## 🏗️ Project Architecture & Framework Overview
This repository contains a full machine learning implementation designed to classify user account verification status on TikTok. The project addresses class imbalances and extracts text characteristics to accurately predict account types.

---

## 📈 Milestone Breakdown & Methodology

### Milestone 1: Discovery & Preprocessing
- **Class Imbalance Mitigation:** The dataset possesses an extreme **94% unverified / 6% verified** class distribution imbalance. To prevent the model from blindly guessing the majority class, we leverage cost-sensitive learning via the `class_weight='balanced'` parameter within the optimization engine.
- **Feature Extraction:** Extracted a new feature, `text_length`, from the raw `video_transcription_text` parameter to capture whether wordier transcriptions correlate with institutional or verified status accounts. Missing records were systematically filled using median feature parameters to avoid data leakage.

### Milestone 2: Feature Engineering & Encoding
- **Categorical Encoding:** Converted non-numeric categories like `claim_status` into numeric vectors using **One-Hot Encoding** configurations.
- **Multicollinearity Cleanout:** Analyzed data features using a Pearson correlation matrix. Features with extreme statistical overlap (such as `video_like_count` vs. `video_view_count`) were dropped to protect the stability of the Logistic Regression model coefficients.

### Milestone 3: Model Construction & Evaluation
- **Data Splitting:** Divided data rows using an **80/20 train-test split**, tracking class distributions precisely via stratified sampling arrays.
- **Scaling Hygiene:** Fitted a `StandardScaler` strictly across the training features to prevent data leaks before transforming the testing sets.
- **Performance Diagnostics:** Built an interpretable **Logistic Regression model**. Evaluation focus centers heavily on **Recall and F1-Score metric indicators** for the minority verified class, ensuring legitimate creators are rarely missed.

---

## 💡 Strategic Business Insights & Recommendations
- **Transcription Metrics:** Longer transcription lengths possess distinct predictive weight adjustments, confirming that high-value verified accounts often provide clearer context structural profiles.
- **Content Profiling:** Accounts publishing verified fact profiles (`opinion` status tags) display significantly lower overall community violations compared to accounts driven by controversial `claim` text formats. This offers clear routing vectors for automated trust and safety pipelines.
