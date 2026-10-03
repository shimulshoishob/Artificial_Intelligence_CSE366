# CSE366 Artificial Intelligence Lab 01 - geometry.py
# Run: python geometry.py

# geometry.py
import math

def euclidean(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])
