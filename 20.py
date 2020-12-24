from functools import reduce
from collections import Counter,defaultdict
from pprint import pprint
from itertools import product, starmap, chain
import string
import operator
INPUT_NAME = __file__.split('.')[0]+'-input.txt'


class Tile:
    def __init__(self, lines):
        self.id = int(lines[0].split(' ')[1][:-1])
        self.data = [list(line) for line in lines[1:]]
        self.disposable_sides = [
            ''.join(self.data[0]), # top >
            ''.join(r[-1] for r in self.data), # right v
            ''.join(self.data[-1][::-1]), # bottom <
            ''.join(r[0] for r in self.data)[::-1], # left ^
        ]
        self.neighbours = [None, None, None, None]

    def __repr__(self):
        return f"<Tile {self.id}>"

    def __str__(self):
        return '\n'.join((''.join(r) for r in self.data))

    def sides(self):
        return [
            ''.join(self.data[0]), # top >
            ''.join(r[-1] for r in self.data), # right v
            ''.join(self.data[-1][::-1]), # bottom <
            ''.join(r[0] for r in self.data)[::-1], # left ^
        ]

    def top_side(self):
        return ''.join(self.data[0]), # top >
    
    def right_side(self):
        return ''.join(r[0] for r in self.data)[::-1]
    
    def bottom_side(self):
        return 

    def rotate_90(self):
        rows, columns = len(self.data), len(self.data[0])
        copy = [r[:] for r in self.data]
        for y, r in enumerate(self.data):
            for x, c in enumerate(r):
               copy[x][rows-1-y] = self.data[y][x]
        self.data = copy

    def mirror(self):
        self.data = [r[::-1] for r in self.data]

    def simple_match_tile(self, tile_to_match):
        for side_to_match_idx, side_to_match in enumerate(tile_to_match.sides()):
            for side_idx, side in enumerate(self.sides()):
                if side == side_to_match or side[::-1] == side_to_match:
                    self.disposable_sides[side_idx] =  None
                    tile_to_match.disposable_sides[side_to_match_idx] = None
                    return True
        return False           
    
    def match_tile(self, fixed_tile):
        # top w/ bottom
        if self.sides()[0] == fixed_tile.sides()[2]:
            self.neighbours[0] = fixed_tile
            fixed_tile.neighbours[2] = self
        # bottom w/ top
        if self.sides()[2] == fixed_tile.sides()[0]:
            self.neighbours[2] = fixed_tile
            fixed_tile.neighbours[0] = self

def read_input():
    tiles = []
    with open(INPUT_NAME) as file:
        buffer = []
        for line in file:
            if line.strip() == '':
                tiles.append(Tile(buffer))
                buffer = []
                continue
            buffer.append(line.strip())
        tiles.append(Tile(buffer))
    return tiles
  

def part_one(tiles):
    for tile in tiles:
        for candidate in tiles:
            if tile.id == candidate.id:
                continue
            tile.simple_match_tile(candidate)
    corners = list(tile.id for tile in tiles if tile.disposable_sides.count(None) == 2)
    return reduce(operator.mul, corners), corners


def part_two(tiles, corner_ids):
    pass

def main():
    tiles = read_input()
    result_one, corners = part_one(tiles)
    print(f"Part one: {result_one}")
    tiles = read_input()
    print(f"Part two: {part_two(tiles, corners)}")

if __name__ == "__main__":
    main()
