# CSE366 Artificial Intelligence Lab 05 - mlp_moons.py
# Run: python mlp_moons.py

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression

X, y = make_moons(n_samples=500, noise=0.25, random_state=0)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=0)

linear = LogisticRegression().fit(X_tr, y_tr)
print("Logistic regression (straight line) test accuracy:", round(linear.score(X_te, y_te), 3))

nn = MLPClassifier(hidden_layer_sizes=(16, 16), activation="relu", alpha=0.0001,
                   max_iter=2000, random_state=0).fit(X_tr, y_tr)
print(f"Neural net: train acc = {nn.score(X_tr, y_tr):.3f}, test acc = {nn.score(X_te, y_te):.3f}")
