machine = []

with open("input3.txt", "r") as f:
    for line in f:
        machine.append(line.strip())

MAX_X = len(machine)-1
MAX_Y = len(machine[0])-1
        

def extend(x, y):
    y_s = y 
    while y_s>0 and machine[x][y_s-1].isdigit():
        y_s -= 1
    y_e = y
    while y_e<MAX_Y and machine[x][y_e+1].isdigit():
        y_e += 1
    return y_s, y_e

def get_numbers(x, s, e):
    number_str = "".join(
        c if c.isdigit() else " "
        for c in machine[x][s:e+1]
    )
    numbers = number_str.split()
    numbers = list(map(int, numbers))
    return numbers
    
def get_gear_numbers(x, y):
    numbers = []
    # line before
    if x > 0:
        y_s, y_e = extend(x-1, y)
    numbers += get_numbers(x-1, y_s, y_e)

    #my line
    y_s, y_e = extend(x, y)
    numbers += get_numbers(x, y_s, y_e)

    # line after 
    if x < MAX_X:
        y_s, y_e = extend(x+1, y)
    numbers += get_numbers(x+1, y_s, y_e)

    return numbers
    
def gear_ratio(x, y):
    numbers = get_gear_numbers(x, y)
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    return 0

x = 0
y = 0
sum = 0
while x <= MAX_X:
    if machine[x][y] == "*":
        sum += gear_ratio(x, y)
    y += 1
    if y > MAX_Y:
        x += 1
        y = 0

    
print(sum)
