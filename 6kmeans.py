from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load the Iris dataset
iris = load_iris()
X = iris.data  # features

# Try k = 2, 3, 4
k_values = [2, 3, 4]

print("K-Means Clustering Results:\n")

for k in k_values:
    # Create a KMeans model with k clusters
    model = KMeans(n_clusters=k, random_state=0, n_init=10)
    
    # Fit the model to the data
    model.fit(X)
    
    # Print the results
    print(f"For k = {k}:")
    print("Cluster Centers:")
    print(model.cluster_centers_)
    print("Labels assigned to each data point:")
    print(model.labels_)
    print("Inertia (distance within clusters):", model.inertia_)
    print("-" * 40)


