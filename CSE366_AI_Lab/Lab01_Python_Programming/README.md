---
title: "CSE366 Artificial Intelligence Lab — Lab 01 — Introduction to Python Programming"
---


**Goal:** learn just enough Python to write the AI programs in later labs.

**Why Python for AI?** It reads almost like English, and it has ready-made libraries for maths (NumPy), machine learning (scikit-learn, PyTorch) and plotting (Matplotlib).

## Part A — Basic Python

```python
# ---------- Variables and types ----------
name = "Rahim"          # str
age = 21                # int
cgpa = 3.65             # float
is_student = True       # bool
print(f"{name} is {age} years old, CGPA {cgpa}")

# ---------- Lists, tuples, dictionaries, sets ----------
courses = ["CSE366", "CSE405", "MAT205"]   # list (changeable, ordered)
point = (3, 4)                              # tuple (cannot change)
marks = {"CSE366": 85, "CSE405": 78}       # dictionary (key -> value)
visited = {"A", "B"}                        # set (no duplicates)

courses.append("CSE477")
marks["MAT205"] = 90
visited.add("A")                            # ignored: already present

# ---------- Conditions and loops ----------
for course, mark in marks.items():
    grade = "A" if mark >= 80 else "B"
    print(course, mark, grade)

# ---------- List comprehension ----------
squares = [x * x for x in range(1, 6)]          # [1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]

# ---------- Functions ----------
def manhattan(p, q):
    """Distance used as a heuristic on grids (Chapter 3)."""
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

print(manhattan((0, 0), (3, 4)))   # 7

# ---------- Classes ----------
class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def is_honours(self):
        return self.cgpa >= 3.5

s = Student("Karim", 3.8)
print(s.name, s.is_honours())      # Karim True
```

**Which data structure for what in AI:**

| Structure | AI use |
| --- | --- |
| List | A path of states, a population in a genetic algorithm |
| Tuple | A grid position (row, col) — can be a dictionary key |
| Dictionary | A graph (node → neighbours), a Q-table ((state, action) → value) |
| Set | The explored set in graph search (fast "have I seen this?") |
| Class | An Agent, an Environment, a SearchProblem |

## Part B — Python modules

A **module** is simply a `.py` file whose functions and classes you can reuse with `import`. A **package** is a folder of modules.

**Your own module** — save this as `geometry.py`:

```python
# geometry.py
import math

def euclidean(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])
```

**Using it, plus standard modules every AI lab needs** — save as `main.py` in the same folder:

```python
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
```

**Modules you will meet in this course:**

| Module | Used for | Lab |
| --- | --- | --- |
| `collections.deque` | FIFO queue | 03 |
| `heapq` | Priority queue | 03 |
| `random` | Exploration, random moves | 02, 06 |
| `math` | sqrt, exp (simulated annealing, sigmoid) | 03, 05 |
| `numpy` | Fast arrays and matrices | 05, 06 |
| `sklearn` | Ready-made ML models | 05 |
| `matplotlib` | Plots | 05 |

**Practice tasks:**

1. Store a small map as a dictionary `{"S": ["A", "B"], "A": ["C"], ...}` and print every node's neighbours.
2. Write a function `path_cost(path, costs)` that adds up the edge costs along a path.
3. Put three functions into your own module and import them from another file.


## Code files in this folder

- `basics.py`
- `geometry.py`
- `main.py`
