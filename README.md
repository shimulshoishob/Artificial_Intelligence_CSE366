# Artificial_Intelligence_CSE366
Complete CSE366 Artificial Intelligence course materials with comprehensive notes, algorithms, examples, and practical Python implementations.

# CSE366 Artificial Intelligence — Easy Course Notes

Oct 3, 2026 · @CO-Work

## How to use these notes

These notes cover all 11 chapters of CSE366 in plain language. Each topic follows the same pattern: a simple definition, a small worked example, and a real-world example you already know.

- **Read the "In one line" summary first.** If you understand it, you understand the core idea.
- **Work every small example by hand.** Exams ask you to trace BFS, compute minimax values, or do one Q-learning update.
- **Use the comparison tables before exams.** They summarise completeness, optimality and complexity in one place.

One running example appears in several chapters: a **food-delivery rider in Dhaka** who must find a route, avoid traffic, and learn which roads are fast. It shows how the same agent can use search, heuristics, probability and learning.

## Chapter 01 — Artificial Intelligence and Agents

**In one line:** AI is about building agents that sense their world, decide, and act to reach goals.

### 1.1 Introduction to Artificial Intelligence

**What is AI?** Artificial Intelligence is the study of building computer systems that do tasks which need intelligence when humans do them: reasoning, planning, learning, understanding language, and recognising images.

A useful way to think about it is "acting rationally": an AI system tries to take the **best action** given what it knows.

**AI principles (the big ideas)**

- **Representation** — describe the world in a form the computer can work with (a map as a graph, a game as a tree).
- **Search** — explore possible actions to find a path to the goal.
- **Reasoning** — draw new conclusions from known facts.
- **Learning** — improve with experience or data.
- **Handling uncertainty** — act sensibly when information is incomplete or noisy.

**AI problem-solving** usually follows four steps:

1. **Define the problem**: initial state, goal state, possible actions, and the cost of actions.
2. **Choose a representation**: states, graph, tree, variables.
3. **Choose a method**: search, optimisation, logic, probability, learning.
4. **Execute and evaluate** the solution.

*Small example — 8-puzzle:* the state is the tile layout, actions are moving the blank up/down/left/right, the goal is tiles in order, and each move costs 1.

**Role of AI in the real world**

| Area | Example | AI technique behind it |
| --- | --- | --- |
| Navigation | Google Maps, Pathao/Uber routing | Search (A\*), traffic prediction |
| Entertainment | YouTube and Netflix recommendations | Machine learning |
| Language | ChatGPT, Claude, Google Translate | Neural networks |
| Health | Detecting disease from X-rays | Deep learning |
| Finance | bKash/bank fraud detection | Probability and learning |
| Games | Chess engines, game bots | Adversarial search |
| Robotics | Warehouse robots, self-driving cars | Planning, reinforcement learning |

### 1.2 Agents

**What is an agent?** An agent is anything that **perceives** its environment through **sensors** and **acts** on it through **actuators**.

| Agent | Sensors | Actuators | Environment |
| --- | --- | --- | --- |
| Human | Eyes, ears, skin | Hands, legs, voice | The world |
| Robot vacuum | Bump sensor, dirt sensor, camera | Wheels, brushes | Rooms of a house |
| Self-driving car | Camera, LiDAR, GPS | Steering, brake, accelerator | Roads, traffic |
| Spam filter | Incoming email text | Move to inbox or spam | Email system |
| Chess program | Board position | Chosen move | Chess board and opponent |

**Agent and environment** interact in a loop:

```
Agent
   ↓
Perceives Environment   (percept)
   ↓
Makes Decision          (agent function)
   ↓
Takes Action            (actuator)
   ↓
Environment changes  →  back to the top
```

- **Percept** = what the agent senses at one moment.
- **Percept sequence** = everything it has sensed so far.
- **Agent function** = the rule that maps percept sequences to actions.

**Agent behaviour.** The behaviour is the action the agent picks after each percept. *Example:* a robot vacuum senses "dirty" → it sucks; senses "clean" → it moves to the next square.

**Types of environments** (often asked in exams):

| Property | Easy version | Hard version | Example of hard |
| --- | --- | --- | --- |
| Observability | Fully observable (chess) | Partially observable | Poker: you can't see cards |
| Determinism | Deterministic (puzzle) | Stochastic | Driving: others are unpredictable |
| Episodes | Episodic (classify one image) | Sequential | Chess: each move affects the future |
| Change | Static (crossword) | Dynamic | Traffic keeps moving while you think |
| Values | Discrete (chess moves) | Continuous | Steering angle |
| Agents | Single agent (Sudoku) | Multi-agent | Football, auctions |

**Intelligent (rational) agents.** A rational agent chooses the action that **maximises its expected performance**, based on what it has perceived and what it knows.

A performance measure says what "good" means. For a robot vacuum: amount of floor cleaned, minus electricity used, minus noise.

**Types of agents (simple → smart):**

1. **Simple reflex agent** — acts only on the current percept with if–then rules. *Example:* a thermostat: if temperature < 25°C, turn heater on.
2. **Model-based reflex agent** — keeps an internal model of what it cannot currently see. *Example:* a car remembering a vehicle is in its blind spot.
3. **Goal-based agent** — picks actions that reach a goal. *Example:* Google Maps finds a route to your destination.
4. **Utility-based agent** — picks the action with the best "happiness score" among goal-reaching options. *Example:* Maps chooses the route that is fastest *and* has no tolls.
5. **Learning agent** — improves its behaviour from experience. *Example:* YouTube recommendations get better the more you watch.

### 1.3 Agent Architectures

**Agent architecture** = the internal structure that connects the agent's sensors to its actuators: how percepts are processed, how decisions are made, and how actions are sent out.

**Agent control** = the part that decides **what to do next**. It takes the current percept plus memory (the "belief state") and outputs a command.

```
Percept + Memory (belief state)  →  Controller  →  Command (action)
                                       ↓
                                 Updated memory
```

**Hierarchical control.** Complex agents split control into **layers**. Higher layers think slowly about long-term goals; lower layers react quickly to the immediate situation. Each layer gives commands to the layer below and receives reports back.

| Layer | Time scale | Delivery-robot example | Self-driving car example |
| --- | --- | --- | --- |
| High (planning) | Minutes | Choose order of delivery stops | Plan route Dhanmondi → Gulshan |
| Middle (navigation) | Seconds | Go to next stop, avoid obstacles | Change lanes, take the next turn |
| Low (reactive) | Milliseconds | Wheel speeds, stop if bump | Brake, steer, keep in lane |

**Why layers?** Each layer is simpler to design. The low layer can react instantly (brake for a child) without waiting for the slow planner.

**Real-world analogy:** a company. The CEO sets yearly goals, managers plan weekly tasks, and workers handle each moment's work.

## Chapter 02 — Uninformed Search

**In one line:** uninformed (blind) search explores the state space using only the problem definition — it has no idea which direction the goal is in.

**Analogy:** you lost your keys and search every room in some fixed order, with no clue where they are.

### Key terms

- **State** — one situation of the problem (a city on a map).
- **Node** — a state in the search tree, plus its parent and path cost.
- **Frontier (open list)** — nodes generated but not yet expanded.
- **Expand** — take a node out of the frontier and generate its children.
- **Explored set (closed list)** — states already expanded, so we don't repeat them.
- **b** = branching factor (children per node), **d** = depth of the shallowest goal, **m** = maximum depth of the tree.
- **Complete** = always finds a solution if one exists. **Optimal** = finds the lowest-cost solution.

### The example graph used in this chapter

Start = **S**, Goal = **G**. Numbers are step costs. Children are taken in alphabetical order.

```
S → A (1)     S → B (5)
A → C (2)     A → D (6)
B → G (6)
C → G (9)
D → G (1)
```

Possible paths: S→B→G costs 11, S→A→C→G costs 12, S→A→D→G costs **8 (cheapest)**.

### 2.1 Breadth-First Search (BFS)

**Idea:** explore **level by level** — all nodes at depth 1, then depth 2, and so on. The frontier is a **FIFO queue** (first in, first out).

**Trace on the example:**

| Step | Expand | Queue after expanding |
| --- | --- | --- |
| 1 | S | A, B |
| 2 | A | B, C, D |
| 3 | B | C, D, G ← goal generated |

BFS returns **S → B → G** (2 steps, cost 11). It found the path with the fewest *steps*, not the lowest *cost*.

- **Complete:** Yes (if b is finite).
- **Optimal:** Yes only when every step costs the same.
- **Time and space:** O(b^d). Memory is BFS's big weakness — it stores the whole level.

**Real world:** "People you may know" on Facebook — friends of friends are found level by level. Also finding the minimum number of moves in a puzzle, or the fewest network hops between two routers.

### 2.2 Depth-First Search (DFS)

**Idea:** go as **deep** as possible down one branch, then **backtrack**. The frontier is a **LIFO stack** (or recursion).

**Trace on the example:** S → A → C → G. DFS returns **S → A → C → G** (cost 12) — not the best.

- **Complete:** No — it can go forever down an infinite branch or loop (yes on finite graphs with cycle checking).
- **Optimal:** No.
- **Time:** O(b^m). **Space:** O(b·m) — very memory-friendly.

**Real world:** solving a maze by always following one corridor until a dead end; exploring folders on your computer; backtracking solvers for Sudoku.

### 2.3 Uniform Cost Search (UCS)

**Idea:** always expand the node with the **lowest path cost g(n)** so far. The frontier is a **priority queue** ordered by g(n). This is Dijkstra's algorithm in search form.

**Trace on the example (cost in brackets):**

