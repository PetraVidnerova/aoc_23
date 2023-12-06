with open("input6.txt", "r") as f:
    lines = f.readlines()

    times = lines[0].split(":")[1].split()
    times = list(map(int, times))
    
    distances = lines[1].split(":")[1].split()
    distances = list(map(int, distances))

def num_choices(time, dist):
    n = 0
    for t in range(time):
        speed = t
        time_left = time - t

        moved = speed * time_left
        if moved > dist:
            n += 1
    return n

result = 1
for time, dist in zip(times, distances):
    result *= num_choices(time, dist)


print(result)
