with open("input15.txt", "r") as f:
    line = f.readlines()[0].strip()
    steps = line.split(",")

def hash_alg(step):
    result = 0
    for x in step:
        result += ord(x)
        result *= 17
        result %= 256
    return result

result = 0
for step in steps:
    result += hash_alg(step)

print(result)
    