| Step | Expand | Frontier after (priority queue) |
| --- | --- | --- |
| 1 | S(0) | A(1), B(5) |
| 2 | A(1) | C(3), B(5), D(7) |
| 3 | C(3) | B(5), D(7), G(12) |
| 4 | B(5) | D(7), G(11) ← cheaper G replaces G(12) |
| 5 | D(7) | G(8) ← cheaper again |
| 6 | G(8) | Goal reached |

UCS returns **S → A → D → G** with cost **8**, the optimal path. Note: the goal test is done when a node is **expanded**, not when it is generated.

- **Complete:** Yes, if every step cost ≥ some small ε > 0.
- **Optimal:** Yes.
- **Time and space:** O(b^(1 + C\*/ε)), where C\* is the optimal cost.

**Real world:** finding the cheapest bus/train fare combination, or the shortest-distance road route when roads have different lengths.

### 2.4 Depth-Limited Search (DLS)

**Idea:** DFS, but **stop going deeper at a limit l**. Nodes at depth l are treated as if they have no children.

*Example:* with l = 1 on our graph, DLS only reaches S, A, B — it never sees G (depth 2), so it fails. With l = 2, it finds S → B → G.

- **Complete:** No, if l < d. **Optimal:** No.
- **Time:** O(b^l). **Space:** O(b·l).

**Real world:** "six degrees of separation" — searching for a connection but only up to 6 links; a chess program that looks only 4 moves ahead.

### 2.5 Iterative Deepening Search (IDS)

**Idea:** run DLS with l = 0, then l = 1, then l = 2, … until the goal is found. It gets the **completeness and optimality of BFS** with the **low memory of DFS**.

*Example on our graph:* l = 0 → {S}; l = 1 → {S, A, B}; l = 2 → finds G via S → B → G.

**Isn't repeating work wasteful?** Not much. Most nodes are at the deepest level, so the repeated upper levels are cheap. With b = 10 and d = 5, IDS generates about 123,450 nodes versus BFS's 111,110 — only about 11% more.

- **Complete:** Yes. **Optimal:** Yes when step costs are equal.
- **Time:** O(b^d). **Space:** O(b·d).

**Real world:** chess engines use iterative deepening: they search 1 move deep, then 2, then 3… and play the best move found when time runs out.

### 2.6 Bidirectional Search

**Idea:** run two searches at once — **forward from the start** and **backward from the goal** — and stop when they **meet in the middle**.

```
Start → → →  (meet)  ← ← ← Goal
```

**Why it is fast:** two searches of depth d/2 are much smaller than one of depth d.

```latex
b^{d/2} + b^{d/2} \ll b^{d}
```

With b = 10 and d = 6: one-way BFS ≈ 1,000,000 nodes; bidirectional ≈ 2 × 1,000 = 2,000 nodes.

- **Complete:** Yes (with BFS on both sides). **Optimal:** Yes for equal step costs.
- **Time and space:** O(b^(d/2)).
- **Limitation:** you must know the goal state exactly and be able to go **backwards** (find predecessors).

**Real world:** LinkedIn finding how you are connected to someone (searching from both people); route planners searching from both origin and destination.

### Summary table

| Algorithm | Frontier | Complete? | Optimal? | Time | Space |
| --- | --- | --- | --- | --- | --- |
| BFS | FIFO queue | Yes | Yes (equal costs) | O(b^d) | O(b^d) |
| DFS | LIFO stack | No | No | O(b^m) | O(b·m) |
| UCS | Priority queue by g(n) | Yes | Yes | O(b^(1+C\*/ε)) | O(b^(1+C\*/ε)) |
| DLS | Stack with limit l | No (if l < d) | No | O(b^l) | O(b·l) |
| IDS | Repeated DLS | Yes | Yes (equal costs) | O(b^d) | O(b·d) |
| Bidirectional | Two queues | Yes | Yes (equal costs) | O(b^(d/2)) | O(b^(d/2)) |

**Exam tip:** if asked "which uses the least memory but is still complete?" → **IDS**.

## Chapter 03 — Informed Search

**In one line:** informed search uses a **heuristic** — an educated guess of how far the goal is — to explore promising nodes first.

**Analogy:** looking for a restaurant in Gulshan. You don't search every street randomly (uninformed); you walk *towards* the area where you think it is (informed).

### Heuristic functions

A heuristic **h(n)** estimates the cost from node n to the goal. It must be cheap to compute.

| Problem | Common heuristic |
| --- | --- |
| Route finding on a map | Straight-line ("as the crow flies") distance to the destination |
| 8-puzzle | h₁ = number of misplaced tiles |
| 8-puzzle (better) | h₂ = Manhattan distance: sum of how many rows + columns each tile is from its place |
| Grid robot | Manhattan distance \|x₁ − x₂\| + \|y₁ − y₂\| |

**Admissible heuristic:** it **never overestimates** the true cost. If h\*(n) is the real cost to the goal:

```latex
0 \le h(n) \le h^*(n)
```

*Example:* straight-line distance is admissible because no road can be shorter than a straight line.

**Consistent (monotone) heuristic:** for every node n and its child n′ reached with step cost c(n, n′):

```latex
h(n) \le c(n, n') + h(n')
```

This is like the triangle inequality. Every consistent heuristic is also admissible.

**Dominance:** if h₂(n) ≥ h₁(n) for all n and both are admissible, h₂ is **better** — it is closer to the truth, so A\* expands fewer nodes. Manhattan distance dominates misplaced tiles.

### Example graph with heuristics

Same graph as Chapter 2, plus h values (all admissible and consistent):

| Node | S | A | B | C | D | G |
| --- | --- | --- | --- | --- | --- | --- |
| h(n) | 7 | 6 | 5 | 7 | 1 | 0 |
| True cost to G | 8 | 7 | 6 | 9 | 1 | 0 |

### 3.1 Greedy Best-First Search

**Idea:** always expand the node that **looks closest to the goal**.

```latex
f(n) = h(n)
```

**Trace:**

| Step | Expand | Frontier (by h) |
| --- | --- | --- |
| 1 | S | B(5), A(6) |
| 2 | B | G(0), A(6) |
| 3 | G | Goal reached |

Greedy returns **S → B → G**, cost **11** — fast, but **not optimal** (the best is 8). It was fooled because B *looked* close.

- **Complete:** No in general (can loop); yes on finite graphs with an explored set.
- **Optimal:** No.
- **Time and space:** O(b^m) worst case, but often much faster with a good heuristic.

**Real world:** a delivery rider who always takes the road pointing most directly towards the customer — usually quick, but sometimes it leads into a jam or a dead end.

### 3.2 A\* Search

**Idea:** combine the cost already paid with the estimated cost remaining.

```latex
f(n) = g(n) + h(n)
```

- g(n) = actual cost from the start to n.
- h(n) = estimated cost from n to the goal.
- f(n) = estimated total cost of the best path through n.

**Trace:**

| Step | Expand | New nodes: g + h = f | Frontier (by f) |
| --- | --- | --- | --- |
| 1 | S (0+7=7) | A: 1+6=7, B: 5+5=10 | A(7), B(10) |
| 2 | A (7) | C: 3+7=10, D: 7+1=8 | D(8), B(10), C(10) |
| 3 | D (8) | G: 8+0=8 | G(8), B(10), C(10) |
| 4 | G (8) | Goal reached | — |

A\* returns **S → A → D → G**, cost **8** — optimal — and it never had to expand B or C. UCS reached the same answer but expanded 5 nodes before G; A\* expanded only 3.

- **Complete:** Yes.
- **Optimal:** Yes, if h is admissible (tree search) or consistent (graph search).
- **Time:** exponential in the worst case, but a good heuristic makes it far faster.
- **Space:** keeps all generated nodes in memory — its main weakness.

**Real world:** Google Maps style route planning, video-game characters finding a path around walls, robot navigation.

### 3.3 IDA\* (Iterative Deepening A\*)

**Idea:** A\* uses too much memory. IDA\* does a **depth-first search with an f-cost limit** instead of a depth limit. If the goal isn't found, raise the limit to the **smallest f value that exceeded it**, and repeat.

**Trace:**

1. **Threshold = f(S) = 7.** Explore S(7) → A(7) → C(10) cut, D(8) cut; B(10) cut. Smallest cut value = 8.
2. **Threshold = 8.** Explore S → A → C(10) cut, D(8) → G(8). **Goal found, cost 8.**

- **Complete and optimal:** Yes (with admissible h).
- **Space:** O(b·d) — linear, like DFS.
- **Drawback:** repeats work between iterations.

**Real world:** solving the 15-puzzle or Rubik's-cube style puzzles, where A\* would run out of memory.

### Comparison: BFS, UCS, Greedy and A\*

| Algorithm | Picks node with lowest | Uses heuristic? | Complete? | Optimal? | Path found on our graph |
| --- | --- | --- | --- | --- | --- |
| BFS | Depth | No | Yes | Only if equal costs | S→B→G (11) |
| UCS | g(n) | No | Yes | Yes | S→A→D→G (8) |
| Greedy | h(n) | Yes | No | No | S→B→G (11) |
| A\* | g(n) + h(n) | Yes | Yes | Yes (admissible h) | S→A→D→G (8) |
| IDA\* | g(n) + h(n), with threshold | Yes | Yes | Yes | S→A→D→G (8) |

**Remember:** UCS is A\* with h(n) = 0. Greedy is A\* with g(n) ignored.

**Search efficiency:** a better heuristic (closer to the true cost, still admissible) means fewer node expansions. For the 8-puzzle at depth 14, A\* with misplaced tiles expands about 539 nodes on average, while Manhattan distance needs only about 113.

## Chapter 04 — Metaheuristic Algorithms

