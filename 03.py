from functools import reduce

INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    lines = []
    with open(INPUT_NAME) as file:
        for line in file:
            lines.append([True if x == '#' else False for x in line.strip()])
    return lines


def part_one(data, dx=3, dy=1):
    trees = 0
    pos_x = 0
    pos_y = 0
    while pos_y < len(data):
        if data[pos_y][pos_x]:
            trees += 1
        pos_x = (pos_x + dx) % len(data[pos_x])
        pos_y += dy
    return trees


def part_two(data):
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    return reduce(lambda x,y: x*y, [part_one(data, dx, dy) for (dx, dy) in slopes])


def main():
    data = read_input()
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
    