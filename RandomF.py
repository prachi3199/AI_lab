import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from matplotlib.colors import ListedColormap

# Load dataset
dataset = pd.read_csv('Churn_Modelling.csv')
dataset = dataset.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)
dataset['Gender'] = dataset['Gender'].map({'Male': 0, 'Female': 1})
dataset = pd.get_dummies(dataset, columns=['Geography'], drop_first=True)

# Use only two features for plotting
X = dataset[['Age', 'Balance']].values
y = dataset['Exited'].values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy: {:.2f}%".format(accuracy_score(y_test, y_pred) * 100))

# Plotting decision boundary for Test Data
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(
    np.arange(X_set[:, 0].min() - 1, X_set[:, 0].max() + 1, 0.01),
    np.arange(X_set[:, 1].min() - 1, X_set[:, 1].max() + 1, 0.01)
)

plt.figure(figsize=(8, 6))
plt.contourf(
    X1, X2,
    model.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(('salmon', 'lightgreen'))
)

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0], X_set[y_set == j, 1],
        color=ListedColormap(('red', 'green'))(i),
        label=f'Class {j}'
    )

plt.title('Random Forest Classifier (Test Set)')
plt.xlabel('Age (scaled)')
plt.ylabel('Balance (scaled)')
plt.legend()
plt.grid(True)
plt.show()
