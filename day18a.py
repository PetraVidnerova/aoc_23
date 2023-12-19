import numpy as np
from tqdm import tqdm

# from day08a import get_members
from scipy.sparse import lil_matrix, csr_matrix


dig_plan = []

with open("input18.txt", "r") as f:
    for line in f:
        line = line.strip()
        direction, number, color = line.split()
        color = color[1:-1]
        direction = "RDLU"[int(color[-1])]
        distance = int("0x"+color[1:-1], 16)

        
        dig_plan.append((direction, distance))

print(dig_plan)
# for direction, distance in dig_plan:
#     print(direction, distance, ":", end="")
#     m = get_members(distance)
#     print(m)
# exit()
        
holes = set()

h = (0,0)

maxx = 0
maxy = 0
minx = 0
miny = 0

HORIZONTAL_LINE = 1
VERTICAL_LINE = 2
F = 3
F7 = 4
L = 5
J = 6

L7 = "54"
FJ = "36"

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
assert h == (0, 0)
            
print(len(holes))
print(minx, miny)
print(maxx, maxy, flush=True)

border = len(holes) 


holes = lil_matrix((maxx-minx+1, maxy-miny+1), dtype="uint8")
print(holes)

last_dir = dig_plan[-1][0]
h = (-minx, -miny)
for direction, number in tqdm(dig_plan):
    assert h[0] >= 0
    assert h[1] >= 0
    assert h[0] <= maxx-minx
    assert h[1] <= maxy-miny

    if last_dir != direction:
        if last_dir + direction in ("RD", "UL"):
            holes[h[0],h[1]] =  F7
        elif last_dir + direction in ("LD", "UR"):
            holes[h[0],h[1]] =  F 
        elif last_dir + direction in  ("DL", "RU"):
            holes[h[0],h[1]] = J
        elif last_dir + direction in ("DR", "LU"):
            holes[h[0],h[1]] =  L
        else:
            raise ValueError("")
    else:
        if direction in "RL":
            holes[h[0],h[1]] = HORIZONTAL_LINE
        else:
            holes[h[0],h[1]] = VERTICAL_LINE

    last_dir = direction

    if direction == "R":
        holes[h[0], h[1]+1:h[1]+number] = HORIZONTAL_LINE
        h = h[0], h[1]+number
    elif direction == "L":
        holes[h[0], h[1]-number+1:h[1]] = HORIZONTAL_LINE
        h = h[0], h[1]-number
    elif direction == "D":
        holes[h[0]+1:h[0]+number, h[1]] = VERTICAL_LINE
        h = h[0]+number, h[1]
    elif direction == "U":
        holes[h[0]-number+1:h[0], h[1]] = VERTICAL_LINE
        h = h[0]-number, h[1]

        
            
print("converting lil to csr", flush=True)           
holes = csr_matrix(holes)
print("matrix ready")


count = border 
for i in tqdm(range(0, -minx+maxx+1)):
    lc = 0
    barier = ""
    row_start  = holes.indptr[i]
    row_end = holes.indptr[i+1]
#    row_columns = list(holes.indices[row_start: row_end])
    
    # for j in range(0, -miny+maxy+1):
    j_old = 0
    for x, j  in zip(holes.data[row_start: row_end], holes.indices[row_start: row_end]):
        if barier == "":
            count += (j-j_old)*lc
        if x == VERTICAL_LINE:
            lc = (lc+1)%2
        elif x in (L, F, J, F7):
            if not barier:
                barier +=  str(x)
            else:
                barier +=  str(x)
                print(barier)
                if barier in ( L7 ,  FJ ):
                    lc = (lc+1)%2
                barier = ""
        j_old = j+1
        
print(count)

