from functools import reduce
from collections import Counter
from pprint import pprint
from itertools import product, starmap, chain, cycle
INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    instructions = []
    with open(INPUT_NAME) as file:
        for line in file:
            instructions.append((line[0], int(line.strip()[1:])))
    return instructions

DIRECTIONS_CLOCKWISE = 'NESW'

DELTAS = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0),
}

def turn_90(face_dir, turn_dir):
    idx = DIRECTIONS_CLOCKWISE.find(face_dir)
    if turn_dir == 'R':
        return DIRECTIONS_CLOCKWISE[(idx+1) % 4]
    else:
        return DIRECTIONS_CLOCKWISE[idx-1]

def part_one(data):
    pos_x, pos_y = 0, 0
    face_dir = 'E'

    for instruction, val in data:
        if instruction in DIRECTIONS_CLOCKWISE:
            delta = DELTAS[instruction]
            pos_x += delta[0] * val
            pos_y += delta[1] * val
        elif instruction in 'LR':
            while val > 0:
                val -= 90
                face_dir = turn_90(face_dir, instruction)
        else:
            forward = 1 if instruction == 'F' else -1
            delta = DELTAS[face_dir]
            pos_x += delta[0] * val * forward
            pos_y += delta[1] * val * forward
    return abs(pos_x) + abs(pos_y)

def part_two(data):
    pos_x, pos_y = 0, 0
    way_x, way_y = 10, 1

    for instruction, val in data:
        if instruction in DIRECTIONS_CLOCKWISE:
            delta = DELTAS[instruction]
            way_x += delta[0] * val
            way_y += delta[1] * val
        elif instruction in 'LR':
            while val > 0:
                val -= 90
                if instruction == 'R':
                    way_x, way_y = way_y, -way_x
                else:
                    way_x, way_y = -way_y, way_x
        elif instruction in 'FB':
            forward = 1 if instruction == 'F' else -1
            pos_x += way_x * val * forward
            pos_y += way_y * val * forward
    return abs(pos_x) + abs(pos_y)


def main():
    data = read_input()
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
