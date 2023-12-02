RED = 12 
GREEN = 13
BLUE =  14

def is_valid(cube):
    number, color = cube.strip().split(" ")
    if color == "red":
        return int(number) <= RED
    if color == "green":
        return int(number) <= GREEN
    if color == "blue":
        return int(number) <= BLUE

def process(line):
    first_part, second_part = line.strip().split(":")
    number = int(first_part.split(" ")[1])

    draws = second_part.split(";")
    for draw in draws:
        cubes = draw.split(",")
        for cube in cubes:
            if not is_valid(cube):
                return 0
    return number

with open("input2.txt", "r") as f:
    sum = 0
    for line in f:
        sum += process(line)

print(sum)
