from math import ceil

UP = 1
RIGHT = 2
DOWN =  3
LEFT = 4

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
    lines = ["."*len(lines[0])] + lines + ["."*len(lines[0])]
    
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

width = len(lines[0])
height = len(lines)


copy = [["."]*width for i in range(height)]

count = 0 
while True:
    x += idx[direction][0]
    y += idx[direction][1]

    copy[x][y] = count
    count += 1
    
    if lines[x][y] == "S":
        break

    direction = dirs[(direction, lines[x][y])]

        
    length += 1
lines[x] = lines[x][:y] + "7" + lines[x][y+1:] # by looking on input
    

for line in copy:
    print(line)

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if copy[i][j] == ".":
            lines[i] = lines[i][:j] + "." + lines[i][j+1:]
    
def inside_horizontal(line):
    count = line.count("|")
    line  = [x for x in line if x != "." and x != "-" and x != "|"]
    while line:
        a = line.pop(0)
        b = line.pop(0)
        if (a, b) == ("F", "J"):
            count += 1
        elif (a, b) == ("L", "7"):
            count += 1 
    return count % 2 == 1

def inside_vertical(line):
    count = line.count("-")
    line  = [x for x in line if x != "." and x != "|" and x != "-"]
    while line:
        a = line.pop(0)
        b = line.pop(0)
        if (a, b) == ("7", "L"):
            count += 1
        elif (a, b) == ("F", "J"):
            count += 1 
    return count % 2 == 1

def is_inside(i, j):
    left = inside_horizontal(lines[i][:j])
    right = inside_horizontal(lines[i][j+1:])
    up = inside_vertical([l[j] for l in lines[:i]])
    down = inside_vertical([l[j] for l in lines[i+1:]])
    
    return left and right and up and down


inside = 0
for i, line in enumerate(lines):
    for j, x in enumerate(line):
        if copy[i][j] == "." and is_inside(i, j):
            inside += 1
print(inside)

