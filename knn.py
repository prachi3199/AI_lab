import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from matplotlib.colors import ListedColormap

# Load the dataset
data = pd.read_csv('Mall_Customers.csv')

# Convert Gender (Genre) to numeric: Male = 0, Female = 1
data['Genre'] = data['Genre'].map({'Male': 0, 'Female': 1})

# Features: Age and Annual Income
X = data[['Age', 'Annual Income (k$)']].values
y = data['Genre'].values  # Target: Gender

# Split the dataset (75% train, 25% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Scale the features
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Train the KNN model (k = 5)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred) * 100, "%")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Visualize the training set result
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(X_set[:, 0].min() - 1, X_set[:, 0].max() + 1, 0.01),
    np.arange(X_set[:, 1].min() - 1, X_set[:, 1].max() + 1, 0.01)
)
plt.contourf(
    X1, X2,
    model.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(('blue', 'green'))
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

# Plot the actual data points
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0], X_set[y_set == j, 1],
        color=ListedColormap(('blue', 'green'))(i),
        label=f'Gender {j} ({["Male", "Female"][j]})'
    )

plt.title("KNN Classifier (Training Set) - Mall Customers")
plt.xlabel("Age (scaled)")
plt.ylabel("Annual Income (scaled)")
plt.legend()
plt.grid(True)
plt.show()
