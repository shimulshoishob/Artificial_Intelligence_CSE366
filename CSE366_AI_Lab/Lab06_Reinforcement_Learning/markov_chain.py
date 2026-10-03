# CSE366 Artificial Intelligence Lab 06 - markov_chain.py
# Run: python markov_chain.py

import numpy as np

states = ["Sunny", "Rainy"]
# P[i][j] = probability of going from state i today to state j tomorrow (rows sum to 1)
P = np.array([[0.8, 0.2],
              [0.4, 0.6]])

# 1) Simulate 15 days
rng = np.random.default_rng(7)
s, days = 0, []
for _ in range(15):
    days.append(states[s][0])                  # 'S' or 'R'
    s = rng.choice(2, p=P[s])                  # next state depends ONLY on current state
print("simulated days:", " ".join(days))

# 2) Probability distribution after n days, starting from a sunny day
dist = np.array([1.0, 0.0])
for n in range(1, 6):
    dist = dist @ P
    print(f"day {n}: P(Sunny) = {dist[0]:.3f}, P(Rainy) = {dist[1]:.3f}")

# 3) Stationary distribution: pi = pi P  (long-run fraction of days)
eigvals, eigvecs = np.linalg.eig(P.T)
pi = np.real(eigvecs[:, np.isclose(eigvals, 1)]).ravel()
pi = pi / pi.sum()
print("stationary distribution:", {st: round(float(p), 3) for st, p in zip(states, pi)})
