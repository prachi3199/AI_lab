# Import necessary libraries
import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt



# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data  # features (sepal length, width, petal length, width)
y = iris.target  # labels (classes)

# Step 2: Standardize the data (important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply PCA
pca = PCA(n_components=4)  # Keep all 4 components for now
X_pca = pca.fit_transform(X_scaled)

# Step 4: Print the Eigenvalues (explained variance)
print("Eigenvalues (Explained Variance):")
print(pca.explained_variance_)

# Step 5: Plot the first two principal components
plt.figure(figsize=(8, 5))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k')
plt.xlabel("First Principal Component")
plt.ylabel("Second Principal Component")
plt.title("PCA - Iris Dataset")
plt.colorbar(label="Target Class")
plt.grid(True)
plt.show()
