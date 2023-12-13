from itertools import product

def is_valid(springs, counts):
    l = 0
    new_counts = []
    for x in springs:
        if x == "#":
            l += 1
        elif x == "." and l > 0:
            new_counts.append(l)
            l = 0
    if l>0:
        new_counts.append(l)
    return new_counts == counts

def num_choices(springs, counts):
    n = springs.count("?")
    count = 0
    for setup in product(".#", repeat=n):
        new_springs = ""
        i = 0
        for x in springs:
            if x == "?":
                new_springs += setup[i]
                i += 1
            else:
                new_springs += x
        if is_valid(new_springs, counts):
            count += 1
    return count


def process_line(line):
    line = line.strip()
    springs, counts = line.split()
    counts = list(map(int, counts.split(",")))
    
    return num_choices(springs, counts)
    
result = 0
with open("input12.txt", "r") as f:
    for line in f:
        result += process_line(line)
print(result)

