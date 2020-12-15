from functools import reduce
from collections import Counter
from pprint import pprint
import itertools
import operator
import math
import time
INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    data = {}
    with open(INPUT_NAME) as file:
        data['t'] = int(file.readline().strip())
        data['lines'] = [int(x) if x != 'x' else None for x in file.readline().strip().split(',')]
    return data

def part_one(data):
    t = data['t']
    lines = [line for line in data['lines'] if line is not None]
    delays = [line - (t % line) if (t % line) != 0 else 0 for line in lines]
    return min(delays) * lines[delays.index(min(delays))]


def part_two(data):
    raw_lines: list = data['lines']
    modulos = [line for line in raw_lines if line is not None]
    remainders = [raw_lines.index(line) for line in modulos]
    
    t = remainders[0]
    delta = modulos[0]
    i = 1
    while i < len(modulos):
        t += delta
        while i < len(modulos) and (t + remainders[i]) % modulos[i] == 0:
            delta *= modulos[i]
            i += 1

    return t
        

def main():
    data = read_input()
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