**In one line:** when the search space is too big to explore fully, metaheuristics start with a candidate solution and **keep improving it**, aiming for a "good enough" answer quickly.

Here we don't care about the *path*, only the *final state*. Examples: the best timetable, the best delivery schedule, the best neural-network weights.

**Key words:**

- **Objective / fitness function** — the score of a solution (maximise profit, or minimise cost/error).
- **Neighbour** — a solution made by a small change to the current one.
- **State-space landscape** — imagine every solution as a point on a hilly map, where height = score.

### 4.1 Hill Climbing

**Idea:** look at the neighbours, move to the **best** one if it is better than the current one, and stop when no neighbour is better.

**Analogy:** climbing a mountain in thick fog. You can only feel the ground around your feet, so you keep stepping uphill until every direction goes down.

**Small example:** maximise f(x) = −(x − 3)² + 9 for whole numbers x. Neighbours are x − 1 and x + 1. Start at x = 0.

| Step | x | f(x) | Best neighbour | Move? |
| --- | --- | --- | --- | --- |
| 1 | 0 | 0 | x = 1, f = 5 | Yes |
| 2 | 1 | 5 | x = 2, f = 8 | Yes |
| 3 | 2 | 8 | x = 3, f = 9 | Yes |
| 4 | 3 | 9 | x = 2 or 4, f = 8 | No → stop |

It finds x = 3, the maximum. On this simple hill it works perfectly. On a bumpy landscape it can get stuck.

**Problems of hill climbing:**

| Problem | What it is | Analogy |
| --- | --- | --- |
| **Local maximum** | A peak higher than its neighbours but lower than the highest peak | Climbing a small hill and thinking it's Everest |
| **Global maximum** | The best solution overall — what we actually want | The real summit |
| **Plateau** | A flat area where all neighbours have the same score, so there's no uphill direction | A flat field in the fog |
| **Shoulder** | A plateau that does lead uphill further on | A flat ledge on the way up |
| **Ridge** | A narrow upward ridge; every single step goes down, even though the ridge rises overall | A knife-edge mountain path you can't walk straight along |

### 4.2 Variations of Hill Climbing

| Variation | How it works | Fixes |
| --- | --- | --- |
| Steepest-ascent | Check all neighbours, take the best | The basic version |
| Stochastic | Pick a random uphill neighbour (better moves more likely) | Less greedy, sometimes finds better peaks |
| First-choice | Generate random neighbours until one is better, take it | Fast when there are thousands of neighbours |
| Sideways moves | Allow moves to equal-score neighbours (with a limit) | Plateaus and shoulders |
| Random-restart | Run hill climbing many times from random starts, keep the best | Local maxima — very effective in practice |
| Local beam search | Keep k states at once and keep the k best neighbours of all of them | Shares information between searches |

*Example:* in the 8-Queens problem, basic hill climbing solves only about 14% of random starts, but random-restart almost always finds a solution after a few tries.

### 4.3 Simulated Annealing

**Idea:** like hill climbing, but **sometimes accept a worse move** to escape local maxima. Early on it accepts bad moves often; later it becomes strict.

**Analogy:** annealing metal — heat it, then cool it slowly so the atoms settle into a strong structure. Or shaking a tray with a ball to get it into the deepest hole: shake hard first, then gently.

**Algorithm:**

1. Pick a random neighbour.
2. If it is better, move to it.
3. If it is worse by ΔE, move to it with probability:

```latex
P(\text{accept}) = e^{-\Delta E / T}
```

4. Lower the temperature T using the **cooling schedule** (for example T ← 0.95 × T) and repeat.

**Example:** a move is worse by ΔE = 2.

| Temperature T | e^(−2/T) | Meaning |
| --- | --- | --- |
| 10 (hot, early) | 0.82 | Accepted 82% of the time — lots of exploring |
| 2 | 0.37 | Accepted 37% of the time |
| 0.5 (cold, late) | 0.02 | Almost never accepted — acts like hill climbing |

- **Temperature** controls how adventurous the search is.
- **Cooling schedule** — if T is lowered slowly enough, simulated annealing finds the global optimum with probability approaching 1.

**Real world:** VLSI chip layout, university exam timetabling, airline crew scheduling.

### 4.4 Genetic Algorithm (GA)

**Idea:** copy natural evolution. Keep a **population** of solutions; the fittest ones "reproduce", and children mix their parents' features with small random changes.

| Term | Meaning | Example (5-bit number) |
| --- | --- | --- |
| Population | A set of candidate solutions | 4 strings |
| Chromosome | One candidate solution | 01101 |
| Gene | One part of a chromosome | A single bit, e.g. 1 |
| Fitness function | Score of a chromosome | f(x) = x² |
| Selection | Choose parents; fitter ones more likely | Roulette wheel |
| Crossover | Combine two parents to make children | Swap tails after a cut point |
| Mutation | Randomly flip a gene | 01100 → 01110 |
| New generation | Children replace the old population | Repeat the cycle |

**Worked example:** maximise f(x) = x², where x is 0–31 written in 5 bits.

**Step 1 — Initial population and fitness:**

| Chromosome | x | Fitness x² | Selection probability |
| --- | --- | --- | --- |
| 01101 | 13 | 169 | 169 / 1170 = 14.4% |
| 11000 | 24 | 576 | 49.2% |
| 01000 | 8 | 64 | 5.5% |
| 10011 | 19 | 361 | 30.9% |

**Step 2 — Selection (roulette wheel):** 11000 has the biggest slice, so it is picked most often. Suppose we pick 01101 and 11000.

**Step 3 — Crossover at point 4:**

```
Parent 1: 0110 | 1        Child 1: 0110 | 0  = 01100 (12)
Parent 2: 1100 | 0   →    Child 2: 1100 | 1  = 11001 (25)
```

Child 2 (25² = 625) is already fitter than any parent.

**Step 4 — Mutation:** with a small probability, flip a bit: 11001 → 11011 (27, fitness 729).

**Step 5 —** form the new generation and repeat until the population reaches 11111 (31) or stops improving.

**Real world:** designing NASA's ST5 spacecraft antenna, optimising delivery routes, tuning machine-learning hyperparameters.

### 4.5 Differential Evolution (DE)

The course outline writes "Differential Evaluation"; the standard name of the algorithm is **Differential Evolution**.

**Idea:** a population-based method for **continuous** (real-number) problems. New candidates are made by adding the **scaled difference of two solutions** to a third.

**Steps for each target vector xᵢ:**

1. **Mutation** — pick three other random vectors x\_r1, x\_r2, x\_r3 and make a donor vector:

```latex
v = x_{r1} + F \cdot (x_{r2} - x_{r3})
```

2. **Crossover** — build a trial vector u by taking each component from v with probability CR, otherwise from xᵢ.
3. **Selection** — if u is better than xᵢ, u replaces it in the next generation; otherwise keep xᵢ.

**Example:** F = 0.5, x\_r1 = (2, 3), x\_r2 = (4, 1), x\_r3 = (1, 2).

- Difference: x\_r2 − x\_r3 = (3, −1).
- Scaled: 0.5 × (3, −1) = (1.5, −0.5).
- Donor: v = (2 + 1.5, 3 − 0.5) = **(3.5, 2.5)**.

**GA vs DE:** GA usually works on bit strings and relies on crossover; DE works on real numbers and relies on difference-based mutation.

**Real world:** tuning the parameters of a power-system controller, fitting curves to experimental data, antenna and filter design.

### 4.6 Gradient Descent

**Idea:** to **minimise** a loss function J(θ), repeatedly take a step in the direction where the loss decreases fastest — opposite to the gradient.

```latex
\theta_{new} = \theta_{old} - \alpha \nabla J(\theta)
```

- **Objective / loss function J(θ)** — measures how bad the current parameters are.
- **Gradient ∇J(θ)** — the slope; it points uphill.
- **Learning rate α** — the step size.
- **Parameter update** — the formula above, repeated many times.

**Analogy:** walking down a hill blindfolded — feel the slope under your feet and step downhill. Small steps are safe but slow; giant steps may jump over the valley.

**Worked example:** J(θ) = θ², so ∇J = 2θ. Start θ = 4, α = 0.1.

| Iteration | θ | Gradient 2θ | Update | New θ |
| --- | --- | --- | --- | --- |
| 1 | 4.00 | 8.00 | 4 − 0.1 × 8 | 3.20 |
| 2 | 3.20 | 6.40 | 3.2 − 0.64 | 2.56 |
| 3 | 2.56 | 5.12 | 2.56 − 0.512 | 2.05 |

θ moves steadily towards 0, the minimum.

**Learning rate matters:** with α = 1.1, θ goes 4 → −4.8 → 5.76 → … and **diverges**. With α = 0.001 it is extremely slow.

**Real world:** training every neural network, including ChatGPT, image classifiers and recommendation systems.

### Summary

| Method | Works with | Escapes local optima? | Typical use |
| --- | --- | --- | --- |
| Hill climbing | One solution | No (unless restarts) | Quick local improvement |
| Simulated annealing | One solution | Yes, accepts worse moves | Scheduling, layout |
| Genetic algorithm | Population | Yes, through diversity | Discrete design problems |
| Differential evolution | Population | Yes | Continuous optimisation |
| Gradient descent | One solution + gradient | No (needs a differentiable function) | Training ML models |

## Chapter 05 — Adversarial Search

**In one line:** in games, an opponent is working against you, so you must choose moves assuming the opponent also plays its best.

### 5.1 Game vs Single-Agent Search

