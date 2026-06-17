# K-means Clustering — Palmer Penguins Morphology Analysis

## 📌 Project Overview
This analysis implements an unsupervised K-means clustering algorithm using Python and Scikit-learn to group Palmer Penguins based entirely on continuous physical attributes: bill length, bill depth, flipper length, and body mass. The goal is to determine if statistical distance metrics can recreate natural biological boundaries without prior species labels.

---

## 🧼 Preprocessing & Scaling Rationale
- **Handling Missing Values:** Rows containing missing numeric measurements were dropped to maintain vector integrity for mathematical distance calculations.
- **Feature Scaling:** Because features have completely different units (e.g., body mass ranges up to 6,300 grams while bill depth stays under 22 millimeters), failing to scale would cause body mass to completely dominate the Euclidean distance calculation. `StandardScaler` was used to center all features to a mean of 0 and a standard deviation of 1.

---

## 📊 Cluster Count Justification ($k$ Selection)
Evaluating the model across cluster ranges $k \in [2, 6]$ provided the following results:
- **$k=2$:** Highest Silhouette Score (`0.5315`). This represents a broad macro split between the large-bodied **Gentoo** penguins and the smaller **Adelie / Chinstrap** species.
- **$k=3$:** Clear elbow "bend point" where the rate of drop in Sum of Squared Errors (SSE) flattens significantly. It yields a strong Silhouette Score (`0.4472`).

### Selection Decision:
We selected **$k=3$**. While $k=2$ is mathematically dense, $k=3$ matches the actual biological taxonomy of the dataset (3 species) and uncovers the subtle structural differences in bill geometry that separate Adelie and Chinstrap penguins.

---

## 🐧 Biological Interpretation of Discovered Clusters

Based on the real-world feature averages across our 3 discovered clusters, the model successfully isolated distinct biological patterns:

1. **Cluster 0 (Chinstrap Dominant):** Characterized by long bills (~47.5mm) and deep bills (~18.8mm) with moderate body masses (~3,902g). This aligns with Chinstrap penguins.
2. **Cluster 1 (Gentoo Super-Cluster):** Characterized by massive body weights (~5,076g) and exceptionally long flippers (~217.2mm), matching Gentoo penguins perfectly.
3. **Cluster 2 (Adelie Dominant):** Characterized by short bills (~38.2mm) but deep profiles (~18.1mm) with lower body masses (~3,584g). This isolates Adelie penguins.

### 👫 Sexual Dimorphism Impact:
Within each species cluster, male penguins consistently cluster toward the upper bounds of mass and bill sizes, while females occupy the lower bounds. This confirms that within-cluster variance is partially driven by natural size differences between sexes.

---

## ⚠️ Unsupervised Clustering Limitations
- **Spherical Assumption:** K-means assumes clusters are isotropic (spherical and equally sized) and separates groups using linear boundaries. It struggles if species feature combinations overlap tightly or form elongated paths.
- **Sensitivity to Outliers:** Because centroids are updated using mean averages, highly unusual individual penguin measurements can pull cluster centers out of place.
- **Feature Selection:** Adding non-informative columns (such as year or island location) would dilute the importance of physical dimensions, shifting the cluster boundaries away from true biological species.
