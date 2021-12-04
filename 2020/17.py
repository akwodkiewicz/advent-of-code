from functools import reduce
from collections import Counter,defaultdict
from pprint import pprint
from itertools import product, starmap, chain

INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input_3d():
    universe = {}
    with open(INPUT_NAME) as file:
        y, z = 0, 0
        for line in file:
            for x, v in enumerate(line.strip()):    
                key = str((x,y,z))
                universe[key] = True if v =='#' else False
            y += 1
    return universe

def read_input_4d():
    universe = {}
    with open(INPUT_NAME) as file:
        y, z, w = 0, 0, 0
        for line in file:
            for x, v in enumerate(line.strip()):    
                key = str((x,y,z,w))
                universe[key] = True if v =='#' else False
            y += 1
    return universe

def get_around(center_pos):
    ranges = [range(dim-1, dim+2) for dim in center_pos]
    return filter(lambda pos: pos != center_pos, product(*ranges))

def universe_iterator(data: dict):
    keys = [tuple(map(int, (key[1:-1].split(', ')))) for key in data.keys()]
    ranges = [range(min(dim)-1, max(dim)+2) for dim in zip(*keys)]
    return product(*ranges)

def process(data):
    for step in range(6):
        changes = []
        for pos in universe_iterator(data):
            key = str(pos)
            value = data.get(key, False)
            around = [data.get(str(p), False) for p in get_around(pos)]
            if value and around.count(True) not in [2,3]:
                changes.append(key)
            elif not value and around.count(True) == 3:
                changes.append(key)
        for key in changes:
            data[key] = not data.get(key, False)
  
    return list(data.values()).count(True)

def main():
    data_3d, data_4d = read_input_3d(), read_input_4d()
    print(f"Part one: {process(data_3d)}")
    print(f"Part two: {process(data_4d)}")

if __name__ == "__main__":
    main()
