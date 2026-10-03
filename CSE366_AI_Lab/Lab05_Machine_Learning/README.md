---
title: "CSE366 Artificial Intelligence Lab — Lab 05 — Introduction to Machine Learning"
---


**Goal:** see learning from data in action, then meet the three tools that fight its biggest problem, overfitting: a held-out test set, regularisation, and cross-validation.

**The ML workflow used in every part:**

```
Data → split into train / test → fit model on train → measure error on test → improve
```

**Issues facing learning algorithms (recap of Chapter 7):** too little data, noisy labels, choosing model complexity (underfitting vs overfitting), and judging performance fairly. This lab shows each one with numbers.

## Part A — Simplest cases of learning and basic supervised learning

The **simplest learner ignores the input** and always predicts the average of the training targets. It is the baseline every real model must beat. Next comes a straight-line model.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Synthetic data: flat rent (thousand Tk) vs size (hundred sq ft), with noise
rng = np.random.default_rng(0)
size = rng.uniform(5, 20, 100).reshape(-1, 1)
rent = 2.0 * size.ravel() + 5 + rng.normal(0, 3, 100)

X_train, X_test, y_train, y_test = train_test_split(size, rent, test_size=0.25, random_state=0)

# 1) Simplest case of learning: ignore the input, always predict the training mean
baseline = np.full_like(y_test, y_train.mean())
print("Baseline (predict the mean) MAE:", round(mean_absolute_error(y_test, baseline), 2))

# 2) Basic supervised learning: fit a line  rent = w * size + b
model = LinearRegression().fit(X_train, y_train)
print("Learned: rent = %.2f * size + %.2f" % (model.coef_[0], model.intercept_))
print("Linear regression MAE:", round(mean_absolute_error(y_test, model.predict(X_test)), 2))
print("Prediction for a 1200 sq ft flat:", round(model.predict([[12]])[0], 1), "thousand Tk")
```

**Output:**

```
Baseline (predict the mean) MAE: 9.31
Learned: rent = 1.97 * size + 5.14
Linear regression MAE: 1.86
Prediction for a 1200 sq ft flat: 28.8 thousand Tk
```

The data was generated with rent = 2 × size + 5, and the model recovered 1.97 and 5.14 from noisy examples alone. Its average error (1.86) is five times smaller than the baseline's (9.31).

## Part B — Overfitting, regularisation and cross-validation

We fit polynomials of different degrees to 30 noisy points from a sine curve.

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import mean_squared_error

# True pattern: a sine curve. We only get 30 noisy samples.
rng = np.random.default_rng(1)
x = np.sort(rng.uniform(0, 1, 30)).reshape(-1, 1)
y = np.sin(2 * np.pi * x).ravel() + rng.normal(0, 0.2, 30)
X_tr, X_te, y_tr, y_te = train_test_split(x, y, test_size=0.33, random_state=1)

def poly_model(degree, alpha=None):
    reg = LinearRegression() if alpha is None else Ridge(alpha=alpha)
    return make_pipeline(PolynomialFeatures(degree), StandardScaler(), reg)

print("--- Overfitting: training error vs test error ---")
for d in [1, 3, 15]:
    m = poly_model(d).fit(X_tr, y_tr)
    tr = mean_squared_error(y_tr, m.predict(X_tr))
    te = mean_squared_error(y_te, m.predict(X_te))
    print(f"degree {d:2d}: train MSE = {tr:.3f}   test MSE = {te:.3f}")

print("--- Regularization: degree 15 with Ridge (L2) ---")
for a in [0.0001, 0.01, 1, 100]:
    m = poly_model(15, alpha=a).fit(X_tr, y_tr)
    tr = mean_squared_error(y_tr, m.predict(X_tr))
    te = mean_squared_error(y_te, m.predict(X_te))
    print(f"alpha {a:>8}: train MSE = {tr:.3f}   test MSE = {te:.3f}")

print("--- 5-fold cross-validation to choose the degree ---")
folds = KFold(n_splits=5, shuffle=True, random_state=0)   # shuffle: x is sorted
for d in [1, 3, 5, 9, 15]:
    scores = cross_val_score(poly_model(d), x, y, cv=folds, scoring="neg_mean_squared_error")
    print(f"degree {d:2d}: mean CV MSE = {-scores.mean():.3f}")
```