|  | Single-agent search | Game (adversarial) search |
| --- | --- | --- |
| Who acts | Only you | You and an opponent take turns |
| Goal | Reach a goal state | Win / maximise your final score |
| Solution | A **sequence of actions** (a path) | A **strategy**: what to do for every opponent reply |
| Uncertainty | Environment only | The opponent's choices |
| Example | Route finding, 8-puzzle | Chess, tic-tac-toe, Ludo, checkers |

Most games studied here are **two-player, zero-sum, deterministic, fully observable**: one player's gain equals the other's loss (+1 win, −1 loss, 0 draw).

**Game formulation:** initial state, PLAYER(s) = whose turn, ACTIONS(s), RESULT(s, a), TERMINAL-TEST(s) = is the game over, and UTILITY(s) = the final score.

### 5.2 Game Trees

A **game tree** shows every possible sequence of moves.

- **Root** = the current position.
- **Levels alternate**: MAX's turn, then MIN's turn, then MAX's…
- **Leaves** = finished games with a utility value.
- One full move by each player = 2 **plies**.

*Size example:* tic-tac-toe has at most 9! = 362,880 move sequences — a computer can search it all. Chess has about 35 moves per position and 80 plies per game, so about 35⁸⁰ ≈ 10¹²³ nodes — impossible to search fully. That's why we need pruning and depth limits.

### 5.3 Minimax Algorithm

**Players:**

- **MAX** — you; wants the **highest** utility.
- **MIN** — the opponent; wants the **lowest** utility.

**Rule:** compute values from the leaves upwards.

```latex
MINIMAX(s) = \begin{cases} UTILITY(s) & \text{if } s \text{ is terminal} \\ \max_a MINIMAX(RESULT(s,a)) & \text{if MAX's turn} \\ \min_a MINIMAX(RESULT(s,a)) & \text{if MIN's turn} \end{cases}
```

**Worked example (from the outline):**

```
          MAX
        /     \
      MIN     MIN
     /  \     /  \
    3    5   2    9
```

1. Left MIN node: min(3, 5) = **3**.
2. Right MIN node: min(2, 9) = **2**.
3. MAX root: max(3, 2) = **3**.

**MAX chooses the left move, and the game value is 3 — not 5.** A common mistake is to pick the biggest leaf (9) or the biggest in the left branch (5). MAX can't get 5 because MIN will reply with the move that gives 3. If MAX goes right hoping for 9, MIN answers with 2.

**Properties:**

- **Complete:** Yes (finite tree). **Optimal:** Yes, against an optimal opponent.
- **Time:** O(b^m). **Space:** O(b·m) (it is a depth-first search).

