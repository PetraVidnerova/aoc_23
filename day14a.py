import tqdm

platform = []
with open("input14.txt", "r") as f:
    for line in f:
        platform.append(list(line.strip()))

for line in platform:
    print(line)

def platform_to_string(platform):
    return "".join([
            "".join(line)
            for line in platform
        ])
    
def move_north(platform): 
    
    def move_block(i, j):
        while i>=0 and new_platform[i][j] == ".":
            i -= 1
        i += 1
        new_platform[i][j] = "O"


    new_platform = [p.copy() for p in platform]    
    for i, line in enumerate(platform):
        if i == 0:
            continue
        for j, block in enumerate(line):
            if block == "O":
                new_platform[i][j] = "."
                move_block(i, j)
    return new_platform
                
def move_south(platform): 
    
    def move_block(i, j):
        while  i<len(new_platform) and new_platform[i][j] == ".":
            i += 1
        i -= 1
        new_platform[i][j] = "O"


    new_platform = [p.copy() for p in platform]    
    for i, line in enumerate(platform[::-1]):
        if i == 0:
            continue
        for j, block in enumerate(line):
            if block == "O":
                new_platform[len(platform)-i-1][j] = "."
                move_block(len(platform)-i-1, j)
    return new_platform


def move_west(platform): 
    
    def move_block(i, j):
        while j>=0 and new_platform[i][j] == ".":
            j -= 1
        j += 1
        new_platform[i][j] = "O"


    new_platform = [p.copy() for p in platform]
    for j in range(len(platform[0])):
        if j == 0:
            continue
        for i in range(len(platform)):
            if platform[i][j] == "O":
                new_platform[i][j] = "."
                move_block(i, j)
    return new_platform


def move_east(platform): 
    
    def move_block(i, j):
        while j<len(new_platform[0]) and new_platform[i][j] == ".":
            j += 1
        j -= 1
        new_platform[i][j] = "O"


    new_platform = [p.copy() for p in platform]    
    for j in range(len(platform[0])):
        if j == 0:
            continue
        for i in range(len(platform)):
            if platform[i][len(platform[0])-j-1] == "O":
                new_platform[i][len(platform[0])-j-1] = "."
                move_block(i, len(platform[0])-j-1)
    
    return new_platform



history_dict = {}
history_dict[platform_to_string(platform)] = 0

cycle = 0
while cycle < 1000000000:
    cycle += 1
    for func in move_north, move_west, move_south, move_east:
        platform = func(platform)
    s = platform_to_string(platform)
    if s in history_dict:
        print("HEUREKA")
        print(cycle, history_dict[s])
        period = cycle - history_dict[s]
        while cycle + period < 1000000000:
            cycle += period
        history_dict = {}    
    history_dict[s] = cycle        
        
print()
for line in platform:
    print(line)
    

result = 0
for i, line in enumerate(platform):
    for block in line:
        if block == "O":
            result += len(platform)-i
            
print(result)
