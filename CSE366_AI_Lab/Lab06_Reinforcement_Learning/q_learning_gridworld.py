# CSE366 Artificial Intelligence Lab 06 - q_learning_gridworld.py
# Run: python q_learning_gridworld.py

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
