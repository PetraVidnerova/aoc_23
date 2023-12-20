HIGH = True
LOW = False

class Module():
    def add_input(self, name):
        pass

    def process_pulse(self, pulse, from_):
        return []

class FlipFlop(Module):
    def  __init__(self, destinations, name):
        self.name = name
        self.state = LOW
        self.destinations = destinations

    def process_pulse(self, pulse, from_):
        if pulse == HIGH:
            return []
        else:
            self.state = not self.state
            return [(self.state, dest, self.name) for dest in self.destinations]

class Conjunction(Module):
    def __init__(self, destinations, name):
        self.name = name 
        self.inputs = {}
        self.destinations = destinations

    def add_input(self, name):
        self.inputs[name] = LOW

    def process_pulse(self, pulse, from_):
        self.inputs[from_] = pulse
        if all(v == HIGH for v in self.inputs.values()):
            return [(LOW, dest, self.name) for dest in self.destinations]
        else:
            return [(HIGH, dest, self.name) for dest in self.destinations]
        
        
rules = {}
start = []

with open("input20.txt", "r") as f:
    for line in f:
        left, right = line.strip().split("->")
        source = left.strip()
        dest = list(map(lambda x: x.strip(), right.strip().split(",")))
        if source == "broadcaster":
            start = dest
        elif source.startswith("%"):
            rules[source[1:]] =  FlipFlop(dest, source[1:])
        elif source.startswith("&"):
            rules[source[1:]] = Conjunction(dest, source[1:])

modules = list(rules.values())
for rule in modules:
    for dest in rule.destinations:
        if dest not in rules:
            rules[dest] = Module()
        rules[dest].add_input(rule.name)
    
for dest in start:
    rules[dest].add_input("broadcaster")
        

low_count = 0
high_count = 0


for button in range(1000):
    low_count += 1
    stack = [(LOW, x, "broadcaster") for x in start]            

    while stack:
        pulse, dest, source_name = stack.pop(0)
        if pulse == HIGH:
            high_count += 1
        else:
            low_count += 1
        stack.extend(
            rules[dest].process_pulse(pulse, source_name)
        )

print(low_count*high_count)
