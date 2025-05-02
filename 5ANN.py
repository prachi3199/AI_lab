from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# List of different hidden layer configurations and activation functions
hidden_layer_configs = [(5,), (10,), (10, 5)]
activation_functions = ['relu', 'tanh', 'logistic']

print("ANN Results with different hidden layers and activation functions:\n")

# Loop through each configuration
for layers in hidden_layer_configs:
    for activation in activation_functions:
        # Create and train the ANN model
        clf = MLPClassifier(hidden_layer_sizes=layers, activation=activation, max_iter=1000, random_state=1)
        clf.fit(X_train, y_train)
        
        # Predict and calculate accuracy
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Print results
        print(f"Hidden Layers: {layers}, Activation: {activation}, Accuracy: {accuracy:.2f}")
