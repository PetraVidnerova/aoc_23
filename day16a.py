field = []
with open("input16.txt", "r") as f:
    for line in f:
        field.append(line.strip())


def next(x, y, direction):
    if direction == "R":
        return x, y+1
    if direction == "L":
        return x, y-1

    if direction == "U":
        return x-1, y
    if direction == "D":
        return x+1, y

def in_field(x, y):
    if x < 0:
        return False
    if x >= len(field):
        return False
    if y < 0:
        return False
    if y >= len(field[0]):
        return False
    return True
    
def new_direction(direction, symbol):
    if symbol == ".":
        yield direction
    elif direction+symbol in ("R-", "L-", "U|", "D|"):
        yield direction
    elif direction+symbol in ("R|", "L|"):
        yield "U"
        yield "D"
    elif direction+symbol in ("U-", "D-"):
        yield "L"
        yield "R"
    else:
        dirs = {
            "R\\": "D",
            "R/": "U",
            "L\\": "U",
            "L/": "D",
            "U\\": "L",
            "U/": "R",
            "D\\": "R",
            "D/": "L"
        }
        yield dirs[direction+symbol]
    

def number_energized(field, start, direction):

    energized = set()
    visited = set()

    beams = [ (start, direction)]
    
    while beams:
        beam = beams.pop(-1)
        (x, y), direction = beam

    
        x, y = next(x, y, direction)
        if in_field(x, y):
            energized.add((x, y))
            for new_dir in new_direction(direction, field[x][y]):
                if ((x,y), new_dir) not in visited:
                    beams.append(((x,y), new_dir))
                    visited.add(((x,y), new_dir))
            
    return len(energized)

start_points = (
    [ ((-1, j), "D") for j in range(len(field[0]))] +
    [ ((len(field), j), "U") for j in range(len(field[0]))] +
    [ ((i, -1), "R") for i in range(len(field))] +
    [ ((i, len(field[0])), "L") for i in range(len(field))]
)

maximum = 0
for start, direction in start_points:
    num = number_energized(field, start, direction)
    if num > maximum:
        maximum = num

print(maximum)
