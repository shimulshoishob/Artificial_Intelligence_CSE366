---
title: "CSE366 Artificial Intelligence Lab — Lab 06 — Reinforcement Learning"
---


**Goal:** simulate a Markov process, then build a Q-learning agent that learns to reach a goal in a grid world through trial and error.

## Part A — Markov process (Markov chain)

A **Markov process** is a set of states with transition probabilities. The **Markov property**: tomorrow depends only on today, not on the days before.

**Example — weather:** if today is sunny, tomorrow is sunny with probability 0.8; if today is rainy, tomorrow is rainy with probability 0.6.

| From \\ To | Sunny | Rainy |
| --- | --- | --- |
| Sunny | 0.8 | 0.2 |
| Rainy | 0.4 | 0.6 |

```python
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
```

**Output:**

```
simulated days: S S R R S S R S R R R S S S S
day 1: P(Sunny) = 0.800, P(Rainy) = 0.200
day 2: P(Sunny) = 0.720, P(Rainy) = 0.280
day 3: P(Sunny) = 0.688, P(Rainy) = 0.312
day 4: P(Sunny) = 0.675, P(Rainy) = 0.325
day 5: P(Sunny) = 0.670, P(Rainy) = 0.330
stationary distribution: {'Sunny': 0.667, 'Rainy': 0.333}
```

**Check by hand:** in the long run the flow into Sunny equals the flow out, so π\_S × 0.2 = π\_R × 0.4. With π\_S + π\_R = 1 this gives π\_S = 2/3 and π\_R = 1/3. Whatever the starting day, about two days in three are sunny in the long run.

**From Markov process to MDP to RL:**

| Model | Adds | Who uses it |
| --- | --- | --- |
| Markov process | States + transition probabilities | Weather simulation, PageRank |
| Markov decision process | + actions and rewards | Planning when the model is known (value iteration, Ch 10.7) |
| Reinforcement learning | The agent does **not** know P or R and must learn by acting | Q-learning (Part B) |

## Part B — Q-learning in a grid world

The agent starts at **S** and must reach **G** (+10) while avoiding the pits **X** (−10). Every step costs −1, so shorter paths are better. The agent is never told the map; it only receives rewards.

```python
import random

# 4x4 grid world.  S = start, G = goal (+10), X = pit (-10), # = wall, each step costs -1
WORLD = ["S...",
         ".#.X",
         "....",
         "X..G"]
ACTIONS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
ROWS, COLS = len(WORLD), len(WORLD[0])

def step(state, action):
    """Environment: returns (next_state, reward, done)."""
    r, c = state
    dr, dc = ACTIONS[action]
    nr, nc = r + dr, c + dc
    if not (0 <= nr < ROWS and 0 <= nc < COLS) or WORLD[nr][nc] == "#":
        nr, nc = r, c                                   # bumped: stay in place
    cell = WORLD[nr][nc]
    if cell == "G": return (nr, nc), 10, True
    if cell == "X": return (nr, nc), -10, True
    return (nr, nc), -1, False

# ---------------- Q-learning ----------------
alpha, gamma = 0.5, 0.9                                 # learning rate, discount
epsilon = 1.0                                           # start by exploring a lot
Q = {((r, c), a): 0.0 for r in range(ROWS) for c in range(COLS) for a in ACTIONS}
random.seed(0)

def choose(state):
    if random.random() < epsilon:                       # explore
        return random.choice(list(ACTIONS))
    return max(ACTIONS, key=lambda a: Q[(state, a)])     # exploit

for episode in range(500):
    state, done, total = (0, 0), False, 0
    while not done:
        a = choose(state)
        nxt, reward, done = step(state, a)
        best_next = 0 if done else max(Q[(nxt, b)] for b in ACTIONS)
        Q[(state, a)] += alpha * (reward + gamma * best_next - Q[(state, a)])   # Q-learning update
        state, total = nxt, total + reward
    epsilon = max(0.05, epsilon * 0.99)                 # explore less over time
    if episode in (0, 50, 100, 499):
        print(f"episode {episode:3d}: total reward = {total:4d}, epsilon = {epsilon:.2f}")

# ---------------- Show the learned policy ----------------
arrow = {"U": "^", "D": "v", "L": "<", "R": ">"}
print("\nlearned policy:")
for r in range(ROWS):
    row = ""
    for c in range(COLS):
        cell = WORLD[r][c]
        row += cell if cell in "#GX" else arrow[max(ACTIONS, key=lambda a: Q[((r, c), a)])]
        row += " "
    print(row)
print("\nQ-values at start:", {a: round(Q[((0, 0), a)], 2) for a in ACTIONS})
```

**Output:**

```
episode   0: total reward =  -39, epsilon = 0.99
episode  50: total reward =  -15, epsilon = 0.60
episode 100: total reward =    5, epsilon = 0.36
episode 499: total reward =    5, epsilon = 0.05

learned policy:
> > v <
v # v X
> > v v
X > > G

Q-values at start: {'U': 0.63, 'D': 1.81, 'L': 0.63, 'R': 1.81}
```

**Reading the results:**

- **Episode 0:** the agent wanders randomly (ε = 1) and scores −39.
- **By episode 100:** it scores +5, the best possible: 5 steps at −1, then +10 for the goal on the 6th step.
- **The policy arrows** lead from S to G in 6 moves and steer away from both pits.
- **Check a Q-value by hand:** following the best path from S gives −1 − 0.9 − 0.81 − 0.729 − 0.656 + 0.9⁵ × 10 = **1.81**, exactly the learned Q(S, D) and Q(S, R). Going down or right first are equally good routes.

**Mapping the code to the theory:**

| Code | Theory (Chapter 11) |
| --- | --- |
| `step()` | The environment: returns next state and reward |
| `Q` dictionary | The Q-table Q(s, a) |
| `choose()` | ε-greedy: exploration vs exploitation |
| `epsilon * 0.99` | Decaying exploration |
| `Q[(state, a)] += alpha * (...)` | Q(s,a) ← Q(s,a) + α\[r + γ max Q(s′,a′) − Q(s,a)\] |

**Viva questions:**

1. What happens with ε = 0 from the start? *The agent never explores, may lock onto its first poor route and never find the goal efficiently.*
2. Why is Q-learning called off-policy? *It updates using the best next action (max), even when it actually took a random one.*
3. What does γ = 0 mean? *The agent only cares about the immediate reward and cannot plan towards the distant goal.*

**Exercises:** make the step cost 0 and see whether the agent still prefers the shortest path; make moves "slippery" (20% chance of moving sideways) and compare the learned policy; replace the update with SARSA and compare how close the path stays to the pits.

## Code files in this folder

- `markov_chain.py`
- `q_learning_gridworld.py`
