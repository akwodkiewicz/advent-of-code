from functools import reduce
from collections import Counter, defaultdict
from pprint import pprint
from itertools import product, starmap, chain
INPUT_NAME = __file__.split('.')[0]+'-input.txt'


def read_input():
    operations = []
    with open(INPUT_NAME) as file:
        for line in file:
            tokens = line.strip().split()
            if tokens[0] == 'mask':
                operations.append((None, tokens[2]))
            else:
                operations.append((int(tokens[0][4:-1]), int(tokens[2])))
    return operations

def part_one(data):
    registers = defaultdict(int)
    for addr, val in data:
        if addr is None:
            mask = val
            ones_mask = int(mask.replace('X', '0'), 2)
            zeros_mask = int(mask.replace('X', '1'), 2)
        else:
            registers[addr] = (val & zeros_mask) | ones_mask
    return sum(registers.values())

def generate_addr(val: str):
    if 'X' not in val:
        yield int(val, 2)
    else:
        yield from generate_addr(val.replace('X', '0', 1))
        yield from generate_addr(val.replace('X', '1', 1))

def part_two(data):
    registers = defaultdict(int)
    for addr, val in data:
        if addr is None:
            mask = val
            ones_mask = int(mask.replace('X', '0'), 2)
        else:
            intermediary = "{0:036b}".format(addr | ones_mask)
            masked_addr = ''.join([intermediary[i] if mask[i] != 'X' else 'X' for i in range(36)])
            for addr in generate_addr(masked_addr):
                registers[addr] = (val)            
    return sum(registers.values())
   
def main():
    data = read_input()
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
