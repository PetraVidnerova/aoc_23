from math import ceil

UP = 0
RIGHT = 1
DOWN =  2
LEFT = 3


dirs = {
    (UP, "|"): UP,
    (UP, "7"): LEFT,
    (UP, "F"): RIGHT,

    (DOWN, "|"): DOWN,
    (DOWN, "J"): LEFT,
    (DOWN, "L"): RIGHT,

    (LEFT, "-"): LEFT,
    (LEFT, "F"): DOWN,
    (LEFT, "L"): UP,

    (RIGHT, "-"): RIGHT,
    (RIGHT, "J"): UP,
    (RIGHT, "7"): DOWN
}

idx = {
    LEFT: (0, -1),
    RIGHT: (0, 1),
    UP: (-1, 0),
    DOWN: (1, 0)
}


with open("input10.txt", "r") as f:
    lines = ["."+line.strip()+"." for line in f.readlines()]
    lines = [["."]*len(lines[0])] + lines + [["."]*len(lines[0])]
    
def findS(lines):
    for i, l in enumerate(lines):
        if "S" in l:
            return i, l.index("S")
    
x, y = findS(lines)
print(x, y)
direction = RIGHT
while not (direction, lines[x+idx[direction][0]][y+idx[direction][1]]) in dirs:
    direction += 1
length = 0 

while True:
    x += idx[direction][0]
    y += idx[direction][1]
    if lines[x][y] == "S":
        break

    direction = dirs[(direction, lines[x][y])]
    length += 1


print(length)
print(ceil(length/2))
