from time import time
from itertools import combinations
from math import comb, factorial
#from multiprocessing import Pool
import json


        
def invalid(springs, counts):
    nx = springs.count("#")
    nq = springs.count("?")
    ndot = springs.count(".")

    totalx = sum(counts)
    nspaces = len(counts)-1

    free_q = nq + nx - totalx
    
    if free_q > nq:
        return True
        
    if  free_q < 0:
        return True

    if  ndot + free_q < nspaces:
        return True
    
    return False

        
def num_choices(springs, counts):

    assert "." not in springs

    assert "?" not in springs

    assert len(counts) == 1

    if len(springs) == counts[0]:
        return 1
    else:
        return 0
    

def central_index(s, c):
    idxs = []
    start = 0 
    while c in s[start:]:
        idxs.append(s.find(c, start))
        start = idxs[-1]+1
    return idxs[len(idxs)//2]

def rec_num_choices(springs, counts, r=0):

    sprints = springs.strip(".")
    
    
    if invalid(springs, counts):
        return 0
    
    assert springs
    assert counts
    
    if "." not in springs:
        if "?" in springs:
            idx  = central_index(springs, "?")
            num = 0
            assert springs[idx] == "?"
            new_springs = springs[:idx]+"."+springs[idx+1:]
            num += rec_num_choices(new_springs, counts, r=r+1)
            new_springs = springs[:idx]+"#"+springs[idx+1:]
            num += rec_num_choices(new_springs, counts, r=r+1)
            return num
        else:
            return num_choices(springs, counts)
    else:
        idx = springs.index(".")
        num = 0
        a, b = springs[:idx], springs[idx+1:]
        if "#" not in b:
            num += rec_num_choices(a, counts)
        if "#" not in a:
            num += rec_num_choices(b, counts)
        for n in range(1, len(counts)):
            if invalid(a, counts[:n]) or invalid(b, counts[n:]):
                continue
            r1 = rec_num_choices(a, counts[:n])
            if r1 != 0:
                r2 = rec_num_choices(b, counts[n:])
                num += r1*r2
        return num


def process_line(line):
    
    line = line.strip()
    springs, counts = line.split()
    counts = list(map(int, counts.split(",")))
    
    while ".." in springs:
        springs = springs.replace("..",".")
    
    springs = "?".join([springs for _ in range(5)])
    counts = counts*5
        
    r = rec_num_choices(springs, counts)
    print(r, flush=True)
    return r


with open("input12.txt", "r") as f:
    lines = f.readlines()

result = 0
for i, line in enumerate(lines):
    print(i, line)
    print(i, ":", end=" ")
    result += process_line(line)

    print(result)
    
print(result)
