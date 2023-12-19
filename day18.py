import numpy as np

dig_plan = []

with open("input18.txt", "r") as f:
    for line in f:
        line = line.strip()
        direction, number, color = line.split()
        dig_plan.append((direction, int(number)))


holes = set()

h = (0,0)
maxx = 0
maxy = 0
minx = 0
miny = 0

for direction, number in dig_plan:
    for i in range(number):
        if direction == "R":
            h = h[0], h[1]+1
        elif direction == "L":
            h = h[0], h[1]-1
        elif direction == "D":
            h = h[0]+1, h[1]
        elif direction == "U":
            h = h[0]-1, h[1]
        holes.add(h)
        if h[0] > maxx:
            maxx = h[0]
        if h[1] > maxy:
            maxy = h[1]
        if h[0] < minx:
            minx = h[0]
        if   h[1] < miny:
            miny = h[1]
            
print(len(holes))
print(minx, miny)
print(maxx, maxy)

border = len(holes) 

holes2 = []

for i in range(0, -minx+maxx+1):
    line = []
    for j in range(0, -miny+maxy+1):
            line.append(".")    
    holes2.append(line) 


    
holes2 = np.array(holes2)
print(holes2.shape)
print(holes2)
print()

last_dir = None
h = (-minx, -miny)
for direction, number in dig_plan+dig_plan[:2]:
    assert h[0] >= 0
    assert h[1] >= 0
    assert h[0] <= maxx-minx
    assert h[1] <= maxy-miny

    if last_dir is not None and last_dir != direction:
        if last_dir + direction in ("RD", "UL"):
            holes2[h] = "7"
        elif last_dir + direction in ("LD", "UR"):
            holes2[h] = "F"
        elif last_dir + direction in  ("DL", "RU"):
            holes2[h] = "J"
        elif last_dir + direction in ("DR", "LU"):
            holes2[h] = "L"
        else:
            raise ValueError("")

    last_dir = direction
    
    for i in range(number):
        if direction == "R":
            h = h[0], h[1]+1
            holes2[h] = "-"
        elif direction == "L":
            h = h[0], h[1]-1
            holes2[h] = "-" 
        elif direction == "D":
            h = h[0]+1, h[1]
            holes2[h] = "|" 
        elif direction == "U":
            h = h[0]-1, h[1]
            holes2[h] = "|" 


def vertical_count(line):
    count = 0
    l = ""
    for x in line:
        if x == "-":
            count += 1
        elif x in "FJL7":
            if not l:
                l += x
            else:
                l += x
                if l in ("7L", "FJ"):
                    count  += 1
                l = ""
    return count 

def horizontal_count(line):
    count = 0
    l = ""
    for x in line:
        if x == "|":
            count += 1
        elif x in "FJL7":
            if not l:
                l += x
            else:
                l += x
                if l in ("L7", "FJ"):
                    count  += 1
                l = ""
    return count 



def is_inside(i, j):
    left_side = horizontal_count(holes2[i][:j])
    right_side = horizontal_count(holes2[i][j+1:])

    up_side = vertical_count(holes2[:i, j])
    down_side = vertical_count(holes2[i+1:, j])
    if left_side % 2 == 1 and right_side % 2 == 1 and up_side % 2 == 1 and down_side % 2 ==1:
        return True
    return False
            
print(holes2)

count = border 
for i, line in enumerate(holes2):
    for j, x in enumerate(line):
        if x == ".":
            if is_inside(i, j):
                count += 1
                holes2[i, j] = "x"
            else:
                holes2[i, j] = "o"
    
print(count)

print(holes2)

for line in holes2:
    print("".join([x for x in line]))
