# CSE366 Artificial Intelligence Lab 04 - tictactoe.py
# Run: python tictactoe.py

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
