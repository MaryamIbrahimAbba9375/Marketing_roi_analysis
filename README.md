# Neural Network Sentiment Analysis — E-Commerce Customer Experience Routing

## 📌 Discovery Phase (Data Preparation)
- **Null Processing Handling:** Missing observations in the `review_text` column were scrubbed to prevent structural errors from entering the model's tokenization pipeline.
- **Sharpening Prediction Boundaries:** Neutral 3-star reviews were filtered out completely to create a distinct binary split between true positive and true negative expressions.
- **Target Label Mapping:** Review scores were scaled to standard binary outputs where ratings of 4–5 stars map to `1` (Positive Sentiment) and 1–2 stars map to `0` (Negative Sentiment).

---

## 🛠️ Technical Model Architecture & Configurations
The deep learning pipeline is built natively using a TensorFlow/Keras Sequential layout:
1. **TextVectorization Layer:** Lowercases characters, strips out punctuation symbols, and converts remaining terms into integers using an adapted 10,000-word vocabulary limit.
2. **Dense Embedding Layer:** Translates sparse word integers into dense 16-dimensional coordinate arrays.
3. **GlobalAveragePooling1D Layer:** Collapses sequence dimensions into fixed length vectors by taking the feature mean across the whole sentence, preventing position tracking errors.
4. **Dense Hidden Layer:** 16 hidden processing units operating on a standard `ReLU` activation function.
5. **Output Neuron Layer:** A single Dense unit using a `Sigmoid` function to ensure prediction outputs map strictly as a continuous confidence probability from `0.0` (Absolute Negative) to `1.0` (Absolute Positive).

---

## 📊 Empirical Training & Validation Metrics
Following a structured, reproducible 7-epoch training execution, the model converged with the following recorded scores:
- **Final Epoch Training Accuracy:** [Insert your Training Accuracy percentage here, e.g., 98.45%]
- **Final Validation Dataset Accuracy:** [Insert your Validation Accuracy percentage here, e.g., 99.12%]

---

## 🚀 Action Phase: Strategic String Evaluation & Auto-Routing Workflows

### 1. Mandatory Test String Analysis
- **Test Target Input:** *"The product arrived broken and I am very unhappy"*
- **Calculated Probability Confidence Score:** [Insert the exact decimal from your output screen, e.g., 0.04218]
- **Interpretation:** The score approaches near `0`, proving that the network correctly identified strong negative sentiment.

### 2. Auto-Flagging Routing Architecture Blueprint
To convert our raw confidence outputs into an efficient business workflow, we follow the threshold mapping rules below:
