from itertools import combinations

image = []
with open("input11.txt", "r") as f:
    for line in f:
        line = line.strip()
        image.append(list(line))
        if "#" not in line:
            image.append(list(line))
    

columns_to_replicate = []
for col in range(len(image[0])):
    if "#" not in [line[col] for line in image]:
        columns_to_replicate.append(col)

new_image = []
for line in image:
    newline = "".join(
        [x if col not in columns_to_replicate else x*2
         for col, x in enumerate(line)]
    )
    new_image.append(list(newline))
image = new_image
        
for line in image:
    print(line)
        
galaxies = []
for i, line in enumerate(image):
    for j, x in enumerate(line):
        if x == "#":
            galaxies.append((i, j))

            

            
def shortest(x, y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

count = 0
print(len(list(combinations(galaxies, 2))))
for x, y in combinations(galaxies, 2):
    count += shortest(x, y)
print(count)
        
