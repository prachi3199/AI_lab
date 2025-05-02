# Decision Tree Classification with Plots

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from matplotlib.colors import ListedColormap

# Load dataset
dataset = pd.read_csv('Churn_Modelling.csv')

# Drop irrelevant columns
dataset = dataset.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

# Encode categorical variables
dataset['Gender'] = dataset['Gender'].map({'Male': 0, 'Female': 1})
dataset = pd.get_dummies(dataset, columns=['Geography'], drop_first=True)

# For plotting: use only CreditScore and Age as features
X_vis = dataset[['CreditScore', 'Age']].values
y = dataset['Exited'].values

# Train-test split for visualization data
X_train_vis, X_test_vis, y_train_vis, y_test_vis = train_test_split(X_vis, y, test_size=0.25, random_state=0)

# Feature scaling
sc_vis = StandardScaler()
X_train_vis = sc_vis.fit_transform(X_train_vis)
X_test_vis = sc_vis.transform(X_test_vis)

# Train Decision Tree on selected 2 features
classifier_vis = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier_vis.fit(X_train_vis, y_train_vis)

# Predict and evaluate
y_pred = classifier_vis.predict(X_test_vis)
cm = confusion_matrix(y_test_vis, y_pred)
accuracy = accuracy_score(y_test_vis, y_pred)

print("Confusion Matrix:\n", cm)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Plotting function
def plot_decision_boundary(X_set, y_set, title):
    X1, X2 = np.meshgrid(
        np.arange(X_set[:, 0].min() - 1, X_set[:, 0].max() + 1, 0.01),
        np.arange(X_set[:, 1].min() - 1, X_set[:, 1].max() + 1, 0.01)
    )
    plt.contourf(
        X1, X2,
        classifier_vis.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
        alpha=0.5,
        cmap=ListedColormap(('salmon', 'lightgreen'))
    )
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(
            X_set[y_set == j, 0], X_set[y_set == j, 1],
            color=ListedColormap(('red', 'green'))(i),
            label=f'Class {j}'
        )
    plt.title(title)
    plt.xlabel('Credit Score (scaled)')
    plt.ylabel('Age (scaled)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot training set
plot_decision_boundary(X_train_vis, y_train_vis, 'Decision Tree (Training Set)')

# Plot test set
plot_decision_boundary(X_test_vis, y_test_vis, 'Decision Tree (Test Set)')
