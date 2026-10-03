# CSE366 Artificial Intelligence Lab 02 - thermostat_agent.py
# Run: python thermostat_agent.py

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
