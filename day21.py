field = []

with open("input21.txt", "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if "S" in line:
            j = line.index("S")
            line = line.replace("S", ".")
            start = (i, j)
        field.append(list(line))



stack = [(start, 0)]
finished = set()

while stack:
    new_stack = set()

    while stack:
        
        pos, count = stack.pop()
        
        print(count)
        
        if count == 64:
            finished.add(pos)
            continue

        for x, y in (
                (pos[0], pos[1]+1),
                (pos[0], pos[1]-1),
                (pos[0]+1, pos[1]),
                (pos[0]-1, pos[1])
        ):
            if field[x][y] == ".":
                new_stack.add(((x,y), count+1))

    stack = new_stack
    
print(len(finished))
