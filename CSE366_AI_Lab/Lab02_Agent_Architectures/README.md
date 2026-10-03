---
title: "CSE366 Artificial Intelligence Lab — Lab 02 — Agent Architectures and Hierarchical Control"
---


**Goal:** code the agent–environment loop from Chapter 1, then split an agent's controller into layers.

```
Environment  ── percept ──▶  Agent
     ▲                         │
     └──────── action ──────────┘
```

The **environment** owns the true state and changes it when an action arrives. The **agent** only sees percepts and returns actions. The **controller** is the agent's decision function.

## Part A — Environment, agent and a simple controller

```python
class Environment:
    """The world. It receives actions and returns percepts."""
    def initial_percept(self):
        raise NotImplementedError
    def do(self, action):
        raise NotImplementedError

class Agent:
    """Anything that maps percepts to actions."""
    def select_action(self, percept):
        raise NotImplementedError

def simulate(agent, env, steps):
    percept = env.initial_percept()
    for t in range(steps):
        action = agent.select_action(percept)     # agent decides
        print(f"t={t}  percept={percept}  action={action}")
        percept = env.do(action)                  # environment changes

# ---------- A concrete environment: a room ----------
class Room(Environment):
    def __init__(self, temp=18.0):
        self.temp = temp
    def initial_percept(self):
        return round(self.temp, 1)
    def do(self, action):
        if action == "heater_on":
            self.temp += 1.5          # heater warms the room
        else:
            self.temp -= 1.0          # room cools down by itself
        return round(self.temp, 1)

# ---------- The agent's controller: a thermostat ----------
class Thermostat(Agent):
    def __init__(self, low=20, high=22):
        self.low, self.high = low, high
        self.heater = "heater_off"     # memory: last command
    def select_action(self, temp):
        if temp < self.low:
            self.heater = "heater_on"
        elif temp > self.high:
            self.heater = "heater_off"
        return self.heater             # between low and high: keep the last command

simulate(Thermostat(), Room(18.0), steps=10)
```

**Output:**

```
t=0  percept=18.0  action=heater_on
t=1  percept=19.5  action=heater_on
t=2  percept=21.0  action=heater_on
t=3  percept=22.5  action=heater_off
t=4  percept=21.5  action=heater_off
t=5  percept=20.5  action=heater_off
t=6  percept=19.5  action=heater_on
t=7  percept=21.0  action=heater_on
t=8  percept=22.5  action=heater_off
t=9  percept=21.5  action=heater_off
```

The temperature settles between 19.5°C and 22.5°C. Because the thermostat **remembers** its last command, it is a model-based agent (it has a belief state), not a pure reflex agent. Without that memory it would switch on and off at every reading around 21°C.

## Part B — Hierarchical control: a delivery robot

The robot works in a grid with walls it does not know in advance. Control is split into three layers. Each layer only talks to the one directly below it.

| Layer | Job | Time scale | Knows about |
| --- | --- | --- | --- |
| Top | Decide the order of places to visit | Whole task | Named locations |
| Middle | Reach one target, avoid walls | A few steps | Target, distances, remembered walls |
| Body | Execute one move, report bumps | One step | Motors and the bump sensor |

```python
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
```

**Output:**

```
mailroom   (4, 0): reached via [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
office     (2, 5): reached via [(4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3), (3, 4), (2, 4), (2, 5)]
charger    (0, 0): reached via [(2, 5), (1, 5), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0)]
walls discovered by bumping: [(1, 2), (2, 3)]
```

**What happened:** on the way to the office, the robot at (2, 2) bumped into walls at (1, 2) and (2, 3). The body layer remembered them, and the middle layer steered down and around through row 3. The top layer never had to know about walls — that is the point of hierarchy.

**Viva questions:**

1. Which class is the environment and which is the agent? *GridEnv is the environment; the three layers together form the agent.*
2. Why does the middle layer penalise going backwards? *To stop it oscillating between two cells.*
3. Is the greedy middle layer guaranteed to reach every target? *No. In a maze with a dead end it can get stuck; replacing it with A* from Lab 03 fixes that.\*

**Exercises:** add a wall at (3, 3) and predict the new route; add a battery level that the top layer checks before each delivery.


## Code files in this folder

- `hierarchical_robot.py`
- `thermostat_agent.py`
