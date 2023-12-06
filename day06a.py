with open("input6.txt", "r") as f:
    lines = f.readlines()

    time = lines[0].split(":")[1]
    time = "".join([t for t in time if t.isdigit()])
    time = int(time)

    distance = lines[1].split(":")[1]
    distance = "".join([d for d in distance if d.isdigit()])
    distance = int(distance)

def num_choices(time, dist):
    n = 0
    for t in range(time):
        speed = t
        time_left = time - t

        moved = speed * time_left
        if moved > dist:
            n += 1
    return n

result = num_choices(time, distance)

print(result)
