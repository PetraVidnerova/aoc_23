class Map():
    def __init__(self):
        self.ranges = []

    def add_range(self, dest, source, length):
        self.ranges.append((dest, source, length))

    def convert(self, couples):
        converted = []
        to_convert = couples
        while to_convert:
            couple = to_convert.pop(0)
            s, e = couple[0], couple[0]+couple[1]-1
            conv = False
            for r in self.ranges:
                if r[1] <= s and e < r[1]+r[2]:
                    converted.append((r[0] + s - r[1], e-s+1))
                    conv = True
                    break
                if r[1] <= s and s < r[1]+r[2]:
                    converted.append((r[0]+(s-r[1]), r[2]-(s-r[1])))
                    to_convert.append((r[1]+r[2], e-(r[1]+r[2])+1))
                    conv = True
                    break
                if r[1] <= e and e < r[1]+r[2]:
                    converted.append((r[0], e-r[1]+1))
                    to_convert.append((s, r[1]-s))
                    conv = True
                    break
                if  s < r[1] and e >= r[1]+r[2]:
                    converted.append((r[0], r[2]))
                    to_convert.append((s, r[1]-s))
                    to_convert.append((r[1]+r[2],e-(r[1]+r[2])+1))
                    conv = True
                    break
            if not conv:
                converted.append((s, e-s+1))
        return converted
       
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

seeds = [
    (seeds[i], seeds[i+1])
    for i in range(0, len(seeds), 2)
]
print(seeds)
            
lowest = None
for seed_couple in seeds:
    seed_couples = [seed_couple]
    for m in maps:
        seed_couples = m.convert(seed_couples)
    l = min([s[0] for s in seed_couples])
    if lowest is None or l < lowest:
        lowest = l

    
print(lowest)