**Output:**

```
--- Overfitting: training error vs test error ---
degree  1: train MSE = 0.160   test MSE = 0.390
degree  3: train MSE = 0.036   test MSE = 0.017
degree 15: train MSE = 0.020   test MSE = 0.115
--- Regularization: degree 15 with Ridge (L2) ---
alpha   0.0001: train MSE = 0.025   test MSE = 0.047
alpha     0.01: train MSE = 0.035   test MSE = 0.043
alpha        1: train MSE = 0.115   test MSE = 0.122
alpha      100: train MSE = 0.232   test MSE = 0.772
--- 5-fold cross-validation to choose the degree ---
degree  1: mean CV MSE = 0.236
degree  3: mean CV MSE = 0.047
degree  5: mean CV MSE = 0.061
degree  9: mean CV MSE = 0.132
degree 15: mean CV MSE = 0.647
```

**Reading the results:**

| Concept | What the numbers show |
| --- | --- |
| **Underfitting** | Degree 1 (a straight line) is bad on both train (0.160) and test (0.390): too simple for a curve. |
| **Good fit** | Degree 3 has low error on both. |
| **Overfitting** | Degree 15 has the *lowest* training error (0.020) but test error rises to 0.115: it memorised the noise. |
| **Regularisation** | Ridge adds a penalty α × (sum of squared weights). A small α (0.01) cuts degree 15's test error from 0.115 to 0.043. Too much (α = 100) makes the model too stiff and it underfits (0.772). |
| **Cross-validation** | Splits the data into 5 folds; each fold is the test set once. The average error picks degree 3 as best, without touching a separate test set. |

**Ridge cost function:**

```latex
J(w) = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \alpha \sum_j w_j^2
```

**Analogy:** cross-validation is like taking 5 different mock tests instead of one; your average mock score is a fairer guess of your real exam score.

## Part C — Neural networks

**C1. A neural network from scratch (backpropagation in NumPy).** XOR cannot be learned by a single neuron (Chapter 7), but one hidden layer solves it.

```python
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
```

**Output:**

```
epoch    0  loss = 0.2775
epoch 1000  loss = 0.0025
epoch 2000  loss = 0.0008
epoch 3000  loss = 0.0004
epoch 4000  loss = 0.0003
epoch 5000  loss = 0.0002
predictions: [0.01 0.98 0.99 0.02] -> rounded: [0 1 1 0]
```

The two lines starting `d_out` and `d_h` are the backpropagation formulas from Chapter 7.3 written for whole layers at once.

**C2. A neural network with scikit-learn** on curved, two-class data:

```python
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
```

**Output:**

```
Logistic regression (straight line) test accuracy: 0.827
Neural net: train acc = 0.949, test acc = 0.907
```

The two hidden layers let the network draw a curved boundary between the two "moons", so test accuracy rises from 82.7% to 90.7%. In `MLPClassifier`, `alpha` is the L2 regularisation strength — the same idea as Ridge.

**Viva questions:**

1. Why not judge a model by its training error? *A model can memorise training data; only unseen data shows whether it generalises.*
2. What does regularisation do to the weights? *Pushes them towards zero, giving a smoother, simpler function.*
3. Why shuffle before K-fold here? *x was sorted, so unshuffled folds would test on regions the model never saw.*

**Exercises:** collect 50 rows of real data (e.g. your semester marks vs study hours) and repeat Part A; plot the degree 1, 3 and 15 curves with Matplotlib.


## Code files in this folder

- `mlp_moons.py`
- `overfitting_regularization_cv.py`
- `supervised_basics.py`
- `xor_backprop.py`
