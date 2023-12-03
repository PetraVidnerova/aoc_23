machine = []

with open("input3.txt", "r") as f:
    for line in f:
        machine.append(line.strip())

MAX_X = len(machine)-1
MAX_Y = len(machine[0])-1
        

def find_next_number(x, y):
    while not machine[x][y].isdigit():
        y += 1
        if y > MAX_Y:
            x += 1
            y = 0
        if x > MAX_X:
            raise ValueError("End of machine")
    return x, y

def find_number_end(x, y):
    while y<=MAX_Y and machine[x][y].isdigit():
        y += 1
    return x, y

def is_symbol(x, y):
    return machine[x][y] != "." and not machine[x][y].isdigit()

def get_neighbor(x, y):
    if x > 0:
        yield x-1, y
        if y > 0:
            yield x-1, y-1
        if y < MAX_Y:
            yield x-1, y+1

    if y > 0:
        yield x, y-1
    if y < MAX_Y:
        yield x, y+1

    if x < MAX_X:
        yield x+1, y
        if y > 0:
            yield x+1, y-1
        if y < MAX_Y:
            yield x+1, y+1
            

def neighbor(x, y):
    for a, b in get_neighbor(x, y):
        if is_symbol(a, b):
            return True
    return False
    
def is_neighbor(x_s, y_s, y_e):
    for y in range(y_s, y_e):
        if neighbor(x_s, y):
            return True
    return False

x = 0
y = 0
sum = 0
while True:
    try:
        x_s, y_s = find_next_number(x, y)
    except ValueError:
        break
    x_e, y_e = find_number_end(x_s, y_s)
    number = int(machine[x_s][y_s:y_e])

    if is_neighbor(x_s, y_s, y_e):
        sum += number
    
    if y_e > MAX_Y:
        x_e = x_e + 1
        y_e = 0
    if x_e > MAX_X:
        break
    x, y = x_e, y_e

print(sum)
