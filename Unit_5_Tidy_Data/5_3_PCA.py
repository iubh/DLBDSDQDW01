# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# PCA

# %% load packages
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# %% load sample data
cancer = load_breast_cancer()

# %% scale the data
scaler = StandardScaler()
scaler.fit(cancer.data)
X_scaled = scaler.transform(cancer.data)

# %% create, train and apply a PCA model
pca = PCA(n_components=2)
pca.fit(X_scaled)
X_pca = pca.transform(X_scaled)

# %% observe changes in shape
print('Original shape: ', X_scaled.shape)
print('Transformed shape: ', X_pca.shape)

# console output:
# Original shape:  (569, 30)
# Transformed shape:  (569, 2)

# %% Plot influence mappig from original
# to PCs
import matplotlib.pyplot as plt
plt.matshow(pca.components_, cmap="viridis")
plt.yticks([0, 1], ["PC1", "PC2"])
plt.colorbar()
plt.xticks(range(len(cancer.feature_names)), \
    cancer.feature_names, rotation=60, ha='left')
plt.xlabel("Features")
plt.ylabel("PC")