**Depth-limited minimax:** for big games, stop at a depth and score positions with an **evaluation function**. *Example for chess:* (my material − opponent's material), where pawn = 1, knight/bishop = 3, rook = 5, queen = 9.

**Real world:** chess engines, tic-tac-toe bots, game AI in strategy games; also security planning where you assume the worst-case attacker.

### 5.4 Alpha-Beta Pruning

**Idea:** get the **same answer as minimax** while skipping branches that **cannot affect the final decision**.

- **α (alpha)** = the best (highest) value MAX is guaranteed so far on this path. Starts at −∞.
- **β (beta)** = the best (lowest) value MIN is guaranteed so far on this path. Starts at +∞.
- **Prune** whenever **α ≥ β**: the rest of that branch can't be chosen.

**Analogy:** you are choosing between restaurants. Restaurant A guarantees a meal you rate 3/5. At restaurant B, the first dish you hear about is rated 2/5, and your friend (MIN) gets to pick the dish there. B can now only be ≤ 2, which is worse than 3, so you stop asking about B's other dishes.

**Worked example:**

```
                 MAX
        /         |          \
      MIN        MIN         MIN
     / | \      / | \       / | \
    3 12  8    2  4  6    14  5  2
```

| Step | Node | What happens | α, β |
| --- | --- | --- | --- |
| 1 | Left MIN | Sees 3, 12, 8 → value = 3 | Root α becomes 3 |
| 2 | Middle MIN | Sees 2 → value ≤ 2 | α = 3, β = 2 |
| 3 | Middle MIN | α (3) ≥ β (2) → **prune 4 and 6** | — |
| 4 | Right MIN | Sees 14 (β = 14), then 5 (β = 5), then 2 (β = 2) → value 2 | No prune: β never fell to 3 or below before the last leaf |
| 5 | Root MAX | max(3, ≤2, 2) = **3** | Same answer as minimax |

Two leaves were never examined. In big trees the savings are huge.

**Efficiency:**

- Worst case (bad move order): O(b^m) — no better than minimax.
- Best case (best moves examined first): O(b^(m/2)). This means alpha-beta can search **about twice as deep** in the same time.
- **Move ordering matters:** trying captures and threats first in chess leads to more pruning.

**Real world:** IBM's Deep Blue (beat Kasparov in 1997) and modern chess engines like Stockfish use alpha-beta with good move ordering and evaluation functions.

|  | Minimax | Alpha-beta |
| --- | --- | --- |
| Result | Optimal move | Same optimal move |
| Nodes examined | All | Fewer (prunes useless branches) |
| Best-case time | O(b^m) | O(b^(m/2)) |
| Extra bookkeeping | None | α and β values |

## Chapter 06 — Constraint Satisfaction Problems

**In one line:** a CSP asks you to give every variable a value so that **all the rules (constraints) are satisfied** at once.

**Analogy:** making your semester class routine. Each course needs a time slot (variable → value), and rules apply: no two of your courses at the same time, a teacher can't be in two rooms, Friday is off.

### 6.1 CSP Problem Formulation

```
CSP
├── Variables    X = {X₁, X₂, …, Xₙ}
├── Domains      D = {D₁, D₂, …, Dₙ}   (allowed values of each variable)
└── Constraints  C = rules on which combinations are allowed
```

- **Assignment** — giving values to some or all variables.
- **Consistent assignment** — breaks no constraint.
- **Complete assignment** — every variable has a value.
- **Valid solution** — an assignment that is **both complete and consistent**.

**Types of constraints:**

- **Unary** — one variable: "SA ≠ green".
- **Binary** — two variables: "WA ≠ NT".
- **Global / higher-order** — many variables: "all digits in a Sudoku row are different" (AllDiff).

A **constraint graph** draws variables as nodes and binary constraints as edges.

**Example 1 — Map colouring (Australia).** Colour 7 regions so that neighbours have different colours.

| Part | Value |
| --- | --- |
| Variables | WA, NT, SA, Q, NSW, V, T |
| Domain | {Red, Green, Blue} for each |
| Constraints | WA≠NT, WA≠SA, NT≠SA, NT≠Q, SA≠Q, SA≠NSW, SA≠V, Q≠NSW, NSW≠V (T has no neighbours) |
| One solution | WA=R, NT=G, SA=B, Q=R, NSW=G, V=R, T=R (or any colour) |

**Example 2 — Sudoku.** Variables = 81 cells; domain = {1–9}; constraints = AllDiff on every row, column and 3×3 box.

**Example 3 — N-Queens.** Variables = Q₁…Qₙ (the row of the queen in each column); domain = {1…n}; constraints = no two queens in the same row or diagonal.

**Real world:** university exam timetabling, assigning gates to flights at an airport, nurse shift scheduling, frequency assignment for mobile towers (neighbouring towers must use different frequencies — the same as map colouring).

### 6.2 Constraint Propagation

**Idea:** use the constraints to **remove impossible values** from domains *before* or *during* search. Fewer values = less searching.

**Forward checking:** after assigning a variable, remove conflicting values from its neighbours' domains. If any domain becomes empty, backtrack immediately.

*Map example:* assign WA = Red.

| Variable | Domain before | Domain after WA = Red |
| --- | --- | --- |
| NT | {R, G, B} | {G, B} |
| SA | {R, G, B} | {G, B} |
| Others | {R, G, B} | unchanged |

Then assign Q = Green → NT becomes {B}, SA becomes {B}. But NT and SA are neighbours and both can only be Blue — a problem forward checking **doesn't notice** yet.

**Arc consistency (AC-3):** an arc X → Y is consistent if, for **every** value of X, there is **some** allowed value in Y. Keep removing values until all arcs are consistent.

*Continuing the example:* NT = {B}, SA = {B}. Check arc SA → NT: if SA = B, NT must be ≠ B, but NT only has B. Remove B from SA → SA = { } (empty). **Failure detected early**, before searching further, so WA = R, Q = G can't work together.

**Analogy:** Sudoku players pencil in possible numbers in each cell and cross them out as they place digits. That pencil-and-erase process is constraint propagation.

### 6.3 Backtracking Search

**Idea:** a depth-first search that assigns **one variable at a time** and **undoes (backtracks)** as soon as a constraint is broken.

```
function BACKTRACK(assignment):
    if assignment is complete: return assignment
    var ← pick an unassigned variable
    for each value in domain(var):
        if value is consistent with assignment:
            add var = value
            (optional) run forward checking / AC-3
            result ← BACKTRACK(assignment)
            if result ≠ failure: return result
            remove var = value          ← backtrack
    return failure
```

**Worked example — 4-Queens** (one queen per column; the value is the row 1–4):

1. Q1 = 1.
2. Q2: row 1 same row, row 2 diagonal → Q2 = 3.
3. Q3: rows 1–4 all attacked → **dead end, backtrack**.
4. Q2 = 4. Q3 = 2. Q4: all rows attacked → **backtrack**.
5. Nothing left for Q2 with Q1 = 1 → **backtrack** to Q1.
6. Q1 = 2, Q2 = 4, Q3 = 1, Q4 = 3 → **solution**.

```
. . Q .
Q . . .
. . . Q
. Q . .
```

**Heuristics that make backtracking much faster:**

| Heuristic | Question it answers | Rule | Intuition |
| --- | --- | --- | --- |
| MRV (minimum remaining values) | Which variable next? | Pick the one with the fewest legal values left | "Fail first" — tackle the hardest part early |
| Degree heuristic | Tie-break for MRV | Pick the variable involved in the most constraints | SA touches 5 regions, so colour it early |
| LCV (least constraining value) | Which value to try first? | Pick the value that removes the fewest options from neighbours | Leave the most freedom for later |

**Real world:** the same idea powers Sudoku apps, timetabling software, and configuration tools (e.g. building a PC where parts must be compatible).

| Method | What it does | Cost |
| --- | --- | --- |
| Plain backtracking | Try, check, undo | Can be exponential |
| + Forward checking | Prune neighbours' domains after each assignment | Small extra work, big savings |
| + Arc consistency | Prune all arcs repeatedly | More work per step, detects failures earliest |

## Chapter 07 — Learning in AI

**In one line:** instead of programming every rule by hand, we let the computer **learn the rules from examples (data)**.

### 7.1 Introduction to Machine Learning

**What is machine learning?** A program learns if its **performance P** at a **task T** improves with **experience E** (Tom Mitchell's definition).

*Example — spam filter:* T = classify emails as spam or not; E = thousands of emails labelled by users; P = % of emails classified correctly.

**Traditional programming vs ML:**

```
Traditional:  Data + Rules     →  Answers
Machine learning:  Data + Answers →  Rules (a model)
```

**Learning from data — the three main types:**

| Type | Data given | Goal | Example |
| --- | --- | --- | --- |
| Supervised | Inputs **with** correct answers (labels) | Predict the label for new inputs | House price from size; cat vs dog photos |
| Unsupervised | Inputs **without** labels | Find hidden groups or structure | Grouping customers by shopping habits |
| Reinforcement | Rewards and penalties from acting | Learn the best actions | Game-playing AI, robot walking (Chapter 11) |

**Learning problems in supervised learning:**

- **Classification** — output is a category: spam / not spam, disease / healthy.
- **Regression** — output is a number: tomorrow's temperature, the price of a flat in Mirpur.

**Issues facing learning algorithms:**

| Issue | What goes wrong | Analogy |
| --- | --- | --- |
| Overfitting | The model memorises training data, including noise, and fails on new data | A student who memorises past questions but can't solve a new one |
| Underfitting | The model is too simple to capture the pattern | Using a straight line to describe a curve |
| Not enough data | Patterns can't be learned reliably | Judging a restaurant from one visit |
| Noisy / wrong labels | The model learns mistakes | Learning from a textbook full of errors |
| Bias in data | The model is unfair to groups under-represented in the data | A face recognizer trained mostly on one skin tone |
| Choosing features | Irrelevant inputs confuse the model | Predicting exam marks from shoe size |
| Computation cost | Big models need lots of time and hardware | Training large language models costs millions |

We check for these by splitting data into **training**, **validation** and **test** sets, and measuring performance on data the model has never seen (**generalisation**).

### 7.2 Neural Networks (Feed-Forward)

**Idea:** a network of simple units (**neurons**) loosely inspired by the brain. Each neuron takes inputs, multiplies each by a **weight**, adds a **bias**, and passes the result through an **activation function**.

```latex
z = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b, \qquad y = f(z)
```

| Part | Meaning | Analogy |
| --- | --- | --- |
| Inputs x | The features (pixel values, age, income…) | Facts you consider when deciding |
| Weights w | How important each input is | How much you trust each fact |
| Bias b | Shifts the decision threshold | Your general mood before deciding |
| Activation f | Adds non-linearity and squashes the output | The final "yes / no / how much" |
| Output y | The neuron's result | Your decision |

**Common activation functions:**

| Function | Formula | Output range | Used for |
| --- | --- | --- | --- |
| Step | 1 if z ≥ 0, else 0 | 0 or 1 | The original perceptron |
| Sigmoid | 1 / (1 + e^(−z)) | 0 to 1 | Probabilities, binary output |
| Tanh | (e^z − e^(−z)) / (e^z + e^(−z)) | −1 to 1 | Hidden layers (older networks) |
| ReLU | max(0, z) | 0 to ∞ | Hidden layers in modern networks |
| Softmax | e^(zᵢ) / Σ e^(zⱼ) | 0 to 1, sums to 1 | Multi-class output |

**Layers:**

- **Input layer** — receives the raw features (no computation).
- **Hidden layer(s)** — learn intermediate patterns (edges → shapes → faces).
- **Output layer** — gives the final prediction.
- **Feed-forward** means information flows only forward: input → hidden → output, with no loops.

**Why hidden layers?** A single neuron can only draw a straight line between classes. It can do AND and OR, but **not XOR**. Adding a hidden layer lets the network learn curved, complex boundaries.

**Worked example — forward pass of one neuron:**

Inputs x₁ = 1, x₂ = 0.5; weights w₁ = 0.4, w₂ = 0.6; bias b = 0.1; sigmoid activation.

1. z = 0.4 × 1 + 0.6 × 0.5 + 0.1 = **0.8**
2. y = 1 / (1 + e^(−0.8)) = 1 / 1.449 = **0.69**

**Real world:** handwritten digit recognition (postal codes), face unlock on phones, voice assistants, Bangla OCR.

### 7.3 Backpropagation (simple form)

**Idea:** after a forward pass, measure the **error**, then send it **backwards** through the network to find how much each weight caused it, and adjust each weight a little to reduce the error. It is gradient descent (Chapter 4.6) applied to a neural network.

```
Input → Hidden Layer → Output   (forward pass)
                         ↓
                       Error = target − output
                         ↓
          Backpropagation (error flows backwards)
                         ↓
                    Weight update
                         ↓
                 Repeat for many examples (epochs)
```

**Key formulas (sigmoid output, squared error):**

```latex
E = \tfrac{1}{2}(t - y)^2
```

```latex
\delta = (y - t)\, y\,(1 - y), \qquad \frac{\partial E}{\partial w_i} = \delta \, x_i, \qquad w_i^{new} = w_i - \eta \, \delta \, x_i
```

Here t = target, y = output, η = learning rate, and y(1 − y) is the derivative of the sigmoid.

**Worked example — continue the neuron above.** Target t = 1, learning rate η = 0.5.

| Step | Calculation | Result |
| --- | --- | --- |
| Output | from the forward pass | y = 0.69 |
| Error | ½ (1 − 0.69)² | E = 0.048 |
| Delta | (0.69 − 1) × 0.69 × 0.31 | δ = −0.066 |
| Update w₁ | 0.4 − 0.5 × (−0.066) × 1 | w₁ = 0.433 |
| Update w₂ | 0.6 − 0.5 × (−0.066) × 0.5 | w₂ = 0.617 |
| Update b | 0.1 − 0.5 × (−0.066) | b = 0.133 |

New z = 0.433 + 0.3085 + 0.133 = 0.875 → y = 0.706. The output moved **closer to the target 1**, so the error fell.

**For hidden neurons:** their δ is computed from the δ values of the layer after them, weighted by the connecting weights. That is the "back" in backpropagation — the **chain rule** passing blame backwards layer by layer.

**Analogy:** a football team loses a goal. The coach traces back: the goalkeeper, then the defender who lost the ball, then the midfielder's bad pass. Each player is corrected in proportion to how much they contributed to the goal.

**Real world:** every modern deep-learning model — image recognition, translation, ChatGPT — is trained with backpropagation plus gradient descent.

## Chapter 08 — Knowledge Base

**In one line:** a knowledge base (KB) stores facts and rules in logic, and the agent **derives new facts** from them automatically.

**Analogy:** a detective's notebook. It has facts ("the door was locked") and rules ("if the door was locked and nothing is broken, the thief had a key"). From these the detective reasons to new conclusions.

### 8.1 Propositional Reasoning

**Proposition:** a statement that is either **true** or **false**. *Examples:* "It is raining" (P), "The road is wet" (Q). "Close the door" is not a proposition.

**Logical operators and truth table:**

| P | Q | ¬P (NOT) | P ∧ Q (AND) | P ∨ Q (OR) | P → Q (IF…THEN) | P ↔ Q (IFF) |
| --- | --- | --- | --- | --- | --- | --- |
| T | T | F | T | T | T | T |
| T | F | F | F | T | F | F |
| F | T | T | F | T | T | F |
| F | F | T | F | F | T | T |

**Remember P → Q:** it is false **only** when P is true and Q is false. "If it rains, the road is wet" is not broken on a dry, sunny day.

**Key ideas:**

- **Interpretation (model)** — an assignment of true/false to every atom.
- **Logical consequence (KB ⊨ g)** — g is true in every model where all KB statements are true.
- **Inference** — deriving new sentences mechanically. The main rule is **Modus Ponens**: from P and P → Q, conclude Q.
- **Sound** — the proof procedure only derives true consequences. **Complete** — it derives every consequence.

### 8.2 Propositional Definite Clauses

A **definite clause** is a rule with exactly one conclusion (head) and a body of atoms joined by AND:

```latex
h \leftarrow a_1 \land a_2 \land \dots \land a_m
```

Read it as "h is true **if** a₁ and a₂ … and aₘ are all true". If m = 0, it is just a **fact** (atomic clause): `h.`

**Running example — a room light:**

```
light_on   ← switch_up ∧ power_ok.
power_ok   ← breaker_ok.
breaker_ok.
switch_up.
```

Definite clauses are simple but powerful: they are the basis of the Prolog programming language and of most rule-based expert systems. They cannot express "NOT" or "OR" in the head, which keeps reasoning fast.

### 8.3 Proof Procedures

A proof procedure finds which atoms are consequences of the KB.

**Bottom-up (forward chaining):** start from facts, keep firing rules whose bodies are all true, until nothing new appears.

| Round | Rule that fires | Known set C |
| --- | --- | --- |
| 0 | Facts | {breaker\_ok, switch\_up} |
| 1 | power\_ok ← breaker\_ok | + power\_ok |
| 2 | light\_on ← switch\_up ∧ power\_ok | + light\_on |
| 3 | Nothing new | Stop |

**Top-down (backward chaining / SLD resolution):** start from the **query** and work backwards to facts.

```
Query:  yes ← light_on
      → yes ← switch_up ∧ power_ok     (use light_on rule)
      → yes ← power_ok                 (switch_up is a fact)
      → yes ← breaker_ok               (use power_ok rule)
      → yes ←                          (breaker_ok is a fact)  ✔ proved
```

|  | Bottom-up | Top-down |
| --- | --- | --- |
| Starts from | Facts | The question |
| Good when | You want all conclusions | You want to answer one question |
| Analogy | Writing down everything you can conclude | A detective working backwards from "who did it?" |
| Used in | Production systems, alarms | Prolog, expert systems |

Both are **sound** and **complete** for definite clauses.

### 8.4 Ask-the-User and Knowledge-Level Debugging

**Ask-the-user.** Some facts are not known in advance — only the user knows them. These are marked as **askable** atoms. During a top-down proof, when the system needs an askable atom, it **asks the user** instead of failing.

*Example — a medical-advice system:*

```
see_doctor ← has_fever ∧ fever_days_more_than_3.
askable has_fever.
askable fever_days_more_than_3.
```

The system asks "Do you have a fever?" If the answer is no, it **doesn't ask** the second question. Asking only what is needed makes the system faster and friendlier.

**Real world:** bank chatbots, online symptom checkers, tax-filing software that asks only the questions relevant to you.

**Knowledge-level debugging.** The KB can be wrong. We debug using the *meaning* of rules (is this rule true in the real world?), not the code. There are three kinds of bugs:

| Bug | Symptom | How to find it |
| --- | --- | --- |
| Incorrect answer | KB proves something that is false in reality | Trace the proof: find a rule whose body atoms are all true but whose head is false — that rule is wrong |
| Missing answer | KB fails to prove something that is true | Find an atom that is true but has no rule whose body is all true — a rule or fact is missing |
| Infinite loop | Top-down proof never ends | Look for circular rules like a ← b and b ← a |

*Example:* the system concludes light\_on, but the light is actually off. Check `light_on ← switch_up ∧ power_ok`: switch\_up and power\_ok are both really true, yet the light is off → this rule is wrong; it is missing a condition like `bulb_ok`.

### 8.5 Proof by Contradiction

```
Assume the opposite
      ↓
Derive a contradiction (false)
      ↓
The original statement must hold
```

In knowledge bases this uses two tools:

- **Integrity constraint:** `false ← a ∧ b` means a and b can never both be true. *Example:* `false ← light_on ∧ room_dark.`
- **Assumables:** atoms we are willing to assume (like "this component works"), but which might be false.

If assuming a set of assumables lets us derive **false**, then those assumptions can't all be true — at least one is false.

*Everyday example:* "Assume Rahim was at home all evening. But CCTV shows him at the shop at 8 pm. Contradiction → he was **not** at home all evening."

*Math example:* to prove √2 is irrational, assume it is rational (a/b in lowest terms), derive that a and b are both even, which contradicts "lowest terms".

### 8.6 Conflicts and Consistency-Based Diagnosis

**Idea:** find **what is broken** by checking which "it works normally" assumptions are inconsistent with what we observe.

**Example — a light and a fan on the same switch.** Assumables: ok\_bulb, ok\_fan, ok\_switch.

```
light_on ← ok_bulb ∧ ok_switch.
fan_on   ← ok_fan  ∧ ok_switch.
false ← light_on.      (observed: light is OFF)
false ← fan_on.        (observed: fan is OFF)
```

- **Conflict:** a set of assumables that together derive false. Here: **{ok\_bulb, ok\_switch}** and **{ok\_fan, ok\_switch}**.
- **Minimal conflict:** no smaller subset is also a conflict (both above are minimal).
- **Diagnosis:** a set of assumables that, if false, removes **every** conflict (it "hits" each conflict at least once).

| Candidate diagnosis | Resolves conflict 1? | Resolves conflict 2? | Minimal? |
| --- | --- | --- | --- |
| {ok\_switch} is false | Yes | Yes | **Yes — simplest explanation** |
| {ok\_bulb, ok\_fan} are false | Yes | Yes | Yes |
| {ok\_bulb} only | Yes | No | Not a diagnosis |

The most likely fault is the **switch**: one broken part explains both symptoms. An electrician would check it first.

**Consistency:** a KB is **consistent** if false cannot be derived. Diagnosis restores consistency by deciding which assumptions to drop.

**Real world:** car on-board diagnostics (OBD) finding the faulty sensor, network management tools locating a failed router, spacecraft fault detection (NASA used this approach).

## Chapter 09 — Planning with Certainty

**In one line:** planning means finding a **sequence of actions** that turns the current state into a goal state, when every action's effect is known for sure.

**"With certainty"** means: the agent knows the current state exactly, and each action always does what it is supposed to. (Uncertainty comes in Chapter 10.)

**Analogy:** planning to cook rice: wash the rice → add water → turn on the cooker → wait. Each step needs something to be true first (you can't cook before adding water) and changes the kitchen in a known way.

### 9.1 Action Semantics

Action semantics = **what an action means**: when it can be done, and how it changes the world.

- **State-based view:** a transition function RESULT(state, action) = next state. Simple, but you'd have to list every state — impossible for big worlds.
- **Feature-based view:** describe the world by **features** (variables), e.g. RobotLocation = office, HasCoffee = false. An action changes only a few features.

**The frame problem:** when an action happens, what *doesn't* change? Moving a robot doesn't change the colour of the walls, but we don't want to write that for every action. **STRIPS assumption:** any feature an action doesn't mention **stays the same**.

### 9.2 Action Representations (STRIPS)

Each action is described by:

| Part | Meaning | Analogy |
| --- | --- | --- |
| **Preconditions** | What must be true before the action can be done | You need a ticket to board a bus |
| **Action** | The name of the operation | Board the bus |
| **Effects** | What becomes true or false after it (add list / delete list) | You are now on the bus; you're no longer at the stop |

**Running example — a coffee-delivery robot.**

Features: **At** (kitchen / office), **HasCoffee** (T / F), **Delivered** (T / F).

| Action | Preconditions | Effects |
| --- | --- | --- |
| go\_kitchen | At = office | At = kitchen |
| go\_office | At = kitchen | At = office |
| pick\_coffee | At = kitchen, HasCoffee = F | HasCoffee = T |
| deliver | At = office, HasCoffee = T | Delivered = T, HasCoffee = F |

- **Initial state:** At = office, HasCoffee = F, Delivered = F.
- **Goal:** Delivered = T.

### 9.3 Forward Planning

**Idea:** treat planning as **state-space search**. Start from the initial state, apply every action whose preconditions hold, and search (BFS, A\*, …) until a state satisfies the goal.

```
Initial State   {office, no coffee, not delivered}
     ↓  go_kitchen
 {kitchen, no coffee, not delivered}
     ↓  pick_coffee
 {kitchen, has coffee, not delivered}
     ↓  go_office
 {office, has coffee, not delivered}
     ↓  deliver
Goal State      {office, no coffee, DELIVERED}
```

**Why the robot can't take shortcuts:** in the initial state, only go\_kitchen is applicable. pick\_coffee needs At = kitchen, and deliver needs HasCoffee = T, so their preconditions fail.

**Forward planning step by step:**

1. Put the initial state in the frontier.
2. Take a state; if it satisfies the goal, return the action path.
3. Otherwise, for each action whose preconditions are true, apply its effects to get a new state.
4. Add new (unseen) states to the frontier; repeat.

**Strengths and weaknesses:**

- Simple, and any search algorithm from Chapters 2–3 can be reused.
- The **branching factor can be huge** — many actions are applicable but irrelevant (a robot could open every door in the building). Good **heuristics** (e.g. "number of goal features not yet satisfied") make it practical.
- The alternative is **regression (backward) planning**: start from the goal and ask "which action could achieve this?" — it only considers relevant actions.

**Real world:**

| Domain | What is planned |
| --- | --- |
| Warehouse robots (e.g. Amazon) | Pick item → move → place on shelf |
| Mars rovers | Drive, take sample, send data, within battery limits |
| Video-game AI | Enemy characters plan "find weapon → take cover → attack" |
| Logistics | Load trucks, route deliveries, unload |
| Manufacturing | The order of assembly steps on a production line |

## Chapter 10 — Reasoning with Uncertainty

**In one line:** the real world is uncertain, so agents use **probability** to measure how much they believe something and to choose actions that work best on average.

**Why logic isn't enough:** the rule "toothache → cavity" is not always true (it could be gum disease). Instead we say P(cavity | toothache) = 0.8.

### 10.1 Probability

**Basics:**

- **Random variable** — something with uncertain value: Weather ∈ {sunny, rainy, cloudy}.
- **P(A)** — degree of belief that A is true, from 0 (impossible) to 1 (certain).
- **Joint probability P(A, B)** — A and B both true.
- **Conditional probability P(A | B)** — probability of A **given** we know B.

```latex
P(A \mid B) = \frac{P(A, B)}{P(B)}
```

**Product rule:** P(A, B) = P(A | B) × P(B).

**Bayes' rule** — the most important formula in this chapter:

```latex
P(H \mid E) = \frac{P(E \mid H)\, P(H)}{P(E)}
```

**Worked example — a medical test.** A disease affects 1% of people. The test detects it 90% of the time when present, but also gives a false positive 5% of the time.

- P(D) = 0.01, P(+ | D) = 0.90, P(+ | ¬D) = 0.05.
- P(+) = 0.90 × 0.01 + 0.05 × 0.99 = 0.009 + 0.0495 = 0.0585.
- P(D | +) = 0.009 / 0.0585 = **0.154**.

Even after a positive test, there is only about a **15%** chance of having the disease, because the disease is rare. This is why doctors order a second test.

**Real world:** weather forecasts ("70% chance of rain"), spam filters, medical diagnosis, self-driving cars estimating where a pedestrian will move.

### 10.2 Conditional Independence

**Independence:** A and B are independent if knowing one tells you nothing about the other: P(A, B) = P(A) × P(B). *Example:* a coin toss in Dhaka and the weather in Paris.

**Conditional independence:** A and B are independent **once we know C**:

```latex
P(A, B \mid C) = P(A \mid C)\, P(B \mid C)
```

Equivalently, P(A | B, C) = P(A | C): once C is known, B adds no extra information about A.

**Example:** Rahim and Karim both arrive late to class. Their lateness is related (if one is late, the other probably is too). But both are caused by a **traffic jam**. Once you know there was a traffic jam, Rahim being late tells you nothing more about Karim. Rahim-late and Karim-late are **conditionally independent given traffic jam**.

**Why it matters:** a full joint table of n yes/no variables needs 2ⁿ − 1 numbers. Conditional independence lets us break it into small pieces.

### 10.3 Belief Networks (Bayesian Networks)

**A belief network is:**

- **Nodes** — random variables.
- **Directed edges** — direct influence, usually cause → effect.
- **Conditional probability tables (CPTs)** — for each node, P(node | its parents).
- No cycles (a directed acyclic graph, DAG).

The whole joint distribution is the product of the local pieces:

```latex
P(X_1, \dots, X_n) = \prod_{i=1}^{n} P(X_i \mid Parents(X_i))
```

**Worked example — Rain → Traffic Jam → Late to class.**

```
Rain (R)  →  Traffic jam (T)  →  Late (L)
```

| Probability | Value |
| --- | --- |
| P(R) | 0.3 |
| P(T \| R) | 0.8 |
| P(T \| ¬R) | 0.2 |
| P(L \| T) | 0.6 |
| P(L \| ¬T) | 0.1 |

**Joint:** P(R, T, L) = 0.3 × 0.8 × 0.6 = **0.144**.

**Prediction (cause → effect):** how likely is a student to be late on a random day?

- P(T) = 0.3 × 0.8 + 0.7 × 0.2 = 0.38.
- P(L) = 0.38 × 0.6 + 0.62 × 0.1 = **0.29**.

**Diagnosis (effect → cause):** a student was late. How likely is it that it rained?

- P(L | R) = 0.8 × 0.6 + 0.2 × 0.1 = 0.50.
- P(R | L) = 0.50 × 0.3 / 0.29 = **0.52**.

Seeing the student late raises our belief in rain from 30% to 52%. This is **probabilistic reasoning**.

**Saving space:** with 30 binary variables, the full joint table needs about 1 billion numbers. If each node has at most 5 parents, the network needs at most 30 × 2⁵ = 960 numbers.

**Real world:** medical diagnosis systems, fault diagnosis in printers (Microsoft's Windows troubleshooters used them), risk assessment, credit scoring.

### 10.4 Properties of Conditional Independence

In a belief network, **three basic patterns** decide when information flows between two nodes:

| Pattern | Shape | Example | Independent? |
| --- | --- | --- | --- |
| Chain | A → B → C | Rain → Traffic → Late | A and C are dependent; **independent given B** |
| Common cause (fork) | A ← B → C | Rahim-late ← Traffic → Karim-late | A and C are dependent; **independent given B** |
| Common effect (collider) | A → B ← C | Burglary → Alarm ← Earthquake | A and C are **independent**; they become **dependent given B** |

**Explaining away (the collider case):** burglaries and earthquakes have nothing to do with each other. But if the alarm rings *and* you hear on the radio that there was an earthquake, the earthquake **explains away** the alarm, so the chance of a burglary goes **down**.

**General rule:** each node is conditionally independent of its **non-descendants** given its **parents**. This is what lets us multiply small CPTs.

**Other useful properties:**

- **Symmetry:** if A is independent of B given C, then B is independent of A given C.
- **Decomposition:** if A is independent of {B, D} given C, then A is independent of B given C.

### 10.5 Bayesian Learning

**Idea:** treat learning as **updating beliefs** with Bayes' rule as data arrives.

```latex
\underbrace{P(h \mid data)}_{posterior} \propto \underbrace{P(data \mid h)}_{likelihood} \times \underbrace{P(h)}_{prior}
```

| Term | Meaning | Analogy |
| --- | --- | --- |
| Prior P(h) | Belief before seeing data | First impression of a new restaurant |
| Likelihood P(data \| h) | How well hypothesis h explains the data | How well "it's good" fits the reviews you read |
| Posterior P(h \| data) | Updated belief after the data | Your opinion after reading reviews |

**Worked example — is the coin fair?** Two hypotheses: **fair** (P(heads) = 0.5) or **biased** (P(heads) = 0.8). Prior: 50% each. We toss and see **H, H, H**.

| Hypothesis | Prior | Likelihood of HHH | Prior × likelihood | Posterior |
| --- | --- | --- | --- | --- |
| Fair | 0.5 | 0.5³ = 0.125 | 0.0625 | 0.0625 / 0.3185 = **0.20** |
| Biased | 0.5 | 0.8³ = 0.512 | 0.256 | 0.256 / 0.3185 = **0.80** |

After three heads, we believe the coin is biased with 80% probability. More tosses would update it further — **today's posterior becomes tomorrow's prior**.

**Real world:** Naive Bayes spam filters update word probabilities as you mark emails as spam; A/B testing on websites; "Bayesian search" used to locate lost submarines and aircraft wreckage, such as Air France flight 447.

### 10.6 Learning Belief Networks

There are two things to learn: the **parameters** (the numbers in the CPTs) and the **structure** (which arrows exist).

| Situation | How to learn |
| --- | --- |
| Structure known, data complete | **Count frequencies.** P(T \| R) = (days with rain and jam) / (days with rain) |
| Structure known, some data missing or hidden | **EM algorithm**: guess the missing values, re-estimate the CPTs, repeat |
| Structure unknown | **Structure search**: try adding/removing/reversing arrows; keep the network with the best score (fit to data minus a penalty for complexity) |

**Counting example:** in 100 days of records, it rained on 30 days, and on 24 of those there was a traffic jam.

- P(R) = 30 / 100 = 0.3
- P(T | R) = 24 / 30 = 0.8

**Laplace (add-one) smoothing:** if some combination never appeared (count 0), add 1 to every count so we never assign probability exactly 0. *Example:* 0 jams in 5 sunny holidays → instead of 0/5, use (0 + 1) / (5 + 2) ≈ 0.14.

### 10.7 Markov Decision Process (MDP)

**Idea:** a model for **sequential decisions under uncertainty**: actions have random outcomes, and the agent wants to maximise total reward over time.

| Part | Symbol | Meaning |
| --- | --- | --- |
| States | S | Situations the agent can be in |
| Actions | A | What the agent can do |
| Transition probabilities | P(s′ \| s, a) | Chance of landing in s′ after doing a in s |
| Rewards | R(s, a, s′) | Immediate gain or cost |
| Discount factor | γ (0 to 1) | How much future rewards count (γ = 0.9 means a reward next step is worth 90%) |
| Policy | π(s) | The rule: which action to take in each state |

**Markov property:** the future depends only on the **current state**, not on how you got there.

**Bellman equation (optimal value):**

```latex
V^*(s) = \max_a \sum_{s'} P(s' \mid s, a)\,\big[R(s, a, s') + \gamma V^*(s')\big]
```

**Worked example — a racing car.** States: Cool, Warm, Overheated (game over). γ = 0.9.

| State | Action | Outcome | Reward |
| --- | --- | --- | --- |
| Cool | slow | Cool (100%) | +1 |
| Cool | fast | Cool (50%) or Warm (50%) | +2 |
| Warm | slow | Cool (50%) or Warm (50%) | +1 |
| Warm | fast | Overheated (100%) | −10 |

**Value iteration** (start with all V = 0):

| Iteration | V(Cool) | V(Warm) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | max(slow 1, fast 2) = **2** | max(slow 1, fast −10) = **1** |
| 2 | max(slow 1 + 0.9×2 = 2.8, fast 2 + 0.9×(0.5×2 + 0.5×1) = 3.35) = **3.35** | max(slow 1 + 0.9×1.5 = 2.35, fast −10) = **2.35** |

**Policy so far:** when Cool → go **fast**; when Warm → go **slow**. That matches common sense.

**Real world:** robot navigation with slippery wheels, inventory management (how much stock to order), treatment planning in medicine, and the foundation of reinforcement learning (Chapter 11).

### 10.8 Hidden Markov Model (HMM)

**Idea:** the true state is **hidden**; we only see **observations** that depend on it. The hidden state changes over time following a Markov chain.

| Part | Meaning | Umbrella example |
| --- | --- | --- |
| Hidden states | What we want to know | Weather: Rain or Sun |
| Observations | What we can see | Your friend carries an umbrella or not |
| Transition probabilities P(Xₜ \| Xₜ₋₁) | How the hidden state changes | P(Rain today \| Rain yesterday) = 0.7 |
| Emission probabilities P(Eₜ \| Xₜ) | How observations depend on the state | P(umbrella \| Rain) = 0.9, P(umbrella \| Sun) = 0.2 |
| Initial distribution | Belief on day 0 | P(Rain) = 0.5 |

**Story:** you work in a windowless lab. Every morning you see whether your friend brings an umbrella and try to guess the weather outside.

**Filtering (forward algorithm) by hand:**

**Day 1 — umbrella seen:**

- Rain: 0.5 × 0.9 = 0.45; Sun: 0.5 × 0.2 = 0.10.
- Normalise: P(Rain) = 0.45 / 0.55 = **0.82**.

**Day 2 — umbrella seen again:**

- Predict: P(Rain₂) = 0.82 × 0.7 + 0.18 × 0.3 = 0.63; P(Sun₂) = 0.37.
- Update: Rain 0.63 × 0.9 = 0.564; Sun 0.37 × 0.2 = 0.075.
- Normalise: P(Rain) = 0.564 / 0.639 = **0.88**.

Two umbrella days in a row make us more confident it is raining.

**Three classic HMM problems:**

1. **Evaluation** — how likely is this observation sequence? (forward algorithm)
2. **Decoding** — what is the most likely hidden state sequence? (Viterbi algorithm)
3. **Learning** — estimate the transition and emission probabilities from data (Baum–Welch / EM).

**Real world:** speech recognition (hidden = words, observed = sound), part-of-speech tagging (hidden = noun/verb, observed = words), gene finding in DNA, GPS map-matching (hidden = actual road, observed = noisy GPS points).

**MDP vs HMM:**

|  | MDP | HMM |
| --- | --- | --- |
| State visible? | Yes | No (hidden) |
| Agent takes actions? | Yes | No, it only observes |
| Main question | What should I do? | What is really happening? |

## Chapter 11 — Reinforcement Learning

**In one line:** the agent learns **by trial and error** — it tries actions, receives rewards or penalties, and gradually learns which actions lead to the most total reward.

**Analogy:** training a dog. Nobody tells the dog the rule "sit means sit". It tries things, gets a treat when it sits on command, and learns. Or learning to ride a bicycle: falling is a penalty, staying up is a reward.

### 11.1 Basic Reinforcement Learning

```
Agent
  ↓  chooses Action a
Environment
  ↓  returns Reward r and New State s′
Agent learns (updates its values / policy)
  ↓
repeat from the new state
```

RL is an **MDP (Chapter 10.7) where the agent does not know** the transition probabilities or the rewards in advance. It must discover them by acting.

| Term | Meaning | Example: a robot learning to walk |
| --- | --- | --- |
| Agent | The learner / decision-maker | The robot's controller |
| Environment | Everything the agent interacts with | Floor, gravity, obstacles |
| State s | The current situation | Joint angles, balance |
| Action a | What the agent does | Move left leg forward |
| Reward r | Immediate feedback (number) | +1 for each step forward, −100 for falling |
| Policy π | Strategy: state → action | "When leaning left, step left" |
| Value V(s) / Q(s, a) | Expected total future reward | How good a posture (or posture + move) is |
| Episode | One run from start to end | One walking attempt until it falls or finishes |

**How RL differs from supervised learning:** nobody gives the correct action. The agent only gets a reward, which may come **late** (in chess, you learn only at the end if you won). Working out which earlier moves deserved credit is called the **credit assignment problem**.

### 11.2 Reinforcement Learning Algorithms

| Approach | Idea | Example algorithm |
| --- | --- | --- |
| Model-based | Learn P(s′ \| s, a) and R first, then plan with value iteration | Adaptive dynamic programming |
| Model-free, Monte Carlo | Play a full episode, then update values with the actual total return | Monte Carlo control |
| Model-free, temporal difference (TD) | Update after **every step** using the next state's estimated value | TD(0), SARSA, Q-learning |
| Policy-based | Adjust the policy directly to increase reward | Policy gradient (REINFORCE) |

**TD learning update** (learn from the difference between expectation and reality):

```latex
V(s) \leftarrow V(s) + \alpha\,\big[r + \gamma V(s') - V(s)\big]
```

The part in brackets is the **TD error**: (what actually happened) − (what I expected). *Analogy:* you expect a 30-minute bus ride; after 10 minutes you're stuck in a jam, so you update your estimate immediately instead of waiting until you arrive.

**SARSA vs Q-learning:**

|  | SARSA (on-policy) | Q-learning (off-policy) |
| --- | --- | --- |
| Learns the value of | The policy it actually follows (including exploration) | The best (greedy) policy |
| Update uses | Q(s′, a′) for the action really taken next | max over a′ of Q(s′, a′) |
| Behaviour near danger | Safer: accounts for its own random mistakes | Bolder: assumes it will act optimally |

### 11.3 Exploration vs Exploitation

- **Exploration** — try something new to discover whether it is better.
- **Exploitation** — use the action already known to give good results.

**Analogy — lunch near campus:** you know the kacchi place gives you a good meal (exploit). But the new restaurant next door might be even better (explore). If you only exploit, you may never find the best place. If you only explore, you keep eating mediocre food.

**ε-greedy strategy (most common):**

- With probability **1 − ε**, choose the best known action (exploit).
- With probability **ε**, choose a random action (explore).
- *Example:* ε = 0.1 → 90% of the time take the best action, 10% try something random.
- Often ε starts high (e.g. 1.0) and **decays** over time: explore a lot early, exploit later.

**Other strategies:** optimistic initial values (start by assuming every action is great, so the agent tries them all), softmax/Boltzmann selection (better actions are chosen with higher probability), and UCB (try actions you are uncertain about).

**Real world:** YouTube and Netflix mostly show what you like (exploit) but sometimes slip in new content (explore); online ads; clinical trials testing new treatments.

### 11.4 Q-Learning

**Idea:** learn a table **Q(s, a)** = the expected total future reward of doing action a in state s and acting optimally afterwards. Once learned, the best policy is simply: in each state, pick the action with the highest Q.

**Q-learning update rule:**

```latex
Q(s,a) \leftarrow Q(s,a) + \alpha\,\big[\,r + \gamma \max_{a'} Q(s',a') - Q(s,a)\,\big]
```

- α = learning rate (how much new information overrides old).
- γ = discount factor (how much future rewards count).
- r + γ max Q(s′, a′) = the **target** (reward now + best future value).

**Algorithm:**

1. Initialise Q(s, a) = 0 for all states and actions.
2. For each episode, start in an initial state s.
3. Choose action a with ε-greedy.
4. Take a; observe reward r and next state s′.
5. Update Q(s, a) with the rule above.
6. s ← s′; repeat until the episode ends.

**One-step example:** Q(s, a) = 2, α = 0.5, γ = 0.9, r = 5, max Q(s′, a′) = 4.

- Target = 5 + 0.9 × 4 = 8.6
- TD error = 8.6 − 2 = 6.6
- New Q(s, a) = 2 + 0.5 × 6.6 = **5.3**

**Worked example — a corridor.** States A → B → C (C is the goal). Moving right gives −1, except reaching C gives +10. α = 0.5, γ = 0.9, all Q start at 0. The agent moves right each time.

| Episode | Transition | Calculation | New value |
| --- | --- | --- | --- |
| 1 | A → B, r = −1 | 0 + 0.5 × (−1 + 0.9 × 0 − 0) | Q(A, right) = −0.5 |
| 1 | B → C, r = +10 | 0 + 0.5 × (10 + 0 − 0) | Q(B, right) = 5 |
| 2 | A → B, r = −1 | −0.5 + 0.5 × (−1 + 0.9 × 5 − (−0.5)) | Q(A, right) = 1.5 |
| 2 | B → C, r = +10 | 5 + 0.5 × (10 + 0 − 5) | Q(B, right) = 7.5 |

**What to notice:** in episode 1, A looked bad (−0.5) because the agent hadn't yet seen that B leads to the goal. In episode 2, the goal's reward **flowed backwards** to A (1.5). With more episodes, Q values converge to the true values.

**Why Q-learning is popular:**

- **Model-free** — no need to know transition probabilities.
- **Off-policy** — it learns the optimal policy even while exploring randomly.
- Guaranteed to converge to the optimal Q (for small tabular problems) if every state–action pair is tried enough and α decreases suitably.

**Limitation and the fix:** a Q-table is impossible for huge state spaces (a game screen has millions of pixel combinations). **Deep Q-Networks (DQN)** replace the table with a neural network (Chapter 7) that estimates Q; DeepMind used this to play Atari games from raw pixels.

**Real world:**

| Application | State | Action | Reward |
| --- | --- | --- | --- |
| AlphaGo / game AI | Board position | Move | Win = +1, lose = −1 |
| Robot arm grasping | Camera image, joint angles | Motor commands | +1 for a successful grasp |
| Traffic-light control | Queue length at each road | Change light phase | −(total waiting time) |
| Data-centre cooling (Google DeepMind) | Temperatures, loads | Cooling settings | −(energy used) |
| Chatbots (RLHF) | Conversation so far | Next response | Human preference score |

### Big picture: how the chapters connect

| Chapter | The agent's question |
| --- | --- |
| 1 Agents | What am I and what is my environment? |
| 2–3 Search | Which path reaches the goal? |
| 4 Metaheuristics | Which solution is good enough, fast? |
| 5 Adversarial search | What if someone is playing against me? |
| 6 CSP | Which assignment satisfies all the rules? |
| 7 Learning | How can I learn patterns from data? |
| 8 Knowledge base | What can I conclude from what I know? |
| 9 Planning | Which sequence of actions reaches my goal? |
| 10 Uncertainty | What should I believe and do when unsure? |
| 11 Reinforcement learning | How do I learn to act well from rewards? |
