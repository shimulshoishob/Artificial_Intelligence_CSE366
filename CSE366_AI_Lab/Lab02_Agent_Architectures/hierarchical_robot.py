# CSE366 Artificial Intelligence Lab 02 - hierarchical_robot.py
# Run: python hierarchical_robot.py

# '#' = wall, '.' = free.  Positions are (row, col).
GRID = ["......",
        ".##...",
        "...#..",
        ".#....",
        "......"]
MOVES = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

class GridEnv:
    """Environment: knows where the robot really is."""
    def __init__(self, start):
        self.pos = start
    def free(self, r, c):
        return 0 <= r < len(GRID) and 0 <= c < len(GRID[0]) and GRID[r][c] == "."
    def do(self, move):
        dr, dc = MOVES[move]
        r, c = self.pos[0] + dr, self.pos[1] + dc
        bumped = not self.free(r, c)
        if not bumped:
            self.pos = (r, c)
        return {"pos": self.pos, "bumped": bumped}

class BodyLayer:
    """Lowest layer: sends one motor command, reports position and bumps."""
    def __init__(self, env):
        self.env = env
        self.blocked = set()            # remembered walls
    def step(self, move):
        percept = self.env.do(move)
        if percept["bumped"]:
            dr, dc = MOVES[move]
            self.blocked.add((percept["pos"][0] + dr, percept["pos"][1] + dc))
        return percept

class MiddleLayer:
    """Navigation: reach ONE target, choosing moves that get closer, avoiding known walls."""
    def __init__(self, body):
        self.body = body
    def go_to(self, pos, target, max_steps=30):
        path, last = [pos], None
        for _ in range(max_steps):
            if pos == target:
                return pos, path
            def score(m):
                dr, dc = MOVES[m]
                nxt = (pos[0] + dr, pos[1] + dc)
                dist = abs(nxt[0] - target[0]) + abs(nxt[1] - target[1])
                penalty = 100 if nxt in self.body.blocked else 0
                back = 1 if last and MOVES[m] == tuple(-x for x in MOVES[last]) else 0
                return dist + penalty + back
            move = min(MOVES, key=score)
            percept = self.body.step(move)
            if not percept["bumped"]:
                pos, last = percept["pos"], move
                path.append(pos)
        return pos, path

class TopLayer:
    """Planning: decides the ORDER of locations to visit."""
    def __init__(self, middle, plan):
        self.middle, self.plan = middle, plan
    def run(self, start):
        pos = start
        for name, target in self.plan:
            pos, path = self.middle.go_to(pos, target)
            status = "reached" if pos == target else "FAILED"
            print(f"{name:10s} {target}: {status} via {path}")

env = GridEnv(start=(0, 0))
robot = TopLayer(MiddleLayer(BodyLayer(env)),
                 plan=[("mailroom", (4, 0)), ("office", (2, 5)), ("charger", (0, 0))])
robot.run(start=(0, 0))
print("walls discovered by bumping:", sorted(robot.middle.body.blocked))
