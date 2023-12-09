def process(line):
    numbers = list(map(int, line.split()))

    sequences = [numbers]
    while not all([s == 0 for s in sequences[-1]]):
        s = sequences[-1]
        new_sequence = [val2-val1 for val1, val2 in zip(s[:-1], s[1:])]
        sequences.append(new_sequence)

    i = 1
    number_to_add = 0 
    while i < len(sequences):
        i += 1
        number_to_add = sequences[-i][0] - number_to_add

    return number_to_add
        
result = 0
with open("input9.txt", "r") as f:
    for line in f:
        result += process(line.strip())
print(result)
