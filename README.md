# Transfer Learning for Automated Quality Control — Production Inspection Pipeline

## 🏗️ Architectural Advantages: GlobalAveragePooling2D vs. Flatten
This project leverages **GlobalAveragePooling2D (GAP)** rather than traditional flattening mechanics immediately after the frozen core block for three critical operational reasons:
1. **Extreme Parameter Reduction:** Instead of unrolling a $7 \times 7 \times 2048$ tensor into an oversized $100,352$ linear weight matrix, GAP reduces the entire spatial plane down to its mean value, outputting a clean $2,048$ vector. This protects the custom classification head from parameter bloating.
2. **Mitigating Validation Overfitting:** Minimizing dense interconnect weights removes structural variance vectors, allowing the model to train cleanly without dropping convergence on thin validation datasets.
3. **Preservation of Spatial Feature Relationships:** GAP bridges native feature extractions to final categorization layers cleanly, keeping dimensional localization elements stable.

---

## 📈 Milestone Implementations

### 1. Discovery Phase: Industrial Preprocessing & Augmentation
- **Input Pipeline Requirements:** All raw component photography records are scaled cleanly to **224x224 pixels** and normalized to match the mathematical expectations of ResNet50 channels.
- **Data Augmentation Constraints:** Deployed continuous `ImageDataGenerator` properties spanning **20-degree rotations, 15% zoom variations, and horizontal flips** to build environmental resilience against shifting assembly line conditions.

### 2. Technical Phase: Feature Engine Core Isolation
- **The Brain Swap:** Imported an ImageNet-trained `ResNet50` pipeline setting `include_top=False`. 
- **Layer Locking Execution:** Freezing the network parameters via `base_model.trainable = False` guarantees that pre-learned general visual shapes remain protected while localized classification shapes adjust over training epochs.

---

## 🚨 Action Phase: Real-Time Sorting Automation Logic

### Robotics Routing Framework
The inference configuration processes runtime imagery to calculate clear probability metrics. To protect manufacturing logistics channels from defective escapes, the automation stack adheres to a strict threshold filter:
- **Decision Boundary Rule:** If an inspected item yields a **Defect Probability Score $\ge$ 0.85**, the software flags a catastrophic failure event.
- **Physical Factory Action:** The logic system communicates via API to signal a robotic control arm, routing the item away from standard shipping tracks and dropping it into the **Reject Escalation Bin** instantly. Any object scoring $<0.85$ passes through to the active assembly conveyor.
