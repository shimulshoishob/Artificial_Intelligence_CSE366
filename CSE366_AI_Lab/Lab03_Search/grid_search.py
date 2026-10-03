# CSE366 Artificial Intelligence Lab 03 - grid_search.py
# Run: python grid_search.py

from generic_search import SearchProblem, generic_search

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
