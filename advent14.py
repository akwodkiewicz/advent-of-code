# pylint: disable=C0103
# pylint: disable=C0111
from typing import List, Set, Tuple, Dict # pylint: disable=W0611

from advent10 import knot_hash_function


INPUT = 'hfdlxzhv'

def create_grid():
    # type: () -> List[str]
    grid = []
    for i in range(128):
        key = INPUT + '-' + str(i)
        hsh = knot_hash_function(key)
        bin_letters = ['{:04b}'.format(int(c, 16)) for c in hsh]
        row = ''.join(bin_letters)
        grid.append(row)
    return grid


def get_number_of_used_squares(grid):
    # type: (List[str]) -> int
    used_squares_count = 0
    for row in grid:
        for bit in row:
            if bit == '1':
                used_squares_count += 1
    return used_squares_count


def print_grid(grid):
    # type: (List[str]) -> None
    for row in grid:
        buffer = []
        for bit in row:
            if bit == '0':
                buffer.append('.')
            else:
                buffer.append('#')
        print(''.join(buffer))
    return


def print_grid_with_regions(grid_with_regions):
    # type: (Dict[Tuple[int, int], int]) -> None
    for y in range(127):
        buffer = []
        for x in range(127):
            buffer.append('{:^3}'.format(str(grid_with_regions.get((x, y), '.'))))
        print(''.join(buffer), flush=True)
    return


def find_regions(grid):
    # type: (List[str]) -> int

    grid_with_regions = {} # type: Dict[Tuple[int, int], int]
    visited = set() # type: Set[Tuple[int, int]]

    def find_one_region(x, y, i):
        # type: (int, int, int) -> None
        counter = 0
        visited.add((x, y))
        stack = [(x, y)]

        while len(stack) > 0:   # pylint: disable=C1801
            cur_x, cur_y = stack[-1]
            stack.remove((cur_x, cur_y))
            grid_with_regions[(cur_x, cur_y)] = i
            counter += 1

            if cur_x > 0 and (cur_x-1, cur_y) not in visited and grid[cur_y][cur_x-1] == '1':
                stack.append((cur_x-1, cur_y))
                visited.add((cur_x-1, cur_y))
            if cur_y > 0 and (cur_x, cur_y-1) not in visited and grid[cur_y-1][cur_x] == '1':
                stack.append((cur_x, cur_y-1))
                visited.add((cur_x, cur_y-1))
            if cur_x < 127  and (cur_x+1, cur_y) not in visited and grid[cur_y][cur_x+1] == '1':
                stack.append((cur_x+1, cur_y))
                visited.add((cur_x+1, cur_y))
            if cur_y < 127 and (cur_x, cur_y+1) not in visited and grid[cur_y+1][cur_x] == '1':
                stack.append((cur_x, cur_y+1))
                visited.add((cur_x, cur_y+1))

        return

    region_num = 0
    for y in range(128):
        for x in range(128):
            if (x, y) in visited or grid[y][x] == '0':
                continue
            region_num += 1
            find_one_region(x, y, region_num)
    print_grid_with_regions(grid_with_regions)

    return region_num

g = create_grid()
print('Part 1: number_of_used_squares = {}'.format(get_number_of_used_squares(g)))
print('Part 2: num_of_regions = {}'.format(find_regions(g)))
