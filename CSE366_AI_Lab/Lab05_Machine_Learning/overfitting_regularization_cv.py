# CSE366 Artificial Intelligence Lab 05 - overfitting_regularization_cv.py
# Run: python overfitting_regularization_cv.py

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
