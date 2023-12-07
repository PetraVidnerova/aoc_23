cards = {str(i): i for i in range(2, 10)} 
cards.update(
    {
        "A" : 14,
        "K" : 13,
        "Q" : 12,
        "J" : 11,
        "T" : 10
    }
)

hand_types = {
    (5,) : 7,
    (4, 1) : 6,
    (3, 2) : 5,
    (3, 1, 1) : 4,
    (2, 2, 1) : 3,
    (2, 1, 1, 1) : 2,
    (1, 1, 1, 1, 1) : 1
}

def convert(hand):
    return [cards[c] for c in hand]

def get_type(hand):
    counts = {}
    for c in hand:
        counts[c] = counts.get(c, 0) + 1
    values = tuple(sorted([v for v in counts.values()], reverse=True))
    return hand_types[values]
    
hands = []
bids = []

with open("input7.txt", "r") as f:
    for line in f:
        hand, bid = line.strip().split()
        hands.append((get_type(hand), convert(hand)))
        bids.append(int(bid))

hands = list(zip(hands, bids))
hands.sort()

sum = 0
for i, hand in enumerate(hands):
    sum += (i+1)*hand[1]
print(sum)
