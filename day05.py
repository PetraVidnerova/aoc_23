class Map():
    def __init__(self):
        self.ranges = []

    def add_range(self, dest, source, length):
        self.ranges.append((dest, source, length))

    def convert(self, number):
        for r in self.ranges:
            if r[1] <= number < r[1]+r[2]:
                return r[0] + number - r[1]
        return number
       
maps = []
seeds = [] 
with open("input5.txt", "r") as f:
    map_started = False
    for line in f:
        if line.strip() == "":
            map_started = False
        elif map_started:
            d, s, l = line.strip().split()
            maps[-1].add_range(int(d), int(s), int(l))
        elif line.startswith("seeds"):
            seeds = list(map(int, line.strip().split(":")[1].split()))
        elif line.strip().endswith("map:"):
            maps.append(Map())
            map_started = True


lowest = None
for seed in seeds:
    converted_seed = seed
    for m in maps:
        converted_seed = m.convert(converted_seed)
    if lowest is None or converted_seed < lowest:
        lowest = converted_seed

print(lowest)
