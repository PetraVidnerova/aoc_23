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
    points = []

    steps = 0
    start = field
    while True:
        direction = instructions[steps % len(instructions)]
        if (start, steps % len(instructions)) in visited:
            break
        visited.add((start, steps % len(instructions)))
        rule = rules[start]
        start = rule[direction]
        visited.add(start)
        steps += 1
        if start.endswith("Z"):
            points.append(steps)
        
    periods[field] = steps-1
    z_points[field] = points

    
print(z_points)
print(periods)
