class Interval():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def split(self, operand, value):
         if operand == "<":
             if self.b < value:
                 return Interval(self.a, self.b), None
             elif self.a >= value:
                 return None, Interval(self.a, self.b)
             else:
                 return Interval(self.a, value-1), Interval(value, self.b)
         if operand == ">":
             if self.a > value:
                 return Interval(self.a, self.b), None
             elif self.b <= value:
                 return None, Interval(self.a, self.b)
             else:
                 return Interval(value+1, self.b), Interval(self.a, value)
             
    def size(self):
        return self.b-self.a+1
        
class Condition():
    def __init__(self, condition):
        for op in "<>":
            if op in condition:
                self.operand = op
                idx = condition.index(op)
                
        self.variable = condition[:idx]
        self.value = int(condition[idx+1:])

    def valid(self, part):
        valid, invalid = part[self.variable].split(self.operand, self.value)
        ret1, ret2 = part.copy(), part.copy()
        ret1[self.variable] = valid
        ret2[self.variable] = invalid
        return ret1, ret2

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
        invalid = part
        for  cond in self.conditions:
            valid, invalid = cond.valid(invalid)
            yield (valid, self.dest_names[i])
            i += 1
        yield (invalid, self.dest_names[i])
            
workflows = {}
        
def parse_workflow(line):
    start = line.index("{")
    name = line[:start]
    workflow = line[start+1:-1]
    
    workflows[name] = Workflow(workflow)

    
with open("input19.txt", "r") as f:
    parse_workflows = True
    for line in f:
        line = line.strip()
        if not line:
            parse_workflows = False
            continue
        if parse_workflows:
            parse_workflow(line)
    

part = {
    "x": Interval(1, 4000), 
    "m": Interval(1, 4000), 
    "a": Interval(1, 4000), 
    "s": Interval(1, 4000)
}

finished = []
stack = [(part, "in")]

while stack:
    p, workflow = stack.pop(-1)

    for setup in workflows[workflow].evaluate(p):
        if setup[1] == "A":
            finished.append(setup[0])
        elif setup[1] == "R":
            pass
        else:
            stack.append(setup)

def size(part):
    res = 1
    for x in "xmas":
        res *= part[x].size()
    return res
    
print(sum([size(p) for p in finished]))
