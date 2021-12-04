from pprint import pprint
from itertools import tee


def parse_input(filename):
    grid = {}
    with open(filename) as file:
        iter1, iter2 = tee(file)
        width = len(next(iter1)) - 1
        d = width // 2 
        for y, line in enumerate(iter2):
            for x, char in enumerate(line):
                if char == '\n':
                    continue
                grid[(x-d, -(y-d))] = char
    return grid


def activate_virus(grid, bursts):
    infection_bursts_num = 0
    x, y = 0, 0
    vel_x, vel_y = 0, 1

    right_turn = {
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1)
    }

    left_turn = dict((v, k) for k, v in right_turn.items())

    for burst in range(bursts):
        # print_grid(grid)
        if grid.get((x,y)) == '.' or not grid.get((x,y)):
            vel_x, vel_y = left_turn[vel_x, vel_y]
            grid[(x,y)] = '#'
            infection_bursts_num += 1
        else:
            vel_x, vel_y = right_turn[vel_x, vel_y]
            grid[(x,y)] = '.'
        
        x += vel_x
        y += vel_y
        
    return infection_bursts_num


def activate_virus2(grid, bursts):
    infection_bursts_num = 0
    x, y = 0, 0
    vel_x, vel_y = 0, 1

    right_turn = {
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1)
    }

    left_turn = dict((v, k) for k, v in right_turn.items())

    for burst in range(bursts):
        if grid.get((x,y)) == '.' or not grid.get((x,y)):
            vel_x, vel_y = left_turn[vel_x, vel_y]
            grid[(x,y)] = 'W'
        
        elif grid.get((x,y)) == 'W':
            grid[(x,y)] = '#'
            infection_bursts_num += 1

        elif grid.get((x,y)) == '#':
            vel_x, vel_y = right_turn[vel_x, vel_y]
            grid[(x,y)] = 'F'

        elif grid.get((x,y)) == 'F':
            vel_x, vel_y = -vel_x, -vel_y
            grid[(x,y)] = '.'
   
        x += vel_x
        y += vel_y
        
    return infection_bursts_num

def print_grid(grid):
    min_x = min(grid, key=(lambda k: k[0]))[0]
    min_y = min(grid, key=(lambda k: k[1]))[1]
    max_x = max(grid, key=(lambda k: k[0]))[0]
    max_y = max(grid, key=(lambda k: k[1]))[1]
    
    lines = []
    for y in range(max_y, min_y-1, -1):
        line = []
        for x in range(min_x, max_x + 1):
            char = grid.get((x, y), '.')
            line.append(char)
        lines.append(' '.join(line))
    printable = ''.join(line + '\n' for line in lines)
    print(printable)


def main():
    grid = parse_input('advent22_input.txt')
    result = activate_virus2(grid, 10000000)
    #print_grid(grid)
    print(result)


if __name__ == '__main__':
    main()