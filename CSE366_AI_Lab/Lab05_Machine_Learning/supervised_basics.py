# CSE366 Artificial Intelligence Lab 05 - supervised_basics.py
# Run: python supervised_basics.py

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
