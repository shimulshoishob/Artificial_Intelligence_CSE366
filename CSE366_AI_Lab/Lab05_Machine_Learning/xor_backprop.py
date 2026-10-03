# CSE366 Artificial Intelligence Lab 05 - xor_backprop.py
# Run: python xor_backprop.py

import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

rng = np.random.default_rng(42)
W1, b1 = rng.normal(0, 1, (2, 4)), np.zeros((1, 4))   # input -> 4 hidden neurons
W2, b2 = rng.normal(0, 1, (4, 1)), np.zeros((1, 1))   # hidden -> 1 output
sigmoid = lambda z: 1 / (1 + np.exp(-z))
lr = 1.0

for epoch in range(5001):
    # ---- forward pass ----
    h = sigmoid(X @ W1 + b1)
    out = sigmoid(h @ W2 + b2)
    loss = np.mean((y - out) ** 2)
    # ---- backpropagation (chain rule) ----
    d_out = (out - y) * out * (1 - out)          # delta at output
    d_h = (d_out @ W2.T) * h * (1 - h)           # delta at hidden layer
    # ---- weight update (gradient descent) ----
    W2 -= lr * h.T @ d_out;  b2 -= lr * d_out.sum(axis=0, keepdims=True)
    W1 -= lr * X.T @ d_h;    b1 -= lr * d_h.sum(axis=0, keepdims=True)
    if epoch % 1000 == 0:
        print(f"epoch {epoch:4d}  loss = {loss:.4f}")

print("predictions:", out.round(2).ravel(), "-> rounded:", out.round().astype(int).ravel())
