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

boxes = {i: {} for i in range(256)}
for step in steps:
    if "=" in step:
        label, number = step.split("=")
        action = "add"
    elif "-" in step:
        label, number = step.split("-")
        action = "remove"
    else:
        raise ValueError("missing separator")

    box_number = hash_alg(label)
    if action == "add": 
        boxes[box_number][label] = number
    elif action == "remove":
        if label in boxes[box_number]:
            del boxes[box_number][label]

result = 0
for box_number, values in boxes.items():

    box_number += 1
    for i, number in enumerate(values.values()):
        result += box_number * (i+1) * int(number)


print(result)
