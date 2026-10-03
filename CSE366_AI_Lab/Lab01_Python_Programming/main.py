# CSE366 Artificial Intelligence Lab 01 - main.py
# Run: python main.py

import geometry                      # whole module
from geometry import manhattan       # one function
import random, heapq
from collections import deque

print(geometry.euclidean((0, 0), (3, 4)))   # 5.0
print(manhattan((0, 0), (3, 4)))            # 7

random.seed(42)                      # same "random" numbers on every run
print(random.choice(["up", "down", "left", "right"]))

q = deque(["A", "B"])                # FIFO queue  -> BFS
q.append("C"); print(q.popleft())    # A

stack = ["A", "B"]                   # LIFO stack  -> DFS
stack.append("C"); print(stack.pop())  # C

pq = []                              # priority queue -> UCS / A*
heapq.heappush(pq, (5, "B"))
heapq.heappush(pq, (1, "A"))
heapq.heappush(pq, (3, "C"))
print(heapq.heappop(pq))             # (1, 'A')  smallest first
