rules = {}
with open("input8.txt", "r") as f:
    lines = f.readlines()
    instructions = lines[0].strip()

    for line in lines[2:]:
        start, left_side = line.strip().split("=")
        start = start.strip()
        left, right = left_side.strip()[1:-1].split(",")
        rules[start] = {"L": left.strip(), "R": right.strip()}


start_fields = [x for x in rules.keys() if x.endswith("A")]
z_points = {}
periods = {}

for field in start_fields:
    visited = set()
    visited_numbers = {}
    points = []

    steps = 0
    start = field
    while True:
        direction = instructions[steps % len(instructions)]
        if (start, steps % len(instructions)) in visited:
            break
        visited.add((start, steps % len(instructions)))
        visited_numbers[(start, steps % len(instructions))] = steps
        rule = rules[start]
        start = rule[direction]
        visited.add(start)
        steps += 1
        if start.endswith("Z"):
            points.append(steps)
        
    periods[field] = steps - visited_numbers[(start, steps % len(instructions))]
    z_points[field] = points

    
print(z_points)
print(periods)

### from now we know that z_points are single values equal to periods

def get_members(value):
    members = {}

    i = 2
    while value > 1:
        while value % i == 0:
            members[i] = members.get(i, 0) + 1
            value = value // i
        i += 1
    return members
    
def update(all_members, members):
    for k, v in members.items():
        if k in all_members:
            all_members[k] = max(all_members[k], v)
        else:
            all_members[k] = v
    return all_members


values = [x for x in periods.values()]

all_members = {}

for value in values:
    members = get_members(value)
    all_members = update(all_members, members)

print(all_members)

result = 1
for k, v in all_members.items():
    result *= k**v
print(result)
