
def process(line):
    card, lists = line.strip().split(":")
    first, second = lists.split("|")
    first_list = list(map(int, first.split()))
    second_list = list(map(int, second.split()))

    number = int(card.split()[1])
    
    return number, first_list, second_list 

def winning_number(first, second):
    count = 0
    for number in second:
         if number in first:
             count += 1
    return count 

cards = {}
with open("input4.txt", "r") as f:
    for line in f:
        number, first, second = process(line)
        cards[number] = (1, first, second)

num = 1
while num < max(cards.keys()):
    count = winning_number(cards[num][1], cards[num][2])
    copies = cards[num][0]
    
    for i in range(1, count+1):
        n = num + i
        count, f, s = cards[n]
        cards[n] = count + copies, f, s
    num += 1

sum_ = 0
for card in cards.values():
    sum_ += card[0]

print(sum_)
