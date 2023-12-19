platform = []
with open("input14.txt", "r") as f:
    for line in f:
        platform.append(list(line.strip()))

for line in platform:
    print(line)
    
def move_block(i, j):
    print(i, j)

    while new_platform[i][j] == "." and i>=0:
        i -= 1
    i += 1
    new_platform[i][j] = "O"


new_platform = [p.copy() for p in platform]    
for i, line in enumerate(platform):
    if i == 0:
        continue
    for j, block in enumerate(line):
        print(block)
        if block == "O":
            new_platform[i][j] = "."
            move_block(i, j)

for line in new_platform:
    print(line)
    

result = 0
for i, line in enumerate(new_platform):
    for block in line:
        if block == "O":
            result += len(new_platform)-i
            
print(result)
