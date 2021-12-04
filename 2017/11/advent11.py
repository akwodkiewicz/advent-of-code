def move(instructions):
    x = 0
    y = 0
    maximum = 0
    for step in instructions:
        if step == 'n':
            y += 1
        elif step == 'ne':
            x += 0.5
            y += 0.5
        elif step == 'se':
            x += 0.5
            y -= 0.5
        elif step == 's':
            y -= 1
        elif step == 'sw':
            x -= 0.5
            y -= 0.5
        elif step == 'nw':
            x -= 0.5
            y += 0.5
        distance = count_steps(x, y)
        if distance > maximum:
            maximum = distance
    return x, y, maximum

def count_steps(x, y):
    small = min(abs(x), abs(y))
    large = max(abs(x), abs(y))
    diagonal_steps = small / 0.5
    straight_steps = large - small
    return diagonal_steps + straight_steps

import io
with open('advent11_input.txt') as f:
    instructions = f.readline().split(',')
    x, y, maximum = move(instructions)
    print('Part 1: hex_distance({}, {}) = {}'.format(x, y, count_steps(x, y)))
    print('Part 2: maximum_hex_distance = {}'.format(maximum))
