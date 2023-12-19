class Condition():
    def __init__(self, condition):
        for op in "<>":
            if op in condition:
                self.operand = op
                idx = condition.index(op)
                
        self.variable = condition[:idx]
        self.value = int(condition[idx+1:])

    def valid(self, part):
        if self.operand == "<":
            return part[self.variable] < self.value
        elif self.operand == ">":
            return part[self.variable] > self.value
            
        

class Workflow():
    def __init__(self, rules):
        self.conditions = []
        self.dest_names = []

        rules = rules.split(",")
        for rule in rules[:-1]:
            condition, dest = rule.split(":") 
            self.conditions.append(Condition(condition))
            self.dest_names.append(dest)
        self.dest_names.append(rules[-1])

            
    def evaluate(self, part):
        i = 0
        for  cond in self.conditions:
            if cond.valid(part):
                break
            i += 1
        return self.dest_names[i]
            
workflows = {}
parts = []
        
def parse_workflow(line):
    start = line.index("{")
    name = line[:start]
    workflow = line[start+1:-1]
    
    workflows[name] = Workflow(workflow)

def parse_parts(line):
    line = line[1:-1]
    part = {}
    for p in line.split(","):
        name, value = p.split("=")
        part[name] = int(value)
    parts.append(part)
    
with open("input19.txt", "r") as f:
    parse_workflows = True
    for line in f:
        line = line.strip()
        if not line:
            parse_workflows = False
            continue
        if parse_workflows:
            parse_workflow(line)
        else:
            parse_parts(line)
    

print(workflows)
print(parts)

result = 0
for part in parts:
    workflow = "in"
    visited = set()

    while workflow != "R" and workflow != "A":
        workflow = workflows[workflow].evaluate(part)

    if workflow == "A":
        result += sum(part.values())

print(result)
