rules = {}
with open("input8.txt", "r") as f:
    lines = f.readlines()
    instructions = lines[0].strip()

    for line in lines[2:]:
        start, left_side = line.strip().split("=")
        start = start.strip()
        left, right = left_side.strip()[1:-1].split(",")
        rules[start] = {"L": left.strip(), "R": right.strip()}

steps = 0
field = "AAA"
while field != "ZZZ":
    rule = rules[field]
    direction = instructions[steps % len(instructions)]

    field = rule[direction]
    steps += 1

print(steps)
