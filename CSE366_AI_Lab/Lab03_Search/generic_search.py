# CSE366 Artificial Intelligence Lab 03 - generic_search.py
# Run: python generic_search.py

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

if __name__ == "__main__":
    for strategy in ["dfs", "astar"]:
        path, cost, expanded = generic_search(problem, strategy)
        print(f"{strategy:6s} path={'->'.join(path)}  cost={cost}  expanded={expanded}")
