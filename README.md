# Artificial Intelligence (CSE366) — Comprehensive Course Handbook & Study Guide

<p align="center">
  <img src="https://img.shields.io/badge/Course-CSE366%20Artificial%20Intelligence-blue?style=for-the-badge&logo=openai&logoColor=white" alt="Course Badge" />
  <img src="https://img.shields.io/badge/Status-Complete%20Study%20Guide-success?style=for-the-badge&logo=gitbook&logoColor=white" alt="Status Badge" />
  <img src="https://img.shields.io/badge/Python-3.8%2B%20Implementations-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  <img src="https://img.shields.io/badge/Diagrams-Interactive%20Mermaid%20Visuals-8A2BE2?style=for-the-badge&logo=diagramsdotnet&logoColor=white" alt="Diagrams Badge" />
  <img src="https://img.shields.io/badge/Exam%20Prep-High%20Yield%20Traces%20%26%20Tips-red?style=for-the-badge&logo=target&logoColor=white" alt="Exam Prep Badge" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" alt="License Badge" />
</p>

---

## 📖 Welcome & Overview

Welcome to the **complete, student-first course companion for CSE366 (Artificial Intelligence)**. This handbook distills every major topic across the 11 core chapters into plain English, intuitive visual diagrams, step-by-step mathematical derivations, exam-proven tracing tables, and runnable Python implementations.

### 🎯 How to Use These Notes

1. **Read the "In One Line" summary first:** Grasp the core philosophy and objective before diving into mechanics.
2. **Follow the Worked Examples & Traces:** Midterms and finals prioritize manual step-by-step traces (e.g., BFS/A\* queues,
   $\alpha$ - $\beta$ cutoffs, CPT joint distributions, Q-learning value tables).
4. **Inspect the Interactive Diagrams:** Every algorithm and concept includes a color-coded Mermaid diagram with clear state transitions.
5. **Inspect the Python Snippets:** Cement your conceptual understanding with concise, dependency-free reference code.
6. **Leverage the Quick Reference Tables:** Use the algorithm comparison and complexity matrices right before your exams.
7. **Solve the Practice Flash Questions:** Test your active recall at the end of each chapter.

> [!NOTE]
> **The Running Real-World Example:**
> A **food-delivery rider in Dhaka** (navigating between Dhanmondi, Gulshan, and Mirpur) appears across chapters. It illustrates how one agent can use **search** to route, **heuristics** to estimate distances, **game theory** to outsmart competition, **logic** to troubleshoot bike issues, **probability** to manage traffic delays, and **reinforcement learning** to discover optimal delivery strategies.

---

## 🗺️ Interactive Visual Course Roadmap

```mermaid
flowchart TD
    subgraph Part1 [1. Foundations & Search]
        C1["01. Agents & Environments"]
        C2["02. Uninformed Search (BFS, DFS, UCS, IDS)"]
        C3["03. Informed Search (Greedy, A*, IDA*)"]
        C4["04. Metaheuristics (Hill Climbing, GA, SA)"]
        C1 --> C2 --> C3 --> C4
    end

    subgraph Part2 [2. Adversarial & Structured Reasoning]
        C5["05. Adversarial Search (Minimax, Alpha-Beta)"]
        C6["06. Constraint Satisfaction (CSP & AC-3)"]
        C8["08. Knowledge Bases & Logic (Definite Clauses)"]
        C9["09. Classical Planning (STRIPS Action Models)"]
        C4 --> C5 --> C6 --> C8 --> C9
    end

    subgraph Part3 [3. Uncertainty & Learning]
        C10["10. Reasoning Under Uncertainty (Bayes, BN, MDP, HMM)"]
        C7["07. Machine Learning & Neural Networks"]
        C11["11. Reinforcement Learning (Q-Learning & SARSA)"]
        C9 --> C10
        C10 --> C7
        C10 --> C11
    end

    classDef fnd fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a;
    classDef dec fill:#f3e8ff,stroke:#9333ea,stroke-width:2px,color:#581c87;
    classDef lrn fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;
    class C1,C2,C3,C4 fnd;
    class C5,C6,C8,C9 dec;
    class C7,C10,C11 lrn;
```

---

## 📑 Table of Contents

