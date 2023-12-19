import numpy as np

blocks = []

with open("input13.txt", "r") as f:
    block = []
    for line in f.readlines()+[""]:
        line = line.strip()
        if not line:
            block = np.vstack(block)
            blocks.append(block)
            block = []
            continue
        lnum = [
            0 if x =="." else 1
            for x in line
        ]
        block.append(np.array(lnum))
        


def line_mirror(block, line):
    i = 0
    smudge = False
    while line-i >= 0 and (line+1+i) < block.shape[0]:
        s = sum(block[line-i, :] != block[line+1+i, :]) 
        if s == 0:
            i += 1
        elif s == 1 and not smudge:
            i += 1
            smudge = True
        else:
            break
    if not smudge:
        return False
    return i == line+1 or i == (block.shape[0]-line-1)
        

def find_vertical_mirror(block):
    nlines = block.shape[0]
    for line in range(0, nlines-1):
        if line_mirror(block, line):
            return line+1

result = 0
for block in blocks:
    vertical, horizontal = False, False

    res = find_vertical_mirror(block)
    if res:
        result += 100*res
        vertical = True
        
    res = find_vertical_mirror(block.T)
    if res:
        result += res
        horizontal = True

    assert not vertical or not horizontal
    assert vertical or horizontal
    
        
print(result)
