# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Load the dataset
data = pd.read_csv("Iris.csv")

# Convert Species (string labels) to numeric codes: Setosa=0, Versicolor=1, Virginica=2
data['Species'] = data['Species'].astype('category').cat.codes

# Select two features for visualization: Petal Length and Petal Width
X = data[['PetalLengthCm', 'PetalWidthCm']].values
y = data['Species'].values

# Split into training and testing sets (75% train, 25% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Feature scaling (important for SVM)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train SVM classifier (linear kernel)
classifier = SVC(kernel='rbf', random_state=0)
classifier.fit(X_train, y_train)

# Predict and evaluate
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:\n", cm)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Visualization (only works with 2D features)
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(X_set[:, 0].min() - 1, X_set[:, 0].max() + 1, 0.01),
    np.arange(X_set[:, 1].min() - 1, X_set[:, 1].max() + 1, 0.01)
)

plt.contourf(
    X1, X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(('lightcoral', 'lightgreen', 'lightblue'))
)

# Plot data points
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        color=ListedColormap(('red', 'green', 'blue'))(i),
        label=f"Class {j}"
    )

plt.title("SVM Classifier (Iris Dataset - Training set)")
plt.xlabel("Petal Length (scaled)")
plt.ylabel("Petal Width (scaled)")
plt.legend()
plt.grid(True)
plt.show()
