---
title: "CSE366 Artificial Intelligence Lab — Lab 04 — Multiagent Systems"
---


**Goal:** implement minimax and alpha-beta pruning for **two-player zero-sum games**, check them on the Chapter 5 tree, then use them to play tic-tac-toe perfectly.

**Zero-sum** means one player's gain is exactly the other's loss. We use one number for the whole game: +1 = MAX (X) wins, −1 = MIN (O) wins, 0 = draw. MAX tries to push it up, MIN tries to push it down.

## Part A — Minimax and alpha-beta on a game tree

```python
import math

# A game tree: a list = an internal node, a number = a leaf utility.
# Levels alternate MAX, MIN, MAX ... starting with MAX at the root.
TREE = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]      # the Chapter 5 example

leaves_seen = []

def minimax(node, is_max):
    if not isinstance(node, list):              # leaf
        leaves_seen.append(node)
        return node
    values = [minimax(child, not is_max) for child in node]
    return max(values) if is_max else min(values)

def alphabeta(node, is_max, alpha=-math.inf, beta=math.inf):
    if not isinstance(node, list):
        leaves_seen.append(node)
        return node
    if is_max:
        value = -math.inf
        for child in node:
            value = max(value, alphabeta(child, False, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:                   # MIN above will never allow this
                break                           # prune remaining children
        return value
    else:
        value = math.inf
        for child in node:
            value = min(value, alphabeta(child, True, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:                   # MAX above already has something better
                break
        return value

leaves_seen.clear()
print("minimax value   :", minimax(TREE, True), " leaves examined:", leaves_seen)
leaves_seen.clear()
print("alpha-beta value:", alphabeta(TREE, True), " leaves examined:", leaves_seen)
```

**Output:**

```
minimax value   : 3  leaves examined: [3, 12, 8, 2, 4, 6, 14, 5, 2]
alpha-beta value: 3  leaves examined: [3, 12, 8, 2, 14, 5, 2]
```

Same value (3), and alpha-beta skipped leaves 4 and 6 — exactly the pruning traced by hand in Chapter 5.

## Part B — Tic-tac-toe

The board is a 9-character string, positions 0–8. X is MAX, O is MIN.

```python
import math, time

LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def winner(b):
    for i, j, k in LINES:
        if b[i] != " " and b[i] == b[j] == b[k]:
            return b[i]
    return None

def utility(b):                     # zero-sum: X wins +1, O wins -1, draw 0
    w = winner(b)
    return 1 if w == "X" else -1 if w == "O" else 0

def terminal(b):
    return winner(b) is not None or " " not in b

def moves(b):
    return [i for i in range(9) if b[i] == " "]

def play(b, i, p):
    return b[:i] + p + b[i+1:]

nodes = 0
def minimax(b, player):             # X = MAX, O = MIN
    global nodes; nodes += 1
    if terminal(b):
        return utility(b)
    if player == "X":
        return max(minimax(play(b, m, "X"), "O") for m in moves(b))
    return min(minimax(play(b, m, "O"), "X") for m in moves(b))

def alphabeta(b, player, alpha=-math.inf, beta=math.inf):
    global nodes; nodes += 1
    if terminal(b):
        return utility(b)
    if player == "X":
        v = -math.inf
        for m in moves(b):
            v = max(v, alphabeta(play(b, m, "X"), "O", alpha, beta))
            alpha = max(alpha, v)
            if alpha >= beta: break
        return v
    v = math.inf
    for m in moves(b):
        v = min(v, alphabeta(play(b, m, "O"), "X", alpha, beta))
        beta = min(beta, v)
        if alpha >= beta: break
    return v

def best_move(b, player):
    """Pick the move with the best alpha-beta value for the player to move."""
    scored = [(alphabeta(play(b, m, player), "O" if player == "X" else "X"), m) for m in moves(b)]
    return max(scored)[1] if player == "X" else min(scored)[1]

empty = " " * 9
for name, f in [("minimax", minimax), ("alpha-beta", alphabeta)]:
    nodes = 0; t = time.time()
    v = f(empty, "X")
    print(f"{name:10s} value of empty board = {v}, nodes visited = {nodes:,}, time = {time.time()-t:.2f}s")

# The computer plays both sides. Optimal play -> draw.
b, p = empty, "X"
while not terminal(b):
    b = play(b, best_move(b, p), p)
    p = "O" if p == "X" else "X"
for r in range(3):
    print(" " + " | ".join(b[3*r:3*r+3]))
print("Result:", winner(b) or "draw")
```

**Output** (times will differ on your computer):

```
minimax    value of empty board = 0, nodes visited = 549,946, time = 0.67s
alpha-beta value of empty board = 0, nodes visited = 18,297, time = 0.02s
 O | X | X
 X | O | O
 O | X | X
Result: draw
```

**What to notice:**

|  | Minimax | Alpha-beta |
| --- | --- | --- |
| Value of the empty board | 0 (draw) | 0 (draw) — identical |
| Nodes visited | 549,946 | 18,297 — about 30 times fewer |

- A value of 0 proves tic-tac-toe is a **draw with perfect play** from both sides.
- Alpha-beta never changes the answer, only the amount of work.

**Viva questions:**

1. What does α ≥ β mean? *The current player's opponent already has a better option elsewhere, so this branch will never be reached.*
2. Why can't we use full minimax for chess? *About 10¹²³ nodes; we must cut off at a depth and use an evaluation function.*
3. How would you make alpha-beta prune more? *Examine likely-best moves first (e.g. the centre square, captures in chess).*

**Exercises:** add a depth limit and an evaluation function (e.g. number of lines still open for X minus for O); let a human play against `best_move` with `input()`.


## Code files in this folder

- `minimax_tree.py`
- `tictactoe.py`
