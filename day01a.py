valid_digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

def convert(triple):
    if triple[2] == "digit":
        return int(triple[1])
    elif triple[2] == "word":
        return valid_digits.index(triple[1]) + 1
    else:
        raise ValueError()

def process(line):
    digits = []
    digits = [(i, x, "digit") for i, x in enumerate(line) if x.isdigit()]

    for valid in valid_digits:
        start = 0
        while valid in line[start:]:
            digits.append((line.find(valid, start), valid, "word"))
            start = line.find(valid, start)+1
            
    digits.sort()

    first = convert(digits[0])
    last = convert(digits[-1])
            
    return first*10+last


with open("input1.txt", "r") as f:
    sum = 0
    for line in f:
        sum += process(line)

print(sum)
