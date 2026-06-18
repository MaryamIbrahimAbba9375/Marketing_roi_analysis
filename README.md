# RNN Recurrent Text Classifier — SMS Spam Detection Core

## 📌 Discovery Phase Pipeline
- **Target Label Transmutation:** Raw classifications were converted into numerical formats where `"spam"` maps to `1` and `"ham"` maps to `0`.
- **Text Vectorization:** Inputs were broken into integer sequence arrays using a `Tokenizer` with a set dictionary size of 5,000 words, utilizing an out-of-vocabulary (`<OOV>`) token flag to catch unfamiliar words safely.
- **Sequence Padding:** To standardize training streams for the recurrent network architecture, all inputs were formatted to a static size of 50 tokens using post-padding (`pad_sequences(maxlen=50)`).

---

## 🛠️ Recurrent Network Architecture Specifications
The neural sequence processor was constructed using a Keras Sequential layout:
1. **Embedding Processing Layer:** Maps 5,000 sparse word indices into continuous, dense 32-dimensional coordinate vectors.
2. **LSTM Recurrent Layer (32 Neurons):** Captures multi-word spatial and structural context dependencies across time steps, safely avoiding vanishing gradient issues.
3. **Dropout Layer (0.20):** Forces the network to learn generalized text styles instead of memorizing specific phrases, protecting against overfitting.
4. **Dense Layer Layer & Sigmoid Out:** Distills multi-dimensional vectors down to a probability risk threshold score between `0.0` (Safe Ham) and `1.0` (Malicious Spam).

---

## 📊 Verified Model Convergence Results
Following optimization checkpoints handled by our `EarlyStopping` monitoring callback, the classifier achieved the following empirical evaluation marks:

* **Final Training Set Accuracy:** [Insert your Training Accuracy percentage here, e.g., 99.17%]
* **Final Validation Set Accuracy:** [Insert your Validation Accuracy percentage here, e.g., 98.33%]

---

## 🚀 Action Phase: Triage Diagnostics & Precision Business Strategy

### 1. Mandatory Core Message Triage Checks
The following three baseline evaluation strings yielded these real test scores:
- **"Hey, are we still meeting for lunch?"** $\rightarrow$ Risk Score: [Insert score 1, e.g., 0.12]% $\rightarrow$ **Action: Delivered to Inbox**
- **"URGENT! Your account is locked. Click here to verify."** $\rightarrow$ Risk Score: [Insert score 2, e.g., 99.84]% $\rightarrow$ **Action: Junk Filter Tripped**
- **"Congratulations, you won a $500 gift card!"** $\rightarrow$ Risk Score: [Insert score 3, e.g., 99.52]% $\rightarrow$ **Action: Junk Filter Tripped**

### 2. Why Precision Rules Over Accuracy in SMS Filtering
In messaging operations, **Precision is significantly more critical than overall Accuracy**:
- If an algorithm has low Precision, it generates high **False Positives** (misclassifying crucial personal messages, banking alerts, or work confirmations as spam). Blocking a critical personal message causes severe user frustration and data loss.
- High Precision guarantees that when a message is moved to the hidden Junk folder, it is statistically guaranteed to be actual spam.

### 3. Confidence Threshold Deployment Recommendations
To optimize real-world user experience (UX), we recommend a split automated pipeline strategy:
- **$\ge$ 95.0% Confidence:** Automated routing straight to the hidden junk repository. This high threshold protects regular communications from being hidden by mistake.
- **50.0% to 94.9% Confidence:** Placed into an in-app "Suspected Spam" warning banner flag, prompting explicit manual feedback from the user.
- **< 50.0% Confidence:** Standard delivery directly to the user's main chat inbox screen.
