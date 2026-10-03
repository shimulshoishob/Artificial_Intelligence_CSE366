# CSE366 Artificial Intelligence Lab 04 - minimax_tree.py
# Run: python minimax_tree.py

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
