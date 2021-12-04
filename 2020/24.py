from functools import reduce
from collections import Counter,defaultdict, deque
from pprint import pprint
from itertools import product, starmap, chain
import string
import operator
import decimal
INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    tiles = []
    with open(INPUT_NAME, 'r') as file:
        for line in file:
            tokens = []
            buffer = []
            for c in line.strip():
                if c in 'sn':
                    buffer.append(c)
                    continue
                buffer.append(c)
                if buffer:
                    tokens.append(''.join(buffer))
                    buffer = []
            if buffer:
                tokens.append(''.join(buffer))
            tiles.append(tokens)
    return tiles


DELTAS = {
    'e': (1, 0),
    'se': (.5, -1),
    'sw': (-.5, -1),
    'w': (-1, 0),
    'nw': (-.5, 1),
    'ne': (.5,1),
}

def part_one(data):
    black = set()
    for tile in data:
        x, y = 0, 0
        for direction in tile:
            delta = DELTAS[direction]
            x += delta[0]
            y += delta[1]
        if (x,y) not in black:
            black.add((x,y))
        else:
            black.remove((x,y))
    return black


def part_two(black):
    max_x, min_x = max(v[0] for v in black), min(v[0] for v in black)
    max_y, min_y = max(v[1] for v in black), min(v[1] for v in black)

    print(f"x: {min_x}-{max_x}")
    print(f"y: {min_y}-{max_y}")
    print(black)

    for day in range(1, 101):
        to_change = []
        for y in range(min_y-1, max_y+2):
            x_type = 1 if y % 2 == 0 else 0.5
            if round(min_x) == min_x:
                if x_type == 1:
                    start = min_x-1
                else:
                    start = min_x-1.5
            else:
                if x_type == 1:
                    start = min_x-1.5
                else:
                    start = min_x-1
            
            x = start
            while x < max_x+2:
                neighbours = [(x+v[0], y+v[1]) for v in DELTAS.values()]
                black_neighbours = [tile for tile in neighbours if tile in black]
                if (x,y) in black and (len(black_neighbours) == 0 or len(black_neighbours) > 2):
                    to_change.append((x,y))
                elif (x,y) not in black and len(black_neighbours) == 2:
                    to_change.append((x,y))
                x+= 1
        for tile in to_change:
            if tile in black:
                black.remove(tile)
            else:
                black.add(tile)
        min_x -= 1
        max_x += 1
        min_y -= 1
        max_y += 1
        print(f'Day {day}: {len(black)}')


    pass

def main():
    data = read_input()
    black = part_one(data)
    print(f"Part one: {len(black)}")
    print(f"Part two: {part_two(black)}")

if __name__ == "__main__":
    main()
