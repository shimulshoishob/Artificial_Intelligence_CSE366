---
title: "CSE366 Artificial Intelligence Lab — Lab 03 — Searching for Solutions"
---


**Goal:** describe any problem with four pieces, then solve it with **one generic search algorithm** that behaves as DFS or A\* depending only on how the frontier is managed.

| Piece | Meaning | Map example |
| --- | --- | --- |
| Start node | Where the search begins | S |
| Goal-test predicate | A function returning True/False: "is this a goal?" | node == G |
| Neighbour function | Returns the next states and step costs | S → \[(A, 1), (B, 5)\] |
| Heuristic function (optional) | Estimated cost to the goal; 0 if unknown | Straight-line distance |

**Key idea:** the only difference between DFS and A\* is **which path you take out of the frontier next**.

| Strategy | Frontier | Takes next |
| --- | --- | --- |
| DFS | Stack (list `pop()`) | The most recently added path |
| A\* | Priority queue (`heapq`) | The path with the lowest f = g + h |

## Part A — Problem interface and the generic searcher

```python
import heapq

# ---------------- 1. The search problem ----------------
class SearchProblem:
    """Everything a searcher needs to know about a problem."""
    def start_node(self):            raise NotImplementedError
    def is_goal(self, node):         raise NotImplementedError
    def neighbors(self, node):       raise NotImplementedError  # -> list of (neighbor, cost)
    def heuristic(self, node):       return 0                    # optional; 0 = no information

class GraphProblem(SearchProblem):
    def __init__(self, edges, start, goal, h=None):
        self.edges, self.start, self.goal = edges, start, goal
        self.h = h or {}
    def start_node(self):        return self.start
    def is_goal(self, node):     return node == self.goal
    def neighbors(self, node):   return self.edges.get(node, [])
    def heuristic(self, node):   return self.h.get(node, 0)

# ---------------- 2. One generic searcher ----------------
def generic_search(problem, strategy="dfs"):
    """strategy = 'dfs' (stack) or 'astar' (priority queue on g + h)."""
    start = problem.start_node()
    frontier = [(problem.heuristic(start), 0, [start])]   # (f, g, path)
    expanded, explored = [], set()
    while frontier:
        if strategy == "dfs":
            f, g, path = frontier.pop()                      # LIFO: newest path
        else:
            f, g, path = heapq.heappop(frontier)             # lowest f = g + h
        node = path[-1]
        if node in explored:                                 # already expanded by another path
            continue
        explored.add(node)
        expanded.append(node)
        if problem.is_goal(node):                            # goal test on expansion
            return path, g, expanded
        children = problem.neighbors(node)
        if strategy == "dfs":
            children = reversed(children)                    # so the first child is popped first
        for nbr, cost in children:
            if nbr in explored:                              # skip states already expanded
                continue
            new_g = g + cost
            new_entry = (new_g + problem.heuristic(nbr), new_g, path + [nbr])
            if strategy == "dfs":
                frontier.append(new_entry)
            else:
                heapq.heappush(frontier, new_entry)
    return None, None, expanded

# ---------------- 3. The example graph from Chapters 2 and 3 ----------------
edges = {"S": [("A", 1), ("B", 5)],
         "A": [("C", 2), ("D", 6)],
         "B": [("G", 6)],
         "C": [("G", 9)],
         "D": [("G", 1)]}
h = {"S": 7, "A": 6, "B": 5, "C": 7, "D": 1, "G": 0}
problem = GraphProblem(edges, "S", "G", h)

for strategy in ["dfs", "astar"]:
    path, cost, expanded = generic_search(problem, strategy)
    print(f"{strategy:6s} path={'->'.join(path)}  cost={cost}  expanded={expanded}")
```

**Output** — the same answers you traced by hand in Chapters 2 and 3:

```
dfs    path=S->A->C->G  cost=12  expanded=['S', 'A', 'C', 'G']
astar  path=S->A->D->G  cost=8  expanded=['S', 'A', 'D', 'G']
```

## Part B — A grid problem with a Manhattan heuristic

The same `generic_search` solves a completely different problem. Only the problem class changes. (`grid_search.py` starts with `from generic_search import SearchProblem, generic_search`, so keep both files in the same folder.)

```python
class GridProblem(SearchProblem):
    def __init__(self, grid, start, goal, use_h=True):
        self.grid, self.start, self.goal, self.use_h = grid, start, goal, use_h
    def start_node(self):     return self.start
    def is_goal(self, node):  return node == self.goal
    def neighbors(self, node):
        r, c = node
        result = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]) and self.grid[nr][nc] != "#":
                result.append(((nr, nc), 1))
        return result
    def heuristic(self, node):
        if not self.use_h:
            return 0                                   # A* with h = 0 is UCS
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])   # Manhattan

GRID = ["..........",
        "..........",
        "....####..",
        ".......#..",
        ".......#..",
        "..........",
        ".........."]
start, goal = (3, 0), (3, 9)

for use_h in [True, False]:
    p = GridProblem(GRID, start, goal, use_h)
    path, cost, expanded = generic_search(p, "astar")
    label = "A* (Manhattan)" if use_h else "UCS (h = 0)"
    print(f"{label:15s} cost={cost}  nodes expanded={len(expanded)}")
path, cost, expanded = generic_search(GridProblem(GRID, start, goal), "dfs")
print(f"{'DFS':15s} cost={cost}  nodes expanded={len(expanded)}")
```

**Output:**

```
A* (Manhattan)  cost=13  nodes expanded=44
UCS (h = 0)     cost=13  nodes expanded=64
DFS             cost=47  nodes expanded=61
```

**What to notice:**

- A\* and UCS both find the optimal cost of 13 (go round the wall), but the heuristic saves A\* about a third of the work.
- DFS finds *a* path, but it wanders: cost 47 instead of 13.
- The Manhattan distance is **admissible** here (a robot moving one square at a time can never beat it), so A\* is guaranteed optimal.

**Viva questions:**

1. How do you turn A\* into UCS? *Return 0 from the heuristic.*
2. How do you turn it into greedy best-first? *Order the priority queue by h only, ignoring g.*
3. Why is the goal tested when a node is expanded, not when it is generated? *A cheaper path to the goal may still be waiting in the frontier; testing on expansion keeps A* optimal.\*

**Exercises:** add a `"bfs"` strategy using `collections.deque`; try a heuristic that overestimates (e.g. 3 × Manhattan) and observe that A\* may return a non-optimal path.


## Code files in this folder

- `generic_search.py`
- `grid_search.py`
