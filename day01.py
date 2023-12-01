def process(line):
    digits = [x for x in line if x.isdigit()]
    number = digits[0]+digits[-1]
    return int(number)

with open("input1.txt", "r") as f:
    sum = 0
    for line in f:
        sum += process(line)

print(sum)