- [Chapter 01 — Artificial Intelligence and Agents](#chapter-01--artificial-intelligence-and-agents)
  - [1.1 Introduction to Artificial Intelligence](#11-introduction-to-artificial-intelligence)
  - [1.2 Agents & Environments (PEAS Framework)](#12-agents--environments-peas-framework)
  - [1.3 Agent Architectures & Hierarchical Control](#13-agent-architectures--hierarchical-control)
  - [Chapter 1 Quick Check](#chapter-1-quick-check)
- [Chapter 02 — Uninformed Search](#chapter-02--uninformed-search)
  - [2.1 Search Graph Formulation](#21-search-graph-formulation)
  - [2.2 Breadth-First Search (BFS)](#22-breadth-first-search-bfs)
  - [2.3 Depth-First Search (DFS)](#23-depth-first-search-dfs)
  - [2.4 Uniform Cost Search (UCS)](#24-uniform-cost-search-ucs)
  - [2.5 Depth-Limited (DLS) & Iterative Deepening (IDS)](#25-depth-limited-dls--iterative-deepening-ids)
  - [2.6 Bidirectional Search](#26-bidirectional-search)
  - [2.7 Python Reference: Uninformed Search Algorithms](#27-python-reference-uninformed-search-algorithms)
  - [Chapter 2 Quick Check](#chapter-2-quick-check)
- [Chapter 03 — Informed (Heuristic) Search](#chapter-03--informed-heuristic-search)
  - [3.1 Heuristic Functions, Admissibility & Consistency](#31-heuristic-functions-admissibility--consistency)
  - [3.2 Greedy Best-First Search](#32-greedy-best-first-search)
  - [3.3 A\* Search](#33-a-search)
  - [3.4 IDA\* (Iterative Deepening A\*)](#34-ida-iterative-deepening-a)
  - [3.5 Python Reference: A\* Search Engine](#35-python-reference-a-search-engine)
  - [Chapter 3 Quick Check](#chapter-3-quick-check)
- [Chapter 04 — Metaheuristic Algorithms](#chapter-04--metaheuristic-algorithms)
  - [4.1 Hill Climbing & Landscape Hazards](#41-hill-climbing--landscape-hazards)
  - [4.2 Hill Climbing Variations](#42-hill-climbing-variations)
  - [4.3 Simulated Annealing](#43-simulated-annealing)
  - [4.4 Genetic Algorithms (GA)](#44-genetic-algorithms-ga)
  - [4.5 Differential Evolution (DE)](#45-differential-evolution-de)
  - [4.6 Gradient Descent](#46-gradient-descent)
  - [4.7 Python Reference: Optimization in Action](#47-python-reference-optimization-in-action)
  - [Chapter 4 Quick Check](#chapter-4-quick-check)
- [Chapter 05 — Adversarial Search & Games](#chapter-05--adversarial-search--games)
  - [5.1 Game Formulations & Game Trees](#51-game-formulations--game-trees)
  - [5.2 The Minimax Algorithm](#52-the-minimax-algorithm)
  - [5.3 Alpha-Beta Pruning ($\alpha$-$\beta$)](#53-alpha-beta-pruning-)
  - [5.4 Python Reference: Minimax & Alpha-Beta Engine](#54-python-reference-minimax--alpha-beta-engine)
  - [Chapter 5 Quick Check](#chapter-5-quick-check)
- [Chapter 06 — Constraint Satisfaction Problems (CSPs)](#chapter-06--constraint-satisfaction-problems-csps)
  - [6.1 CSP Formalism & Constraint Graphs](#61-csp-formalism--constraint-graphs)
  - [6.2 Constraint Propagation: Forward Checking & AC-3](#62-constraint-propagation-forward-checking--ac-3)
  - [6.3 Backtracking Search with MRV, Degree & LCV](#63-backtracking-search-with-mrv-degree--lcv)
  - [6.4 Python Reference: CSP Solver](#64-python-reference-csp-solver)
  - [Chapter 6 Quick Check](#chapter-6-quick-check)
- [Chapter 07 — Learning in AI & Neural Networks](#chapter-07--learning-in-ai--neural-networks)
  - [7.1 Foundations of Machine Learning](#71-foundations-of-machine-learning)
  - [7.2 Artificial Neural Networks & Activation Functions](#72-artificial-neural-networks--activation-functions)
  - [7.3 The Backpropagation Algorithm](#73-the-backpropagation-algorithm)
  - [7.4 Python Reference: Neural Network Forward & Backprop Pass](#74-python-reference-neural-network-forward--backprop-pass)
  - [Chapter 7 Quick Check](#chapter-7-quick-check)
- [Chapter 08 — Knowledge Bases & Logic](#chapter-08--knowledge-bases--logic)
  - [8.1 Propositional Logic & Models](#81-propositional-logic--models)
  - [8.2 Definite Clauses & Horn Clauses](#82-definite-clauses--horn-clauses)
  - [8.3 Proof Procedures: Forward & Backward Chaining](#83-proof-procedures-forward--backward-chaining)
  - [8.4 Ask-the-User & Knowledge-Level Debugging](#84-ask-the-user--knowledge-level-debugging)
  - [8.5 Consistency-Based Diagnosis & Minimal Conflicts](#85-consistency-based-diagnosis--minimal-conflicts)
  - [8.6 Python Reference: Forward Chaining Engine](#86-python-reference-forward-chaining-engine)
  - [Chapter 8 Quick Check](#chapter-8-quick-check)
- [Chapter 09 — Classical Planning with Certainty](#chapter-09--classical-planning-with-certainty)
  - [9.1 Action Representations & The STRIPS Assumption](#91-action-representations--the-strips-assumption)
  - [9.2 Forward State-Space Planning vs Backward Planning](#92-forward-state-space-planning-vs-backward-planning)
  - [9.3 Python Reference: STRIPS Planning Engine](#93-python-reference-strips-planning-engine)
  - [Chapter 9 Quick Check](#chapter-9-quick-check)
- [Chapter 10 — Reasoning Under Uncertainty](#chapter-10--reasoning-under-uncertainty)
  - [10.1 Probability Basics & Bayes' Rule](#101-probability-basics--bayes-rule)
  - [10.2 Conditional Independence & Network Topologies](#102-conditional-independence--network-topologies)
  - [10.3 Bayesian Belief Networks (BBN)](#103-bayesian-belief-networks-bbn)
  - [10.4 Bayesian Parameter Learning](#104-bayesian-parameter-learning)
  - [10.5 Markov Decision Processes (MDPs) & The Bellman Equation](#105-markov-decision-processes-mdps--the-bellman-equation)
  - [10.6 Hidden Markov Models (HMMs)](#106-hidden-markov-models-hmms)
  - [10.7 Python Reference: Bayesian & HMM Computing](#107-python-reference-bayesian--hmm-computing)
  - [Chapter 10 Quick Check](#chapter-10-quick-check)
- [Chapter 11 — Reinforcement Learning (RL)](#chapter-11--reinforcement-learning-rl)
  - [11.1 The Reinforcement Learning Paradigm](#111-the-reinforcement-learning-paradigm)
  - [11.2 Passive vs Active RL, TD-Learning & SARSA](#112-passive-vs-active-rl-td-learning--sarsa)
  - [11.3 Exploration vs Exploitation ($\epsilon$-Greedy)](#113-exploration-vs-exploitation--greedy)
  - [11.4 Q-Learning (Off-Policy TD Control)](#114-q-learning-off-policy-td-control)
  - [11.5 Python Reference: Tabular Q-Learning Engine](#115-python-reference-tabular-q-learning-engine)
  - [Chapter 11 Quick Check](#chapter-11-quick-check)
- [🏆 Master Exam Cheat Sheet & Formulas](#-master-exam-cheat-sheet--formulas)

---

## Chapter 01 — Artificial Intelligence and Agents

> **In One Line:** AI builds rational agents that perceive their environment through sensors, reason over internal models, and act through actuators to maximize performance.

### 1.1 Introduction to Artificial Intelligence

Artificial Intelligence (AI) designs computational systems capable of performing tasks typically requiring human intelligence: reasoning, visual perception, natural language understanding, learning, and planning.

```mermaid
flowchart LR
    P["👁️ Perception<br>(Sensory Input)"] --> R["🗺️ Representation<br>(Graph/Logic/Prob)"]
    R --> D["🧠 Reasoning & Search<br>(Decision Making)"]
    D --> L["📈 Learning<br>(Experience Update)"]
    L --> A["🦾 Action<br>(Actuators/Output)"]

    classDef step fill:#f0f9ff,stroke:#0284c7,stroke-width:2px,color:#0369a1;
    class P,R,D,L,A step;
```

#### Core Foundational Pillars
1. **Representation:** Modeling facts, constraints, and relationships in computational structures (graphs, trees, logic clauses).
2. **Search:** Exploring prospective action trajectories to locate goal states.
3. **Reasoning:** Deriving logically sound inferences from existing knowledge.
4. **Learning:** Refining decision policies automatically from experiential data.
5. **Handling Uncertainty:** Making optimal decisions despite noisy, incomplete, or stochastic environments.

---

### 1.2 Agents & Environments (PEAS Framework)

An **agent** interacts with an **environment** in a continuous closed loop:

```mermaid
flowchart TD
    Env(["🌍 Environment (World / State)"]) -->|Percepts / Raw Signals| Sensors["👁️ Sensors (Cameras, GPS, LiDAR)"]
    Sensors --> AgentBrain["🧠 Agent Function: f(P*) to Actions"]
    AgentBrain --> Actuators["🦾 Actuators (Motors, Steering, Display)"]
    Actuators -->|Actions / Interventions| Env

    classDef envStyle fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f;
    classDef sensStyle fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0369a1;
    classDef brainStyle fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#4c1d95;
    classDef actStyle fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;

    class Env envStyle;
    class Sensors sensStyle;
    class AgentBrain brainStyle;
    class Actuators actStyle;
```

- **Percept:** The current sensory input at one instance.
- **Percept Sequence ($P^*$):** The complete history of all sensory inputs received to date.
- **Agent Function:** An abstract mathematical mapping from percept sequences to actions ($f: P^* \rightarrow A$).
- **Agent Program:** The concrete software implementation executing the agent function on a physical architecture.

#### PEAS Framework (Performance, Environment, Actuators, Sensors)

| System | Performance Measure (P) | Environment (E) | Actuators (A) | Sensors (S) |
| :--- | :--- | :--- | :--- | :--- |
| **Pathao / Uber Driver Agent** | Fast trip, safety, fuel efficiency, passenger rating | Dhaka roads, pedestrians, traffic jams, weather | Steering, throttle, brake, horn, app UI | GPS, camera, speedometer, accelerometer |
| **Medical Diagnostic Agent** | Diagnostic accuracy, minimized cost/risk, speed | Patient records, symptoms, lab test results | Screen display, prescription generation | Keyboard input, lab feed, EHR database |
| **Autonomous Vacuum Cleaner** | Cleanliness, energy usage, minimal wear, low noise | Rooms, carpet/tiles, furniture, stairs | Wheels, brushes, suction motor | Bump switch, infrared cliff sensor, dirt sensor |

#### Environmental Dimensions & Taxonomies

```mermaid
flowchart LR
    EnvDim["🌐 Environment Dimensions"] --> Obs["Observability: Fully vs Partially"]
    EnvDim --> Det["Determinism: Deterministic vs Stochastic"]
    EnvDim --> Ep["Episodicity: Episodic vs Sequential"]
    EnvDim --> Dyn["Dynamism: Static vs Dynamic"]
    EnvDim --> Val["Continuity: Discrete vs Continuous"]
    EnvDim --> Ag["Agents: Single-Agent vs Multi-Agent"]

    classDef main fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#4c1d95;
    classDef branch fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#334155;
    class EnvDim main;
    class Obs,Det,Ep,Dyn,Val,Ag branch;
```

| Dimension | Easy Setting | Hard Setting | Real-World Hard Case Example |
| :--- | :--- | :--- | :--- |
| **Observability** | Fully Observable (Chess) | Partially Observable | Poker (hidden opponent hands), Foggy driving |
| **Determinism** | Deterministic (8-Puzzle) | Stochastic | Driving in Dhaka traffic (unpredictable actors) |
| **Episodicity** | Episodic (Image classification) | Sequential | Chess (early move impacts endgame survival) |
| **Dynamism** | Static (Crossword) | Dynamic | Stock trading (market moves while agent computes) |
| **Continuity** | Discrete (Tic-Tac-Toe) | Continuous | Steering wheel angles, robotic arm velocities |
| **Multi-Agent** | Single-Agent (Sudoku) | Multi-Agent | Football match, autonomous drone fleet collision avoidance |

---

### 1.3 Agent Architectures & Hierarchical Control

```mermaid
flowchart LR
    A1["1. Simple Reflex<br>(Condition-Action)"] --> A2["2. Model-Based<br>(Internal Memory)"]
    A2 --> A3["3. Goal-Based<br>(Target Directed)"]
    A3 --> A4["4. Utility-Based<br>(Happiness Score)"]
    A4 --> A5["5. Learning Agent<br>(Self-Improving)"]

    classDef arch fill:#f1f5f9,stroke:#475569,stroke-width:2px,color:#0f172a;
    class A1,A2,A3,A4,A5 arch;
```

1. **Simple Reflex Agent:** Fires condition-action rules purely based on current percept (no memory).
2. **Model-Based Reflex Agent:** Maintains internal state tracking unobserved aspects of the world.
3. **Goal-Based Agent:** Combines state information with goal descriptions to select path-finding actions.
4. **Utility-Based Agent:** Uses a continuous utility function ($U: S \rightarrow \mathbb{R}$) to trade off competing goals (e.g., speed vs safety).
5. **Learning Agent:** Composed of a *Critic* (evaluates performance), *Learning Element* (makes improvements), *Performance Element* (chooses actions), and *Problem Generator* (suggests exploratory actions).

#### Hierarchical Agent Control Stack

```mermaid
graph TD
    High["Top Layer: Strategic Planner (Minutes/Hours)<br>E.g., Select Route: Dhanmondi to Gulshan"]
    Mid["Middle Layer: Tactical Navigation (Seconds)<br>E.g., Lane changing, overtaking slow rickshaw"]
    Low["Low Layer: Reactive Execution (Milliseconds)<br>E.g., Emergency brake on sudden obstacle"]

    High -->|Route Waypoints| Mid
    Mid -->|Steering / Speed Target| Low
    Low -.->|Telemetry / Bump Status| Mid
    Mid -.->|Traffic Progress / Blockages| High

    classDef l1 fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a;
    classDef l2 fill:#e0e7ff,stroke:#4f46e5,stroke-width:2px,color:#312e81;
    classDef l3 fill:#fce7f3,stroke:#db2777,stroke-width:2px,color:#831843;

    class High l1;
    class Mid l2;
    class Low l3;
```

---

### Chapter 1 Quick Check

<details>
<summary><b>🔍 Self-Check Question 1:</b> What is the difference between an Agent Function and an Agent Program?</summary>

- **Agent Function:** The mathematical abstraction that maps any given percept sequence history to an action ($f: P^* \rightarrow A$).
- **Agent Program:** The concrete software implementation of the agent function running on physical computing architecture.
</details>

<details>
<summary><b>🔍 Self-Check Question 2:</b> Why is an environment classified as dynamic rather than static?</summary>

An environment is **dynamic** if it can change while the agent is deliberating. If the environment does not change with the passage of time during decision-making, it is **static**.
</details>

---

## Chapter 02 — Uninformed Search

> **In One Line:** Blind search algorithms systematically explore state spaces using only state connectivity and transition costs, possessing zero domain-specific knowledge about goal proximity.

### 2.1 Search Graph Formulation

A formal search problem is defined by a 5-tuple:
1. **Initial State ($s_0$):** Starting node.
2. **Actions ($A(s)$):** Legal moves available in state $s$.
3. **Transition Model ($Result(s, a)$):** The state resulting from action $a$ in $s$.
4. **Goal Test ($IsGoal(s)$):** Boolean predicate determining if state is a target.
5. **Path Cost ($c(s, a, s')$):** Step cost $g(n)$ accumulated along the path.

#### Benchmark Graph for Traces

```mermaid
graph LR
    S((S)) -- 1 --> A((A))
    S -- 5 --> B((B))
    A -- 2 --> C((C))
    A -- 6 --> D((D))
    B -- 6 --> G(((G)))
    C -- 9 --> G
    D -- 1 --> G

    classDef startNode fill:#dbeafe,stroke:#2563eb,stroke-width:3px,color:#1e3a8a;
    classDef midNode fill:#f1f5f9,stroke:#64748b,stroke-width:2px,color:#0f172a;
    classDef goalNode fill:#dcfce7,stroke:#16a34a,stroke-width:3px,color:#14532d;

    class S startNode;
    class A,B,C,D midNode;
    class G goalNode;
```

**Alternative Paths & Costs:**
- $S \rightarrow B \rightarrow G$: Cost $= 5 + 6 = 11$
- $S \rightarrow A \rightarrow C \rightarrow G$: Cost $= 1 + 2 + 9 = 12$
- $S \rightarrow A \rightarrow D \rightarrow G$: Cost $= 1 + 6 + 1 = \mathbf{8}$ *(Optimal)*

---

### 2.2 Breadth-First Search (BFS)

- **Mechanism:** Explores shallowest unexplored nodes first using a **FIFO Queue**.
- **Goal Test Timing:** Applied when node is **generated**.
- **Properties:** Complete (if branching factor $b$ is finite). Optimal if and only if all step costs are identical.
- **Time Complexity:** $O(b^d)$, **Space Complexity:** $O(b^d)$ (where $d$ is goal depth).

```mermaid
graph TD
    subgraph Level0 [Depth 0]
        S["S"]
    end
    subgraph Level1 [Depth 1]
        A["A"]
        B["B"]
    end
    subgraph Level2 [Depth 2]
        C["C"]
        D["D"]
        G["G (Goal Found!)"]
    end

    S --> A
    S --> B
    A --> C
    A --> D
    B --> G

    classDef active fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;
    class G active;
```

#### Manual Trace on Benchmark Graph

| Step | Expand Node | Frontier FIFO Queue | Notes |
| :---: | :---: | :--- | :--- |
| **1** | $S$ | $[A, B]$ | $S$ expanded; $A, B$ added |
| **2** | $A$ | $[B, C, D]$ | $A$ expanded; $C, D$ added |
| **3** | $B$ | $[C, D, G]$ | **Goal $G$ generated!** Immediate termination |

- **Output Path:** $S \rightarrow B \rightarrow G$ (2 hops, Path Cost $= 11$). Found minimum hops, not minimal cost!

---

### 2.3 Depth-First Search (DFS)

- **Mechanism:** Explores deepest nodes first using a **LIFO Stack** (or recursion).
- **Goal Test Timing:** Applied when node is expanded.
- **Properties:** Not complete in infinite/cyclic state spaces (complete on finite spaces with graph cycle checking). Not optimal.
- **Time Complexity:** $O(b^m)$, **Space Complexity:** $O(b \cdot m)$ (where $m$ is maximum tree depth).

#### Manual Trace (Alphabetical Tie-Breaking)
1. Expand $S \rightarrow$ Stack: $[B, A]$
2. Expand $A \rightarrow$ Stack: $[B, D, C]$
3. Expand $C \rightarrow$ Stack: $[B, D, G]$
4. Expand $G \rightarrow$ **Goal reached!**
- **Output Path:** $S \rightarrow A \rightarrow C \rightarrow G$ (Cost $= 12$).

---

### 2.4 Uniform Cost Search (UCS)

- **Mechanism:** Expands node with the lowest cumulative path cost $g(n)$ using a **Priority Queue (Min-Heap)**. (Dijkstra's search formulation).
- **Goal Test Timing:** Applied when node is **expanded / popped**, NOT when generated!
- **Properties:** Complete (if step costs $\ge \epsilon > 0$). **Optimal** for arbitrary non-negative step costs.
- **Complexity:** Time & Space $O(b^{1 + \lfloor C^* / \epsilon \rfloor})$, where $C^*$ is optimal cost.

#### Manual Step-by-Step Trace

| Step | Node Popped | $g(n)$ | Frontier Priority Queue $\{Node: g(n)\}$ | Explored Set |
| :---: | :---: | :---: | :--- | :--- |
| **1** | $S$ | $0$ | $\{A: 1, B: 5\}$ | $\{S\}$ |
| **2** | $A$ | $1$ | $\{C: 3, B: 5, D: 7\}$ | $\{S, A\}$ |
| **3** | $C$ | $3$ | $\{B: 5, D: 7, G: 12\}$ | $\{S, A, C\}$ |
| **4** | $B$ | $5$ | $\{D: 7, G: 11\}$ *(G updated: $\min(12, 11) = 11$)* | $\{S, A, C, B\}$ |
| **5** | $D$ | $7$ | $\{G: 8\}$ *(G updated: $\min(11, 7+1) = 8$)* | $\{S, A, C, B, D\}$ |
| **6** | $G$ | $\mathbf{8}$ | Goal popped! **Terminate.** | $\{S, A, C, B, D, G\}$ |

- **Output Path:** $S \rightarrow A \rightarrow D \rightarrow G$ (Optimal Cost $= \mathbf{8}$).

---

### 2.5 Depth-Limited (DLS) & Iterative Deepening (IDS)

#### Depth-Limited Search (DLS)
DFS executed with a fixed depth bound $l$. Returns cutoff if depth limit is reached without finding goal.
- Space Complexity: $O(b \cdot l)$. Incomplete if $l < d$.

#### Iterative Deepening Search (IDS)
Repeatedly invokes DLS with incrementally increasing depth limits: $l = 0, 1, 2, \dots, d$.

```
Iteration l=0: [S] (Cutoff)
Iteration l=1: [S -> A], [S -> B] (Cutoff)
Iteration l=2: [S -> A -> C], [S -> A -> D], [S -> B -> G] (Goal Found!)
```

> [!TIP]
> **Why IDS is not wasteful:**
> In exponential search trees, the vast majority of nodes reside at the bottom layer ($d$).
> Total nodes generated in IDS:
> $$N(\text{IDS}) = (d+1)b^0 + d b^1 + (d-1)b^2 + \dots + 1 b^d = O(b^d)$$
> For $b=10, d=5$: BFS generates $111,110$ nodes; IDS generates $123,450$ nodes (only $\approx 11\%$ overhead), while saving massive amounts of RAM: $O(b \cdot d)$ vs $O(b^d)$!

---

### 2.6 Bidirectional Search

Runs two concurrent searches: **Forward** from Initial State and **Backward** from Goal State, terminating when frontiers intersect.

```mermaid
graph LR
    subgraph ForwardSide [Forward Search Frontier: O b^d/2]
        StartNode((Start S)) --> F1((Node F1)) --> MidNode((Intersection))
    end
    subgraph BackwardSide [Backward Search Frontier: O b^d/2]
        MidNode --> B1((Node B1)) --> GoalNode(((Goal G)))
    end

    classDef fwd fill:#dbeafe,stroke:#2563eb,stroke-width:2px;
    classDef bwd fill:#fce7f3,stroke:#db2777,stroke-width:2px;
    classDef meet fill:#dcfce7,stroke:#16a34a,stroke-width:3px;

    class StartNode,F1 fwd;
    class GoalNode,B1 bwd;
    class MidNode meet;
```

$$b^{d/2} + b^{d/2} \ll b^d$$

---

### 2.7 Python Reference: Uninformed Search Algorithms

```python
import heapq
from collections import deque

graph = {
    'S': [('A', 1), ('B', 5)],
    'A': [('C', 2), ('D', 6)],
    'B': [('G', 6)],
    'C': [('G', 9)],
    'D': [('G', 1)],
    'G': []
}

def bfs(start, goal):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.get(node, []):
                queue.append(path + [neighbor])
    return None

def ucs(start, goal):
    # Min-heap stores: (cost, current_node, path)
    heap = [(0, start, [start])]
    visited = {}
    while heap:
        cost, node, path = heapq.heappop(heap)
        if node == goal:
            return path, cost
        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost
        for neighbor, weight in graph.get(node, []):
            heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')

print("BFS Path:", bfs('S', 'G'))          # Output: ['S', 'B', 'G']
print("UCS Path & Cost:", ucs('S', 'G'))   # Output: (['S', 'A', 'D', 'G'], 8)
```

---

### Chapter 2 Quick Check

<details>
<summary><b>🔍 Self-Check Question 1:</b> When must the goal test be applied in Uniform Cost Search (UCS) to guarantee optimality?</summary>

The goal test must be applied when a node is **expanded (popped from priority queue)**, not when generated. Testing upon generation can return suboptimal paths before cheaper alternatives are discovered.
</details>

<details>
<summary><b>🔍 Self-Check Question 2:</b> What search algorithm combines the low space complexity of DFS with the completeness/optimality of BFS?</summary>

**Iterative Deepening Search (IDS)** achieves $O(b \cdot d)$ linear memory with $O(b^d)$ time and guaranteed optimality for uniform step costs.
</details>

---

## Chapter 03 — Informed (Heuristic) Search

> **In One Line:** Informed search utilizes domain-specific heuristics ($h(n)$) to prioritize nodes that appear closest to the goal, drastically pruning the state space.

### 3.1 Heuristic Functions, Admissibility & Consistency

- **Heuristic Function $h(n)$:** Estimated path cost from node $n$ to the nearest goal state ($h(Goal) = 0$).
- **True Remaining Cost $h^*(n)$:** The exact, optimal cost from node $n$ to goal.

```mermaid
flowchart TD
    subgraph HeuristicRules [Heuristic Function Properties]
        Adm["1. Admissibility<br>0 ≤ h(n) ≤ h*(n)<br>(Never overestimates true cost)"]
        Cons["2. Consistency (Monotonicity)<br>h(n) ≤ c(n, a, n') + h(n')<br>(Triangle Inequality)"]
        Dom["3. Dominance<br>h2(n) ≥ h1(n) for all n<br>(h2 expands fewer nodes)"]
    end

    Adm -->|Required for| TreeOpt["Tree Search A* Optimality"]
    Cons -->|Required for| GraphOpt["Graph Search A* Optimality (No Re-opening)"]
    Cons -->|Implies| Adm

    classDef ruleBox fill:#f0fdf4,stroke:#16a34a,stroke-width:2px,color:#14532d;
    classDef optBox fill:#eff6ff,stroke:#2563eb,stroke-width:2px,color:#1e3a8a;

    class Adm,Cons,Dom ruleBox;
    class TreeOpt,GraphOpt optBox;
```

#### Benchmark Heuristic Table for Graph

| Node | $S$ | $A$ | $B$ | $C$ | $D$ | $G$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Heuristic $h(n)$** | $7$ | $6$ | $5$ | $7$ | $1$ | $0$ |
| **True Cost to Goal $h^*(n)$** | $8$ | $7$ | $6$ | $9$ | $1$ | $0$ |

*(All $h(n) \le h^*(n)$, making $h$ admissible & consistent).*

---

### 3.2 Greedy Best-First Search

- **Evaluation Function:** $f(n) = h(n)$ (pure heuristic focus, ignores past path cost $g(n)$).
- **Characteristics:** Fast and goal-directed, but incomplete (can loop in cycles) and **suboptimal**.

#### Trace on Benchmark Graph
1. Expand $S \rightarrow$ Frontier: $\{B: h=5, A: h=6\}$
2. Expand $B \rightarrow$ Frontier: $\{G: h=0, A: h=6\}$
3. Expand $G \rightarrow$ **Goal reached!**
- **Output Path:** $S \rightarrow B \rightarrow G$ (Path Cost $= \mathbf{11}$). Misled by greedily choosing $B$ over $A$.

---

### 3.3 A\* Search

- **Evaluation Function:** $f(n) = g(n) + h(n)$
  - $g(n)$: Exact accumulated cost from start to $n$.
  - $h(n)$: Estimated cost from $n$ to goal.
  - $f(n)$: Estimated total cost of optimal path through $n$.

```mermaid
graph TD
    S["S: g=0, h=7 ⇒ f=7"] --> A["A: g=1, h=6 ⇒ f=7"]
    S --> B["B: g=5, h=5 ⇒ f=10"]
    A --> C["C: g=3, h=7 ⇒ f=10"]
    A --> D["D: g=7, h=1 ⇒ f=8"]
    D --> G["G: g=8, h=0 ⇒ f=8 (OPTIMAL GOAL)"]
    B -.-> BG["G via B: g=11, f=11 (Pruned)"]

    classDef bestPath fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;
    classDef otherPath fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#475569;

    class S,A,D,G bestPath;
    class B,C,BG otherPath;
```

#### Step-by-Step Manual Trace

| Step | Node Expanded | $g(n)$ | $h(n)$ | $f(n)$ | New Successors Generated ($g + h = f$) | Priority Queue Sorted by $f(n)$ |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **1** | $S$ | $0$ | $7$ | $7$ | $A(1+6=7), B(5+5=10)$ | $\{A: 7, B: 10\}$ |
| **2** | $A$ | $1$ | $6$ | $7$ | $C(3+7=10), D(7+1=8)$ | $\{D: 8, B: 10, C: 10\}$ |
| **3** | $D$ | $7$ | $1$ | $8$ | $G(8+0=8)$ | $\{G: 8, B: 10, C: 10\}$ |
| **4** | $G$ | $8$ | $0$ | $\mathbf{8}$ | Goal Popped! **Terminate.** | — |

- **Output Path:** $S \rightarrow A \rightarrow D \rightarrow G$ (Optimal Cost $= \mathbf{8}$).
- **Comparison:** UCS expanded 5 nodes before reaching $G$; A\* expanded only 3!

---

### 3.4 IDA\* (Iterative Deepening A\*)

- **Problem with A\*:** A\* keeps all generated nodes in memory ($O(b^d)$ space bottleneck).
- **IDA\* Solution:** Performs depth-first search bounded by an **$f$-cost threshold** instead of depth.
- **Update Rule:** If goal not found, threshold is increased to the **minimum $f$-value that exceeded the previous limit**.
- **Space Complexity:** $O(b \cdot d)$ (linear memory!).

---

### 3.5 Python Reference: A\* Search Engine

```python
import heapq

graph = {
    'S': [('A', 1), ('B', 5)],
    'A': [('C', 2), ('D', 6)],
    'B': [('G', 6)],
    'C': [('G', 9)],
    'D': [('G', 1)],
    'G': []
}

heuristics = {'S': 7, 'A': 6, 'B': 5, 'C': 7, 'D': 1, 'G': 0}

def a_star_search(start, goal):
    # Heap stores: (f_cost, g_cost, current_node, path)
    frontier = [(heuristics[start], 0, start, [start])]
    explored = {}

    while frontier:
        f, g, node, path = heapq.heappop(frontier)

        if node == goal:
            return path, g

        if node in explored and explored[node] <= g:
            continue
        explored[node] = g

        for neighbor, weight in graph.get(node, []):
            new_g = g + weight
            new_f = new_g + heuristics[neighbor]
            heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

path, cost = a_star_search('S', 'G')
print(f"A* Optimal Path: {path} with Total Cost: {cost}")
# Output: A* Optimal Path: ['S', 'A', 'D', 'G'] with Total Cost: 8
```

---

### Chapter 3 Quick Check

<details>
<summary><b>🔍 Self-Check Question 1:</b> If heuristic h(n) = 0 for all states, what standard algorithm does A* become?</summary>

When $h(n) = 0$, $f(n) = g(n) + 0 = g(n)$, reducing A\* identically to **Uniform Cost Search (UCS)**.
</details>

<details>
<summary><b>🔍 Self-Check Question 2:</b> Can an admissible heuristic overestimate the true cost to the goal?</summary>

**No.** By definition, an admissible heuristic must satisfy $0 \le h(n) \le h^*(n)$ for all nodes $n$. Overestimating could cause A\* to bypass the true optimal path.
</details>

---

## Chapter 04 — Metaheuristic Algorithms

> **In One Line:** When search spaces are astronomically large, metaheuristics iteratively optimize candidate solutions on a fitness landscape to find high-quality solutions rapidly.

### 4.1 Hill Climbing & Landscape Hazards

Hill climbing begins with an arbitrary state and iteratively shifts towards the neighbor with the highest objective improvement.

```mermaid
graph TD
    subgraph OptimizationLandscape [State Space Landscape Topology]
        GM["🏔️ Global Maximum<br>(Target Optimal Solution)"]
        LM["⛰️ Local Maximum<br>(Traps Greedy Search)"]
        PL["🏞️ Flat Plateau<br>(Zero Gradient Walk)"]
        SH["🧗 Shoulder<br>(Leads upward later)"]
        RD["🔪 Narrow Ridge<br>(Requires Zig-Zag steps)"]
    end

    classDef landStyle fill:#f8fafc,stroke:#475569,stroke-width:2px,color:#0f172a;
    class GM,LM,PL,SH,RD landStyle;
```

#### Landscape Pathologies

| Hazard | Landscape Characterization | Failure Mode / Consequence | Remedial Strategy |
| :--- | :--- | :--- | :--- |
| **Local Maximum** | Peak higher than immediate neighbors, but suboptimal globally | Algorithm halts prematurely at suboptimal peak | Random Restarts, Simulated Annealing |
| **Plateau** | Flat state space region with identical evaluation values | Gradients vanish ($\nabla f = 0$); random walk | Allow bounded sideways moves |
| **Ridge** | Narrow sequence of local maxima leading upward | Slopes drop in all orthogonal cardinal directions | Macro-moves, diagonal step variations |

---

### 4.2 Hill Climbing Variations

- **Steepest-Ascent:** Evaluates all neighbors; transitions to highest scoring neighbor.
- **Stochastic Hill Climbing:** Chooses randomly among uphill neighbors, weighted by gradient magnitude.
- **First-Choice Hill Climbing:** Generates random neighbors sequentially, selecting the first one that improves fitness.
- **Random-Restart Hill Climbing:** Runs $k$ independent hill-climb trials from randomized initial states:
  $$\text{Success Probability} = 1 - (1 - p)^k$$

---

### 4.3 Simulated Annealing

Simulated Annealing mimics the metallurgical cooling process, permitting downhill/worse moves with a temperature-dependent probability to escape local optima.

```mermaid
flowchart TD
    Start(["Generate Initial Candidate Solution"]) --> Eval["Evaluate Neighbor State"]
    Eval --> Check{"Is Neighbor Better? (ΔE > 0)"}
    Check -- Yes --> Accept["Accept Neighbor Move"]
    Check -- No --> Prob["Accept with Prob: exp(ΔE / T)"]
    Accept --> Cool["Decrease Temp: T ← α · T"]
    Prob --> Cool
    Cool --> StopCheck{"Is Temperature Minimum?"}
    StopCheck -- No --> Eval
    StopCheck -- Yes --> Done(["Return Best Solution"])

    classDef process fill:#f0fdf4,stroke:#16a34a,stroke-width:2px,color:#14532d;
    classDef decision fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f;
    classDef term fill:#eff6ff,stroke:#2563eb,stroke-width:2px,color:#1e3a8a;

    class Eval,Accept,Cool,Prob process;
    class Check,StopCheck decision;
    class Start,Done term;
```

#### Acceptance Probability Formula
$$\Delta E = E_{\text{new}} - E_{\text{current}} \quad (\text{For maximization, } \Delta E < 0 \text{ is worse})$$
$$P(\text{accept}) = e^{\frac{\Delta E}{T}}$$

- At high Temperature $T \gg 0$: $P(\text{accept}) \approx 1$ (Aggressive exploration).
- At low Temperature $T \rightarrow 0$: $P(\text{accept}) \approx 0$ (Pure hill climbing exploitation).

---

### 4.4 Genetic Algorithms (GA)

Genetic Algorithms simulate Darwinian natural selection across a population of candidate chromosome bit-strings.

```mermaid
flowchart LR
    Pop["1. Population<br>(Bit Chromosomes)"] --> Fit["2. Fitness Score<br>f(x) Evaluation"]
    Fit --> Sel["3. Selection<br>(Roulette Wheel)"]
    Sel --> Cross["4. Crossover<br>(Tail Swapping)"]
    Cross --> Mut["5. Mutation<br>(Bit Flip)"]
    Mut --> Pop

    classDef gaStep fill:#faf5ff,stroke:#9333ea,stroke-width:2px,color:#581c87;
    class Pop,Fit,Sel,Cross,Mut gaStep;
```

#### Comprehensive Worked Example: Maximizing $f(x) = x^2$ for $x \in [0, 31]$ (5-bit String)

1. **Initial Population & Selection Probabilities ($P_i = \frac{f_i}{\sum f}$):**

| Chromosome | $x$ | Fitness $f(x) = x^2$ | $P_i$ (Selection Probability) |
| :---: | :---: | :---: | :---: |
| $C_1: 01101$ | $13$ | $169$ | $169 / 1170 \approx \mathbf{14.4\%}$ |
| $C_2: 11000$ | $24$ | $576$ | $576 / 1170 \approx \mathbf{49.2\%}$ |
| $C_3: 01000$ | $8$ | $64$ | $64 / 1170 \approx \mathbf{5.5\%}$ |
| $C_4: 10011$ | $19$ | $361$ | $361 / 1170 \approx \mathbf{30.9\%}$ |
| **Sum ($\sum$)** | — | $\mathbf{1170}$ | **$100\%$** |

2. **Single-Point Crossover (Cut-point = 4 between Parent $C_1$ and Parent $C_2$):**
   - Parent 1: `0 1 1 0 | 1` $\rightarrow$ **Child 1:** `0 1 1 0 | 0` ($x=12, f=144$)
   - Parent 2: `1 1 0 0 | 0` $\rightarrow$ **Child 2:** `1 1 0 0 | 1` ($x=25, f=\mathbf{625}$)
3. **Mutation:** Bit 3 flipped on Child 2: `1 1 0 1 1` ($x=27, f=\mathbf{729}$).

---

### 4.5 Differential Evolution (DE)

Population-based global optimization algorithm tailored for **continuous vector spaces** $\mathbf{x} \in \mathbb{R}^D$.

$$\mathbf{v}_i = \mathbf{x}_{r_1} + F \cdot (\mathbf{x}_{r_2} - \mathbf{x}_{r_3})$$

- $\mathbf{v}_i$: Mutant donor vector.
- $F \in [0, 2]$: Mutation scaling factor.
- $r_1, r_2, r_3$: Distinct randomly chosen vector indices.

---

### 4.6 Gradient Descent

Iterative first-order optimization algorithm to minimize differentiable objective loss functions $J(\theta)$.

$$\theta^{(t+1)} = \theta^{(t)} - \alpha \nabla_{\theta} J(\theta)$$

```python
# Minimizing J(θ) = θ^2 -> Gradient dJ/dθ = 2θ
theta = 4.0
alpha = 0.1  # Learning rate
for step in range(5):
    grad = 2 * theta
    theta = theta - alpha * grad
    print(f"Step {step+1}: theta = {theta:.4f}, Loss = {theta**2:.4f}")
```

---

### 4.7 Python Reference: Optimization in Action

```python
import math
import random

def simulated_annealing(cost_func, initial_state, temp=1000.0, cooling_rate=0.95, min_temp=1e-3):
    current_state = initial_state
    current_cost = cost_func(current_state)
    best_state, best_cost = current_state, current_cost

    while temp > min_temp:
        # Neighbor: perturb current state slightly
        neighbor = current_state + random.uniform(-1.0, 1.0)
        neighbor_cost = cost_func(neighbor)
        delta_e = neighbor_cost - current_cost

        # For minimization: accept if better or probabilistically if worse
        if delta_e < 0 or random.random() < math.exp(-delta_e / temp):
            current_state = neighbor
            current_cost = neighbor_cost
            if current_cost < best_cost:
                best_state, best_cost = current_state, current_cost

        temp *= cooling_rate

    return best_state, best_cost

# Target: Minimize f(x) = (x - 7)^2 + 3 -> Optimal x = 7.0, f(x) = 3.0
opt_x, min_val = simulated_annealing(lambda x: (x - 7)**2 + 3, initial_state=0.0)
print(f"Optimized x: {opt_x:.2f}, Minimum Value: {min_val:.2f}")
```

---

### Chapter 4 Quick Check

<details>
<summary><b>🔍 Self-Check Question 1:</b> In Simulated Annealing, what happens to the acceptance probability of a bad move as temperature T approaches 0?</summary>

As $T \rightarrow 0$, $e^{\Delta E / T} \rightarrow 0$ (for $\Delta E < 0$). The probability of accepting worse moves vanishes, causing the algorithm to behave purely as deterministic greedy hill climbing.
</details>

---

## Chapter 05 — Adversarial Search & Games

> **In One Line:** Adversarial search models competitive multi-agent environments where agents must select optimal moves under the assumption of a rational, counter-maximizing opponent.

### 5.1 Game Formulations & Game Trees

A deterministic, two-player, zero-sum game is formalized as:
- **$S_0$:** Initial state configuration.
- **$\text{Player}(s)$:** Returns whose turn it is ($\text{MAX}$ or $\text{MIN}$).
- **$\text{Actions}(s)$:** Legal move set.
- **$\text{Result}(s, a)$:** State transition resulting from move $a$.
- **$\text{Terminal-Test}(s)$:** True if game has finished.
- **$\text{Utility}(s, p)$:** Numeric outcome payoff for player $p$ at terminal state $s$ (e.g., $+1, 0, -1$).

---

### 5.2 The Minimax Algorithm

The Minimax algorithm chooses the best move assuming that the opponent also plays optimally.

$$
\text{Minimax}(s)=
\begin{cases}
\text{Utility}(s), & \text{if Terminal-Test}(s) \\
\max\limits_{a \in A(s)}
\text{Minimax}(\text{Result}(s,a)),
& \text{if Player}(s)=\text{MAX} \\
\min\limits_{a \in A(s)}
\text{Minimax}(\text{Result}(s,a)),
& \text{if Player}(s)=\text{MIN}
\end{cases}
$$

#### Example

```mermaid
graph TD
    Root["MAX Root: max(3, 2) = 3"]

    M1["MIN 1: min(3, 5) = 3"]
    M2["MIN 2: min(2, 9) = 2"]

    L1["Utility: 3"]
    L2["Utility: 5"]
    L3["Utility: 2"]
    L4["Utility: 9"]

    Root --> M1
    Root --> M2

    M1 --> L1
    M1 --> L2

    M2 --> L3
    M2 --> L4

    classDef maxNode fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a
    classDef minNode fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d
    classDef leafNode fill:#f1f5f9,stroke:#64748b,stroke-width:1px,color:#0f172a

    class Root maxNode
    class M1,M2 minNode
    class L1,L2,L3,L4 leafNode
```

> [!WARNING]
> **Common Student Exam Trap:**
> Do NOT simply look for the highest leaf in the tree (e.g., $9$). If MAX chooses the right branch hoping for $9$, a rational MIN opponent will choose $2$, giving MAX a payoff of $2$. MAX must play Left to secure guaranteed utility $\mathbf{3}$.

---

### 5.3 Alpha-Beta Pruning ($\alpha$-$\beta$)

$\alpha$-$\beta$ pruning returns the exact identical minimax decision while avoiding expansion of subtrees that cannot influence the final root outcome.

- $\alpha$: Value of the best (highest-value) choice found so far along the path for **MAX** ($\text{Initial } \alpha = -\infty$).
- $\beta$: Value of the best (lowest-value) choice found so far along the path for **MIN** ($\text{Initial } \beta = +\infty$).
- **Pruning Invariant:** Prune subtree branches beneath a node as soon as $\alpha \ge \beta$.

```mermaid
graph TD
    subgraph Level0 [MAX Root]
        Root["MAX Root: 3"]
    end
    subgraph Level1 [MIN Nodes]
        M1["MIN A: 3"]
        M2["MIN B: <= 2"]
        M3["MIN C: 2"]
    end
    subgraph Level2 [Terminal Leaves]
        A1["3"]
        A2["12"]
        A3["8"]
        B1["2"]
        B2["4 (PRUNED)"]
        B3["6 (PRUNED)"]
        C1["14"]
        C2["5"]
        C3["2"]
    end

    Root --> M1
    Root --> M2
    Root --> M3
    M1 --> A1
    M1 --> A2
    M1 --> A3
    M2 --> B1
    M2 -.-> B2
    M2 -.-> B3
    M3 --> C1
    M3 --> C2
    M3 --> C3

    classDef maxNode fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a;
    classDef minNode fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef pruneNode fill:#f1f5f9,stroke:#94a3b8,stroke-dasharray: 4 4,color:#64748b;

    class Root maxNode;
    class M1,M2,M3 minNode;
    class B2,B3 pruneNode;
```

#### Step-by-Step Trace of Pruning

1. Left MIN evaluates leaves $3, 12, 8 \rightarrow \text{Returns } 3$.
2. Root MAX updates its lower bound: $\alpha = \max(-\infty, 3) = \mathbf{3}$.
3. Middle MIN inspects first child ($2$). Its bound becomes $\beta = \min(+\infty, 2) = \mathbf{2}$.
4. **Pruning Condition Checked:** $\alpha (3) \ge \beta (2) \implies$ **Cutoff occurs!** Remaining children $4$ and $6$ are discarded without evaluation.
5. Right MIN evaluates $14, 5, 2 \rightarrow \text{Returns } 2$. Root $\alpha = \max(3, 2) = \mathbf{3}$.

---

### 5.4 Python Reference: Minimax & Alpha-Beta Engine

```python
def alpha_beta(node, depth, alpha, beta, is_maximizing, tree):
    # Base case: terminal leaf node
    if isinstance(tree[node], int):
        return tree[node]

    if is_maximizing:
        max_eval = float('-inf')
        for child in tree[node]:
            eval_score = alpha_beta(child, depth - 1, alpha, beta, False, tree)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if alpha >= beta:
                break  # Beta cutoff / prune
        return max_eval
    else:
        min_eval = float('inf')
        for child in tree[node]:
            eval_score = alpha_beta(child, depth - 1, alpha, beta, True, tree)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if alpha >= beta:
                break  # Alpha cutoff / prune
        return min_eval

game_tree = {
    'Root': ['M1', 'M2', 'M3'],
    'M1': ['L1', 'L2', 'L3'],
    'M2': ['L4', 'L5', 'L6'],
    'M3': ['L7', 'L8', 'L9'],
    'L1': 3, 'L2': 12, 'L3': 8,
    'L4': 2, 'L5': 4,  'L6': 6,
    'L7': 14, 'L8': 5, 'L9': 2
}

optimal_score = alpha_beta('Root', 2, float('-inf'), float('inf'), True, game_tree)
print(f"Optimal Alpha-Beta Minimax Value: {optimal_score}") # Output: 3
```

---

### Chapter 5 Quick Check

<details>
<summary><b>🔍 Self-Check Question 1:</b> In the best-case move ordering, what is the effective time complexity of Alpha-Beta pruning?</summary>

Under perfect move ordering (best moves evaluated first), the branching factor is effectively halved: $O(b^{m/2})$. This allows alpha-beta to search twice as deep as standard Minimax in identical compute time.
</details>

---

## Chapter 06 — Constraint Satisfaction Problems (CSPs)

> **In One Line:** CSPs reframe problem-solving from arbitrary path search to finding consistent variable assignments that adhere to an explicit set of constraints.

### 6.1 CSP Formalism & Constraint Graphs

A CSP comprises:
1. **Variables ($X$):** $X = \{X_1, X_2, \dots, X_n\}$
2. **Domains ($D$):** $D = \{D_1, D_2, \dots, D_n\}$, where $D_i$ denotes legal values for $X_i$.
3. **Constraints ($C$):** $C = \{C_1, C_2, \dots, C_m\}$, specifying allowed combinations of values.

#### Map Coloring Problem (Australia)

```mermaid
graph TD
    WA((WA: Red)) --- NT((NT: Green))
    WA --- SA((SA: Blue))
    NT --- SA
    NT --- Q((Q: Red))
    SA --- Q
    SA --- NSW((NSW: Green))
    SA --- V((V: Red))
    Q --- NSW
    NSW --- V
    T((T: Any Color))

    classDef rNode fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef gNode fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;
    classDef bNode fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a;
    classDef tNode fill:#f1f5f9,stroke:#64748b,stroke-width:2px,color:#0f172a;

    class WA,Q,V rNode;
    class NT,NSW gNode;
    class SA bNode;
    class T tNode;
```

- **Variables:** $\{WA, NT, SA, Q, NSW, V, T\}$
- **Domain:** $\{\text{Red}, \text{Green}, \text{Blue}\}$
- **Constraints:** Adjacent regions must not share identical colors ($WA \ne NT, WA \ne SA, \dots$).
- **Valid Solution:** $\{WA=R, NT=G, SA=B, Q=R, NSW=G, V=R, T=R\}$.

---

### 6.2 Constraint Propagation: Forward Checking & AC-3

#### Forward Checking
Whenever variable $X$ is assigned, prune all values from the domains of unassigned neighbors $Y$ that violate constraints with $X$. Backtrack immediately if any domain becomes empty.

#### Arc Consistency (AC-3 Algorithm)
An arc $X_i \rightarrow X_j$ is **arc-consistent** if for *every* value $x \in D_i$, there exists *some* legal value $y \in D_j$ satisfying binary constraint $(X_i, X_j)$.

```mermaid
flowchart TD
    Init["Initialize Queue with all directed Arcs in CSP"] --> Pop["Pop Arc (X_i to X_j) from Queue"]
    Pop --> Revise{"Revise Domain D_i? (Prune illegal values)"}
    Revise -- Values Pruned --> CheckEmpty{"Is D_i Empty?"}
    CheckEmpty -- Yes --> Fail(["Return Inconsistency / Failure"])
    CheckEmpty -- No --> AddNeighbors["Add all Arcs (X_k to X_i) back to Queue"]
    Revise -- No Change --> CheckQueue{"Is Queue Empty?"}
    AddNeighbors --> CheckQueue
    CheckQueue -- No --> Pop
    CheckQueue -- Yes --> Success(["CSP is Arc-Consistent"])

    classDef step fill:#f8fafc,stroke:#475569,stroke-width:2px,color:#0f172a;
    classDef decision fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f;
    classDef pass fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;
    classDef fail fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;

    class Init,Pop,AddNeighbors step;
    class Revise,CheckEmpty,CheckQueue decision;
    class Success pass;
    class Fail fail;
```

---

### 6.3 Backtracking Search with MRV, Degree & LCV

Standard CSP Backtracking is a recursive depth-first search assigning one variable at a time. Three core heuristics accelerate search performance:

```mermaid
flowchart LR
    subgraph VarOrder [Variable Ordering]
        MRV["Minimum Remaining Values (MRV)<br>Fail-First: Pick variable with fewest legal values"]
        DEG["Degree Heuristic<br>Tie-Breaker: Pick variable with most active constraints"]
    end
    subgraph ValOrder [Value Ordering]
        LCV["Least Constraining Value (LCV)<br>Fail-Last: Pick value pruning fewest neighbor options"]
    end

    classDef vo fill:#e0e7ff,stroke:#4f46e5,stroke-width:2px,color:#312e81;
    classDef val fill:#fce7f3,stroke:#db2777,stroke-width:2px,color:#831843;

    class MRV,DEG vo;
    class LCV val;
```

| Heuristic | Question Answered | Operational Rule | Intuitive Rationale |
| :--- | :--- | :--- | :--- |
| **MRV** | Which variable next? | Select variable with smallest $|D_i|$ | Identifies failures immediately at top of search tree |
| **Degree** | Which variable next (tie)? | Select variable involved in maximum active constraints | Constrains other variables maximally |
| **LCV** | Which value to try first? | Select value that rules out fewest neighbor values | Leaves maximum flexibility for remaining assignments |

---

### 6.4 Python Reference: CSP Solver

```python
def is_valid(assignment, var, val, neighbors):
    for neighbor in neighbors.get(var, []):
        if neighbor in assignment and assignment[neighbor] == val:
            return False
    return True

def backtrack(assignment, variables, domains, neighbors):
    if len(assignment) == len(variables):
        return assignment  # Solution found

    # Minimum Remaining Values (MRV)
    unassigned = [v for v in variables if v not in assignment]
    var = min(unassigned, key=lambda v: len(domains[v]))

    for val in domains[var]:
        if is_valid(assignment, var, val, neighbors):
            assignment[var] = val
            result = backtrack(assignment, variables, domains, neighbors)
            if result is not None:
                return result
            del assignment[var]  # Backtrack

    return None

vars_australia = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
doms = {v: ['Red', 'Green', 'Blue'] for v in vars_australia}
adj = {
    'WA': ['NT', 'SA'], 'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'], 'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'], 'V': ['SA', 'NSW'], 'T': []
}

solution = backtrack({}, vars_australia, doms, adj)
print("CSP Map Coloring Assignment:", solution)
```

---

### Chapter 6 Quick Check

<details>
<summary><b>🔍 Self-Check Question 1:</b> What is the time complexity of the AC-3 arc consistency algorithm for a CSP with n variables, domain size at most d, and c binary constraints?</summary>

AC-3 has a worst-case time complexity of $O(c \cdot d^3)$ operations.
</details>

---

## Chapter 07 — Learning in AI & Neural Networks

> **In One Line:** Machine Learning empowers systems to extract predictive mappings from data, using neural networks and gradient backpropagation to model non-linear boundaries.

### 7.1 Foundations of Machine Learning

$$\text{Traditional: } \text{Data} + \text{Rules} \rightarrow \text{Answers} \qquad\Longleftrightarrow\qquad \text{Machine Learning: } \text{Data} + \text{Answers} \rightarrow \text{Rules (Model)}$$

- **Supervised Learning:** Inputs paired with target labels (Classification / Regression).
- **Unsupervised Learning:** Unlabeled data; clusters patterns (K-Means, PCA).
- **Reinforcement Learning:** Learns through scalar reward feedback from environment.

---

### 7.2 Artificial Neural Networks & Activation Functions

```mermaid
graph LR
    subgraph Inputs [Input Vector]
        x1["Input x1"]
        x2["Input x2"]
        b["Bias b (+1)"]
    end
    subgraph Neuron [Artificial Processing Unit]
        Sum["Linear Combination:<br>z = w1·x1 + w2·x2 + b"]
        Act["Non-Linear Activation:<br>y = σ(z)"]
    end
    subgraph Output [Model Prediction]
        y["Prediction y"]
    end

    x1 -->|Weight w1| Sum
    x2 -->|Weight w2| Sum
    b -->|Weight 1.0| Sum
    Sum --> Act
    Act --> y

    classDef inNode fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0369a1;
    classDef sumNode fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#4c1d95;
    classDef outNode fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;

    class x1,x2,b inNode;
    class Sum,Act sumNode;
    class y outNode;
```

$$z = \sum_{i=1}^{n} w_i x_i + b \qquad\Longrightarrow\qquad y = \sigma(z) = \frac{1}{1 + e^{-z}}$$

#### Standard Activation Functions

| Function | Mathematical Formulation | Output Range | Primary Application |
| :--- | :--- | :--- | :--- |
| **Sigmoid ($\sigma$)** | $f(z) = \frac{1}{1 + e^{-z}}$ | $(0, 1)$ | Binary probabilities / Output layers |
| **Tanh** | $f(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$ | $(-1, +1)$ | Zero-centered hidden layer activations |
| **ReLU** | $f(z) = \max(0, z)$ | $[0, \infty)$ | Default hidden layer activation (prevents vanishing gradient) |
| **Softmax** | $f(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$ | $(0, 1), \sum=1$ | Multi-class categorical distributions |

---

### 7.3 The Backpropagation Algorithm

Backpropagation implements the multivariate calculus **chain rule** to propagate loss gradients backwards from the output layer to hidden weights.

```mermaid
flowchart LR
    Fwd["Forward Pass:<br>x → Linear z → Activation y"] --> Loss["Compute Loss:<br>E = 0.5 * (target - y)²"]
    Loss --> Back["Backward Pass:<br>δ = (y - target) · y(1 - y)"]
    Back --> Update["Gradient Update:<br>w_new = w_old - η · δ · x"]

    classDef fwdStyle fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a;
    classDef lossStyle fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef backStyle fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#4c1d95;
    classDef updStyle fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;

    class Fwd fwdStyle;
    class Loss lossStyle;
    class Back backStyle;
    class Update updStyle;
```

#### Detailed Single Neuron Calculation Walkthrough

- **Given Parameters:** Inputs $x_1 = 1.0, x_2 = 0.5$; Initial weights $w_1 = 0.4, w_2 = 0.6$; Bias $b = 0.1$; Learning rate $\eta = 0.5$; Target label $t = 1.0$.

1. **Forward Pass:**
   $$z = w_1 x_1 + w_2 x_2 + b = (0.4)(1.0) + (0.6)(0.5) + 0.1 = 0.4 + 0.3 + 0.1 = \mathbf{0.8}$$
   $$y = \sigma(0.8) = \frac{1}{1 + e^{-0.8}} = \frac{1}{1 + 0.4493} = \mathbf{0.69}$$
   $$\text{Error } E = \frac{1}{2}(t - y)^2 = \frac{1}{2}(1.0 - 0.69)^2 = \mathbf{0.048}$$

2. **Backward Pass (Gradient Computation):**
   $$\delta = (y - t) \cdot y(1 - y) = (0.69 - 1.0) \cdot (0.69)(0.31) = (-0.31)(0.2139) = \mathbf{-0.0663}$$

3. **Weight Adjustments ($w_i \leftarrow w_i - \eta \cdot \delta \cdot x_i$):**
   $$w_1^{\text{new}} = 0.4 - (0.5)(-0.0663)(1.0) = 0.4 + 0.0331 = \mathbf{0.4331}$$
   $$w_2^{\text{new}} = 0.6 - (0.5)(-0.0663)(0.5) = 0.6 + 0.0166 = \mathbf{0.6166}$$
   $$b^{\text{new}} = 0.1 - (0.5)(-0.0663) = 0.1 + 0.0331 = \mathbf{0.1331}$$

---

### 7.4 Python Reference: Neural Network Forward & Backprop Pass

```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_derivative(y):
    return y * (1.0 - y)

# Sample Forward & Backpropagation Step
x = np.array([1.0, 0.5])
w = np.array([0.4, 0.6])
b = 0.1
target = 1.0
eta = 0.5

# 1. Forward
z = np.dot(w, x) + b
y = sigmoid(z)
error = 0.5 * (target - y)**2

# 2. Backward
delta = (y - target) * sigmoid_derivative(y)
grad_w = delta * x
grad_b = delta

# 3. Update
w_new = w - eta * grad_w
b_new = b - eta * grad_b

print(f"Output y: {y:.4f} | Loss: {error:.4f}")
print(f"Updated Weights: {w_new.round(4)} | Updated Bias: {b_new:.4f}")
```

---

## Chapter 08 — Knowledge Bases & Logic

> **In One Line:** Knowledge-based agents store structured logical assertions and use sound inference procedures (forward/backward chaining) to prove conclusions and diagnose faults.

### 8.1 Propositional Logic & Models

- **Knowledge Base ($KB$):** A set of sentences expressed in formal logic.
- **Entailment ($KB \models \alpha$):** Sentence $\alpha$ is true in *all* possible worlds/models where $KB$ is true.
- **Inference Rule (Modus Ponens):** From $P$ and $P \rightarrow Q$, infer $Q$.

---

### 8.2 Definite Clauses & Horn Clauses

A **definite clause** contains exactly one positive literal (its head) and conjunctions of positive body atoms:

$$h \leftarrow a_1 \land a_2 \land \dots \land a_m$$

*(Read as: $h$ is true IF $a_1 \land \dots \land a_m$ are all true).*

```
light_on   ← switch_up ∧ power_ok.
power_ok   ← breaker_ok.
breaker_ok.
switch_up.
```

---

### 8.3 Proof Procedures: Forward & Backward Chaining

```mermaid
graph TD
    subgraph BottomUp [Forward Chaining: Data-Driven]
        F1["Facts: breaker_ok, switch_up"] -->|Fires Rule 1| F2["Infers: power_ok"]
        F2 -->|Fires Rule 2| F3["Infers: light_on (Goal Proved!)"]
    end
    subgraph TopDown [Backward Chaining: Goal-Driven]
        Q["Query: light_on?"] --> Q1["Subgoals: switch_up AND power_ok"]
        Q1 --> Q2["switch_up: Ground Fact<br>power_ok: Needs breaker_ok"]
        Q2 --> Q3["breaker_ok: Ground Fact (Q.E.D.)"]
    end

    classDef fcStyle fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;
    classDef bcStyle fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a;

    class F1,F2,F3 fcStyle;
    class Q,Q1,Q2,Q3 bcStyle;
```

| Attribute | Bottom-Up (Forward Chaining) | Top-Down (Backward Chaining) |
| :--- | :--- | :--- |
| **Direction** | Data-driven: Facts $\rightarrow$ Conclusions | Goal-driven: Query $\rightarrow$ Supporting Subgoals |
| **Use Case** | Routine monitoring, reactive production systems | Query answering, expert diagnostics, Prolog engines |
| **Space Overhead** | High (derives all possible consequences) | Low (explores only goal-relevant sub-branches) |

---

### 8.4 Ask-the-User & Knowledge-Level Debugging

- **Askable Atoms:** Primitives that can be queried from the user at runtime during backward chaining.
- **Debugging Types:**
  - **Incorrect Answer:** Trace backward to find a clause where body atoms are true in reality, but head atom is false $\rightarrow$ Clause is erroneous.
  - **Missing Answer:** Find an atom that is true in reality, but has no matching clause whose body evaluates to true $\rightarrow$ Clause is missing.

---

### 8.5 Consistency-Based Diagnosis & Minimal Conflicts

Given a set of normal-behavior assumptions (**Assumables** $\{ok(C_1), ok(C_2), \dots\}$), an observed symptom contradicts normalcy:

$$\text{Conflict Set: A subset of assumables that entails } \text{false}$$
$$\text{Diagnosis: A minimal set of components whose failure resolves all conflicts}$$

```mermaid
graph TD
    Switch["Switch Component: ok_switch"] --> Light["Light: ok_bulb"]
    Switch --> Fan["Fan: ok_fan"]
    Obs1["Observed: Light is OFF"] -.-> Light
    Obs2["Observed: Fan is OFF"] -.-> Fan
    Diag["Minimal Diagnosis: ok_switch = False<br>(Single fault explains both symptoms)"]

    classDef comp fill:#f1f5f9,stroke:#64748b,stroke-width:2px,color:#0f172a;
    classDef obs fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef diag fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;

    class Switch,Light,Fan comp;
    class Obs1,Obs2 obs;
    class Diag diag;
```

---

### 8.6 Python Reference: Forward Chaining Engine

```python
def forward_chaining(facts, rules, query):
    inferred = set(facts)
    changed = True

    while changed:
        changed = False
        for head, body in rules:
            if head not in inferred and all(atom in inferred for atom in body):
                inferred.add(head)
                changed = True
                if head == query:
                    return True, inferred

    return query in inferred, inferred

kb_facts = {'breaker_ok', 'switch_up'}
kb_rules = [
    ('power_ok', ['breaker_ok']),
    ('light_on', ['switch_up', 'power_ok'])
]

success, conclusions = forward_chaining(kb_facts, kb_rules, 'light_on')
print(f"Query Proved: {success} | Derived Knowledge Base: {conclusions}")
```

---

## Chapter 09 — Classical Planning with Certainty

> **In One Line:** Classical planning determines an organized sequence of actions that transitions an agent from an initial state to a goal state in deterministic, fully observable worlds.

### 9.1 Action Representations & The STRIPS Assumption

```mermaid
flowchart LR
    Act["STRIPS Action Operator"] --> Pre["1. Preconditions:<br>Predicates required before execution"]
    Act --> EffA["2. Add List:<br>Predicates that become True"]
    Act --> EffD["3. Delete List:<br>Predicates that become False"]

    classDef actStyle fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#4c1d95;
    classDef subStyle fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#334155;

    class Act actStyle;
    class Pre,EffA,EffD subStyle;
```

> [!NOTE]
> **The STRIPS Frame Assumption:**
> Any world literal not explicitly stated in an action's Add or Delete list remains unchanged after action execution.

#### Coffee Delivery Robot Problem Pipeline

```mermaid
flowchart LR
    S0["S0: At Office, No Coffee"] -->|go_kitchen| S1["S1: At Kitchen, No Coffee"]
    S1 -->|pick_coffee| S2["S2: At Kitchen, Has Coffee"]
    S2 -->|go_office| S3["S3: At Office, Has Coffee"]
    S3 -->|deliver| S4["S4: Goal Reached (Delivered)"]

    classDef planStep fill:#f0fdf4,stroke:#16a34a,stroke-width:2px,color:#14532d;
    class S0,S1,S2,S3,S4 planStep;
```

| Action | Preconditions | Add List (Effects True) | Delete List (Effects False) |
| :--- | :--- | :--- | :--- |
| `go_kitchen` | `At = Office` | `At = Kitchen` | `At = Office` |
| `go_office` | `At = Kitchen` | `At = Office` | `At = Kitchen` |
| `pick_coffee`| `At = Kitchen`, `HasCoffee = F` | `HasCoffee = T` | `HasCoffee = F` |
| `deliver` | `At = Office`, `HasCoffee = T` | `Delivered = T`, `HasCoffee = F` | `HasCoffee = T` |

---

### 9.2 Forward State-Space Planning vs Backward Planning

- **Forward Planning (Progression):** Searches forward from $S_0$ by exploring applicable actions. (Sound and complete, but suffers from large branching factors).
- **Backward Planning (Regression):** Searches backwards from Goal by identifying relevant operators achieving goal literals. (Prunes irrelevant actions).

---

### 9.3 Python Reference: STRIPS Planning Engine

```python
class Action:
    def __init__(self, name, preconds, add_list, del_list):
        self.name = name
        self.preconds = set(preconds)
        self.add_list = set(add_list)
        self.del_list = set(del_list)

    def is_applicable(self, state):
        return self.preconds.issubset(state)

    def apply(self, state):
        return (state - self.del_list) | self.add_list

def plan_forward(initial_state, goal_state, actions):
    from collections import deque
    queue = deque([(initial_state, [])])
    visited = [initial_state]

    while queue:
        state, plan = queue.popleft()
        if goal_state.issubset(state):
            return plan

        for action in actions:
            if action.is_applicable(state):
                next_state = action.apply(state)
                if next_state not in visited:
                    visited.append(next_state)
                    queue.append((next_state, plan + [action.name]))
    return None

actions = [
    Action('go_kitchen', ['At_Office'], ['At_Kitchen'], ['At_Office']),
    Action('go_office', ['At_Kitchen'], ['At_Office'], ['At_Kitchen']),
    Action('pick_coffee', ['At_Kitchen', 'No_Coffee'], ['Has_Coffee'], ['No_Coffee']),
    Action('deliver', ['At_Office', 'Has_Coffee'], ['Delivered', 'No_Coffee'], ['Has_Coffee'])
]

init = {'At_Office', 'No_Coffee'}
goal = {'Delivered'}
plan = plan_forward(init, goal, actions)
print("Synthesized Plan:", plan)
# Output: ['go_kitchen', 'pick_coffee', 'go_office', 'deliver']
```

---

## Chapter 10 — Reasoning Under Uncertainty

> **In One Line:** Probability theory, Bayesian Networks, Markov Decision Processes, and HMMs allow agents to quantify uncertainty, update beliefs, and make optimal sequential decisions.

### 10.1 Probability Basics & Bayes' Rule

$$P(A \mid B) = \frac{P(A \land B)}{P(B)} \qquad\Longrightarrow\qquad P(H \mid E) = \frac{P(E \mid H) \cdot P(H)}{P(E)}$$

#### High-Yield Medical Diagnosis Example

- Prior probability of disease: $P(D) = 0.01$. Test sensitivity: $P(+ \mid D) = 0.90$. False positive rate: $P(+ \mid \neg D) = 0.05$.

$$P(+) = P(+ \mid D)P(D) + P(+ \mid \neg D)P(\neg D) = (0.90)(0.01) + (0.05)(0.99) = 0.009 + 0.0495 = \mathbf{0.0585}$$
$$P(D \mid +) = \frac{P(+ \mid D)P(D)}{P(+)} = \frac{0.009}{0.0585} \approx \mathbf{15.38\%}$$

---

### 10.2 Conditional Independence & Network Topologies

```mermaid
graph TD
    subgraph Chain["1. Causal Chain: A to B to C"]
        C_A["Rain A"] --> C_B["Traffic B"]
        C_B --> C_C["Late C"]
        C_Note["A and C are conditionally independent given B"]
    end

    subgraph Fork["2. Common Cause: A from B to C"]
        F_A["Karim Late A"] --> F_B["Traffic B"]
        F_B --> F_C["Rahim Late C"]
        F_Note["A and C are conditionally independent given B"]
    end

    subgraph Collider["3. Collider: A to B from C"]
        CL_A["Burglary A"] --> CL_B["Alarm B"]
        CL_C["Earthquake C"] --> CL_B
        CL_Note["A and C are independent; they become dependent given B"]
    end

    classDef boxStyle fill:#f8fafc,stroke:#475569,stroke-width:1px,color:#0f172a

    class C_A,C_B,C_C,F_A,F_B,F_C,CL_A,CL_B,CL_C boxStyle
```

> [!IMPORTANT]
> **Explaining Away (The Collider Property):**
> In a collider network ($\text{Burglary} \rightarrow \text{Alarm} \leftarrow \text{Earthquake}$), Burglary and Earthquake are initially independent. However, conditioning on $\text{Alarm} = \text{True}$ creates dependency: confirming an Earthquake explains away the alarm, decreasing the posterior probability of a Burglary.

---

### 10.3 Bayesian Belief Networks (BBN)

A Bayesian Network represents a joint probability distribution over DAG variables:

$$P(X_1, X_2, \dots, X_n) = \prod_{i=1}^{n} P(X_i \mid \text{Parents}(X_i))$$

```mermaid
graph TD
    R["🌧️ Rain (R)<br>P(R) = 0.30"] --> T["🚗 Traffic Jam (T)<br>P(T given R)=0.8, P(T given ¬R)=0.2"]
    T --> L["⏰ Late to Class (L)<br>P(L given T)=0.6, P(L given ¬T)=0.1"]

    classDef bnNode fill:#f0f9ff,stroke:#0284c7,stroke-width:2px,color:#0369a1;
    class R,T,L bnNode;
```

#### Diagnostic Query Computation: $P(R \mid L)$

1. $P(T) = (0.3)(0.8) + (0.7)(0.2) = 0.24 + 0.14 = \mathbf{0.38}$
2. $P(L) = P(L \mid T)P(T) + P(L \mid \neg T)P(\neg T) = (0.6)(0.38) + (0.1)(0.62) = 0.228 + 0.062 = \mathbf{0.29}$
3. $P(L \mid R) = (0.8)(0.6) + (0.2)(0.1) = 0.48 + 0.02 = \mathbf{0.50}$
4. **Bayes Rule Application:**
   $$P(R \mid L) = \frac{P(L \mid R) P(R)}{P(L)} = \frac{(0.50)(0.30)}{0.29} \approx \mathbf{51.72\%}$$

---

### 10.4 Bayesian Parameter Learning

For complete data, maximum likelihood parameters are calculated directly via counting with **Laplace Add-One Smoothing**:

$$P_{\text{Laplace}}(X = v \mid \text{Parent}) = \frac{\text{Count}(X = v, \text{Parent}) + 1}{\text{Count}(\text{Parent}) + |D_X|}$$

---

### 10.5 Markov Decision Processes (MDPs) & The Bellman Equation

A Markov Decision Process (MDP) is defined by:

$$
\langle S, A, T, R, \gamma \rangle
$$

where:

- $S$ = Set of states
- $A$ = Set of actions
- $T$ = Transition model
- $R$ = Reward function
- $\gamma$ = Discount factor

The Bellman optimality equation is:

$$ V^*(s) = \max_{a \in A} \sum_{s'} P(s' \mid s,a) \left[ R(s,a,s') + \gamma V^*(s') \right] $$

where $V^*(s)$ represents the optimal value of state $s$.

#### Example: Temperature-Controlled Environment

```mermaid
graph LR
    Cool((Cool)) -->|slow 100%| Cool
    Cool -->|fast 50%| Cool
    Cool -->|fast 50%| Warm((Warm))

    Warm -->|slow 50%| Cool
    Warm -->|slow 50%| Warm
    Warm -->|fast 100%| Overheat((Overheated -10))

    classDef coolNode fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a
    classDef warmNode fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f
    classDef dangerNode fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d

    class Cool coolNode
    class Warm warmNode
    class Overheat dangerNode

---

### 10.6 Hidden Markov Models (HMMs)

HMM assumes true system state $X_t$ is hidden; agent only receives observations $E_t$.

```mermaid
graph LR
    subgraph HiddenTrellis [Hidden Weather State Timeline]
        X1["X1: Rain/Sun"] -->|Transition P| X2["X2: Rain/Sun"] -->|Transition P| X3["X3: Rain/Sun"]
    end
    subgraph ObservedTrellis [Observed Evidence Timeline]
        E1["E1: Umbrella?"]
        E2["E2: Umbrella?"]
        E3["E3: Umbrella?"]
    end

    X1 -->|Emission P| E1
    X2 -->|Emission P| E2
    X3 -->|Emission P| E3

    classDef hStyle fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#4c1d95;
    classDef oStyle fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f;

    class X1,X2,X3 hStyle;
    class E1,E2,E3 oStyle;
```

- **Forward Algorithm (Filtering):** Computes current belief state $P(X_t \mid e_{1:t})$.
- **Viterbi Algorithm (Decoding):** Finds most probable sequence of hidden states $\arg\max_{X_{1:t}} P(X_{1:t} \mid e_{1:t})$.

---

### 10.7 Python Reference: Bayesian & HMM Computing

```python
# HMM Forward Algorithm (Filtering) for Umbrella Example
# States: 0: Rain, 1: Sun
P_init = [0.5, 0.5]
T_matrix = [[0.7, 0.3],   # P(X_t | Rain_{t-1})
            [0.3, 0.7]]   # P(X_t | Sun_{t-1})
E_matrix = [[0.9, 0.1],   # P(Umbrella | Rain), P(No | Rain)
            [0.2, 0.8]]   # P(Umbrella | Sun), P(No | Sun)

# Day 1: Umbrella observed
f1_rain = P_init[0] * E_matrix[0][0]
f1_sun  = P_init[1] * E_matrix[1][0]
norm1 = f1_rain + f1_sun
f1 = [f1_rain / norm1, f1_sun / norm1]
print(f"Day 1 Belief P(Rain|U1): {f1[0]:.4f}")  # Output: 0.8182

# Day 2: Umbrella observed
pred_rain = f1[0] * T_matrix[0][0] + f1[1] * T_matrix[1][0]
pred_sun  = f1[0] * T_matrix[0][1] + f1[1] * T_matrix[1][1]
f2_rain = pred_rain * E_matrix[0][0]
f2_sun  = pred_sun * E_matrix[1][0]
norm2 = f2_rain + f2_sun
f2 = [f2_rain / norm2, f2_sun / norm2]
print(f"Day 2 Belief P(Rain|U1, U2): {f2[0]:.4f}")  # Output: 0.8829
```

---

### Chapter 10 Quick Check

<details>
<summary><b>🔍 Self-Check Question 1:</b> In a Bayes Net with a collider topology (A → B ← C), are A and C conditionally independent given B?</summary>

**No.** In a collider structure, $A$ and $C$ are marginally independent, but they become **conditionally dependent** when conditioned on their common child $B$ (the Explaining Away phenomenon).
</details>

---

## Chapter 11 — Reinforcement Learning (RL)

> **In One Line:** Reinforcement learning solves unknown MDPs through trial-and-error interactions, balancing exploration of novel actions with exploitation of rewarded behaviors.

### 11.1 The Reinforcement Learning Paradigm

```mermaid
flowchart TD
    Agent["🤖 Agent (Policy π)"] -->|Action a_t| Env["🌐 Environment (Unknown MDP)"]
    Env -->|Reward r_t+1| Agent
    Env -->|Next State s_t+1| Agent

    classDef agStyle fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a;
    classDef envStyle fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;

    class Agent agStyle;
    class Env envStyle;
```

- **Credit Assignment Problem:** Determining which past action sequence deserved praise for delayed terminal rewards.
- **Model-Free vs Model-Based:** Model-free RL learns value functions directly without constructing explicit transition/reward tables.

---

### 11.2 Passive vs Active RL, TD-Learning & SARSA

#### Temporal Difference (TD) Learning Update
$$V(s) \leftarrow V(s) + \alpha \left[ \underbrace{r + \gamma V(s')}_{\text{TD Target}} - \underbrace{V(s)}_{\text{Estimate}} \right]$$

#### SARSA (On-Policy TD Control)
$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma Q(s', a') - Q(s, a) \right]$$
*(Updates using the actual action $a'$ chosen by the exploratory policy).*

---

### 11.3 Exploration vs Exploitation ($\epsilon$-Greedy)

$$a = \begin{cases} \arg\max_{a'} Q(s, a') & \text{with probability } 1 - \epsilon \quad \text{(Exploit)} \\ \text{Random Action} & \text{with probability } \epsilon \quad \text{(Explore)} \end{cases}$$

---

### 11.4 Q-Learning (Off-Policy TD Control)

$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$$

```mermaid
flowchart TD
    Init["Initialize Q-Table Q(s, a) = 0"] --> Observe["Observe State s"]
    Observe --> ActSelect["Choose Action a via ε-greedy"]
    ActSelect --> Exec["Take action a: Receive r and Next State s'"]
    Exec --> QUpdate["Update Q: Q(s,a) ← Q(s,a) + α · TD_Error"]
    QUpdate --> NextState["Transition: s ← s'"]
    NextState --> CheckTerm{"Is Episode Finished?"}
    CheckTerm -- No --> ActSelect
    CheckTerm -- Yes --> Observe

    classDef step fill:#f0fdf4,stroke:#16a34a,stroke-width:2px,color:#14532d;
    classDef dec fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f;

    class Init,Observe,ActSelect,Exec,QUpdate,NextState step;
    class CheckTerm dec;
```

#### Step-by-Step Two-Episode Trace (Corridor World)
- Environment: $A \rightarrow B \rightarrow C \text{ (Goal)}$. Step cost $r = -1$, reaching $C$ gives $r = +10$. $\alpha = 0.5, \gamma = 0.9$. All initial $Q = 0$.

| Episode | Step / Transition | Q-Update Equation | New $Q(s, a)$ Value |
| :---: | :---: | :--- | :--- |
| **Ep 1** | $A \rightarrow B, r=-1$ | $0 + 0.5[-1 + 0.9(0) - 0]$ | $Q(A, \text{right}) = \mathbf{-0.5}$ |
| **Ep 1** | $B \rightarrow C, r=+10$| $0 + 0.5[10 + 0.9(0) - 0]$ | $Q(B, \text{right}) = \mathbf{+5.0}$ |
| **Ep 2** | $A \rightarrow B, r=-1$ | $-0.5 + 0.5[-1 + 0.9(5.0) - (-0.5)]$ | $Q(A, \text{right}) = \mathbf{+1.5}$ |
| **Ep 2** | $B \rightarrow C, r=+10$| $5.0 + 0.5[10 + 0.9(0) - 5.0]$ | $Q(B, \text{right}) = \mathbf{+7.5}$ |

---

### 11.5 Python Reference: Tabular Q-Learning Engine

```python
import numpy as np

# Corridor: State 0 (A), State 1 (B), State 2 (C - Terminal Goal)
num_states = 3
num_actions = 1  # 0: move right
Q = np.zeros((num_states, num_actions))

alpha = 0.5
gamma = 0.9

episodes = [
    [(0, 0, -1, 1), (1, 0, 10, 2)],  # Ep 1: (s, a, r, s')
    [(0, 0, -1, 1), (1, 0, 10, 2)]   # Ep 2: (s, a, r, s')
]

for ep_idx, episode in enumerate(episodes):
    for s, a, r, next_s in episode:
        max_q_next = 0.0 if next_s == 2 else np.max(Q[next_s])
        td_target = r + gamma * max_q_next
        Q[s, a] += alpha * (td_target - Q[s, a])

print("Trained Q-Table:")
print(f"Q(State A, Right): {Q[0, 0]:.2f}")  # Output: 1.50
print(f"Q(State B, Right): {Q[1, 0]:.2f}")  # Output: 7.50
```

---

## 🏆 Master Exam Cheat Sheet & Formulas

### 1. Algorithm Complexity Matrix

| Algorithm | Frontier Data Structure | Complete? | Optimal? | Time Complexity | Space Complexity |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **BFS** | FIFO Queue | **Yes** (if $b < \infty$) | **Yes** (for uniform step costs) | $O(b^d)$ | $O(b^d)$ |
| **DFS** | LIFO Stack / Recursion | **No** (infinite trees) | **No** | $O(b^m)$ | $O(b \cdot m)$ |
| **UCS** | Priority Queue by $g(n)$ | **Yes** (if $c \ge \epsilon > 0$) | **Yes** (general non-negative costs) | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ |
| **IDS** | Repeated Depth Bounds | **Yes** | **Yes** (uniform costs) | $O(b^d)$ | $O(b \cdot d)$ |
| **Greedy** | Priority Queue by $h(n)$ | **No** | **No** | $O(b^m)$ | $O(b^m)$ |
| **A\*** | Priority Queue by $g(n) + h(n)$ | **Yes** | **Yes** (admissible/consistent $h$) | $O(b^d)$ | $O(b^d)$ |
| **IDA\*** | Depth-first bounded by $f$ | **Yes** | **Yes** | $O(b^d)$ | $O(b \cdot d)$ |
| **Minimax**| Game Tree Recursion | **Yes** (finite game) | **Yes** (vs optimal opponent) | $O(b^m)$ | $O(b \cdot m)$ |
| **Alpha-Beta**| Pruned Recursion ($\alpha, \beta$) | **Yes** | **Yes** (same as Minimax) | $O(b^{m/2})$ *(best case)* | $O(b \cdot m)$ |

---

### 2. High-Yield Formula Reference

| Name | Mathematical Equation | Key Use / Context |
| :--- | :--- | :--- |
| **Heuristic Admissibility** | `0 ≤ h(n) ≤ h*(n)` | Guarantees Tree-Search A* optimality |
| **Heuristic Consistency** | `h(n) ≤ c(n,n') + h(n')` | Guarantees Graph-Search A* optimality |
| **Simulated Annealing** | `P(accept) = e^(ΔE/T)` | Escaping local optima in stochastic search |
| **Bayes' Rule** | `P(H\|E) = P(E\|H)P(H) / P(E)` | Inverse conditional probability updating |
| **Bayes Net Joint** | `P(X₁,...,Xₙ) = ∏ P(Xᵢ\|Parents(Xᵢ))` | Factorizing the full joint distribution |
| **Bellman Equation** | `V*(s) = maxₐ Σ P(s'\|s,a)[R(s,a,s') + γV*(s')]` | Value iteration for optimal MDP policy |
| **Q-Learning Update** | `Q(s,a) ← Q(s,a) + α[r + γ maxₐ' Q(s',a') - Q(s,a)]` | Model-free off-policy reinforcement learning |
| **Delta Rule (Backpropagation)** | `δ = (y - t)y(1-y)` → `wᵢ ← wᵢ - ηδxᵢ` | Neural-network gradient-descent weight update |

---

<p align="center">
  <b>CSE366 Artificial Intelligence Study Guide</b><br>
  Built with ❤️ for academic excellence. Happy Studying & Best of Luck with your Exams!
</p>
