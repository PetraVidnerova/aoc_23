
def process(line):
    _, lists = line.strip().split(":")
    first, second = lists.split("|")
    first_list = list(map(int, first.split()))
    second_list = list(map(int, second.split()))

    count = 0
    for number in second_list:
        if number in first_list:
            count += 1

    return 0 if count == 0 else 2**(count-1)


sum = 0 
with open("input4.txt", "r") as f:
    for line in f:
        sum += process(line)

print(sum)
