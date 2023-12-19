from itertools import combinations

image = []
lines_to_replicate = []
with open("input11.txt", "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        image.append(list(line))
        if "#" not in line:
            lines_to_replicate.append(i)
    

columns_to_replicate = []
for col in range(len(image[0])):
    if "#" not in [line[col] for line in image]:
        columns_to_replicate.append(col)

                
galaxies = []
for i, line in enumerate(image):
    for j, x in enumerate(line):
        if x == "#":
            galaxies.append((i, j))

            

            
def shortest(x, y):
    path = 0
    i1, j1 = x
    i2, j2 = y

    if i1 > i2:
        i1, i2 = i2, i1
    while i1 < i2:
        i1 = i1 + 1
        if i1 in lines_to_replicate:
            path += 1000000
        else:
            path += 1

    if j1 > j2:
        j1, j2 = j2, j1
    while j1 < j2:
        j1 += 1
        if j1 in columns_to_replicate:
            path += 1000000
        else:
            path += 1

    return path

count = 0
print(len(list(combinations(galaxies, 2))))
for x, y in combinations(galaxies, 2):
    count += shortest(x, y)
print(count)
        
