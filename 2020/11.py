from functools import reduce
from collections import Counter
from pprint import pprint
from itertools import product, starmap, chain

INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    rows = []
    with open(INPUT_NAME) as file:
        for line in file:
            rows.append([c for c in line.strip()])
    return rows

def in_bounds(data, pos):
    r, c = pos
    max_r, max_c = len(data), len(data[0])
    return 0 <= r < max_r and 0 <= c < max_c

def safe_get(data, r, c):
    if not in_bounds(data, (r,c)):
        return None
    return data[r][c]

def first_chair_in_line(data, pos, delta):
    cur = (pos[0] + delta[0], pos[1] + delta[1])
    while in_bounds(data, cur):
        val = data[cur[0]][cur[1]]
        if val in ['L', '#']:
            return val
        cur = (cur[0] + delta[0], cur[1] + delta[1])
    return None

def simple_around(data, r, c):
    around_positions = [pos for pos in product(range(r-1, r+2), range(c-1, c+2)) if pos != (r,c)]
    return [safe_get(data, r, c) for r, c in around_positions]

def complex_around(data, r, c):
    deltas = [x for x in product(range(-1, 2), range(-1, 2)) if x != (0,0)]
    return [first_chair_in_line(data, (r,c), delta) for delta in deltas]

def process(original_data, get_around, empty_predicate, taken_predicate):
    data = original_data[:]
    rows, columns = len(data), len(data[0])
    changed = True
    while changed:
        after = [r[:] for r in data]
        changed = False
        for r, c in product(range(rows), range(columns)):
            around = get_around(data, r, c)
            if data[r][c] == 'L' and empty_predicate(around):
                after[r][c] = '#'
                changed = True
            if data[r][c] == '#' and taken_predicate(around):
                after[r][c] = 'L'
                changed = True
        data = after
    return sum(1 for c in chain.from_iterable(data) if c == '#')

def part_one(data):
    empty = lambda around: all((x != '#' for x in around))
    taken = lambda around: sum(1 for x in around if x == '#') >= 4
    return process(data, simple_around, empty, taken)

def part_two(data):
    empty = lambda around: all((x != '#' for x in around))
    taken = lambda around: sum(1 for x in around if x == '#') >= 5
    return process(data, complex_around, empty, taken)

def main():
    data = read_input()
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
