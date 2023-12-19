from copy import deepcopy

loss_map = [] 
with open("input17.txt", "r") as f:
    for line in f:
        line = line.strip()
        loss_map.append(list(map(int, line)))

MAXX = len(loss_map)-1
MAXY = len(loss_map[0])-1

visited = {}

def min_to_end(x, y):
    min_ = min(loss_map[x][y:])
    for i in range(x+1, MAXX+1):
        m = min(loss_map[i][y:])
        if m < min_:
            min_ = m
    return min_

min_map = [] 
for i, line in enumerate(loss_map):
    min_line = []
    for j, x in enumerate(line):
        min_line.append(min_to_end(i, j))
    min_map.append(min_line)

print(min_map)
    
def min_cost_path(path):
    x, y = path.path[-1]
    return ((MAXX-x) + (MAXY-y))*min_map[x][y]
        
class Path:
    def __init__(self, x, y):
        self.cost = 0
        self.path = [(x, y)]
        self.direction = "R"
        self.same_dir = 0

    def finished(self):
        if self.path[-1] == (MAXX, MAXY):
            return True
        return False
        
    def turn_left(self):
        left = {"R": "U",
                "U": "L",
                "L": "D",
                "D": "R"}
        self.direction = left[self.direction]
        self.same_dir = 0

    def turn_right(self):
        right = {"R": "D",
                 "D": "L",
                 "L": "U",
                 "U": "R"}
        self.direction = right[self.direction]
        self.same_dir = 0

    def move(self):
        if self.same_dir == 3:
            return False
        
        x, y = self.path[-1]
        if self.direction == "R":
            x, y = x, y+1
        elif self.direction == "L":
            x, y = x, y-1
        elif self.direction == "U":
            x, y = x-1, y
        elif self.direction == "D":
            x, y = x+1, y

        if 0 <= x <= MAXX and 0 <= y <= MAXY:
            key = (x, y, self.direction, self.same_dir)
            if key not in visited or visited[key] > self.cost:
                for k in range(self.same_dir, 3):
                    k = (key[0], key[1], key[2], k)
                    visited[k] = min([visited.get(k, self.cost), self.cost])
            
                self.cost += loss_map[x][y]
                self.path.append((x,y))
                self.same_dir += 1
                return True
        return False
        
stack = []
stack.append(Path(0, 0))


minimum = None
while stack:

    idx = 0
    min_l = None
    min_cost = None
    for i, p in enumerate(stack):
        l = (MAXX - p.path[-1][0]) + (MAXY - p.path[-1][1])
        if min_l is None or l < min_l or (l==min_l and p.cost < min_cost):
            idx = i
            min_l = l
            min_cost = p.cost 
        
    path = stack.pop(idx)

    
    if path.finished():
        if minimum is None or path.cost < minimum:
            minimum = path.cost
        print(path.cost, "         ", len(stack), 100*len(visited)/(MAXX*MAXY*4*3))
        continue

    # try direct
    path_dir = deepcopy(path)
    if path_dir.move():
        if minimum is None or path_dir.cost+min_cost_path(path_dir) < minimum:
            stack.append(path_dir)

    # try left
    path_left = deepcopy(path)
    path_left.turn_left()
    if path_left.move():
        if minimum is None or path_left.cost+min_cost_path(path_left) < minimum:
            stack.append(path_left)

    # try right
    path_right = deepcopy(path)
    path_right.turn_right()
    if path_right.move():
        if minimum is None or path_right.cost+min_cost_path(path_right) < minimum:
            stack.append(path_right)
