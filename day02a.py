
def process_cube(cube, max_nums):
    ret = max_nums.copy()
    number, color = cube.strip().split(" ")
    number = int(number)
    if number > ret[color]:
        ret[color] = number
    return ret
    
def process(line):
    _, second_part = line.strip().split(":")
    max_nums = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    
    draws = second_part.split(";")
    for draw in draws:
        cubes = draw.split(",")
        for cube in cubes:
            max_nums  = process_cube(cube, max_nums)
    power = 1
    for k in max_nums.values():
        power *= k 
    return power

with open("input2.txt", "r") as f:
    sum = 0
    for line in f:
        sum += process(line)

print(sum)
