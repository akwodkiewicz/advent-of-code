INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    instructions = []
    with open(INPUT_NAME) as file:
        for line in file:
            data = line.strip().split(' ')
            instructions.append((data[0], int(data[1])))
    return instructions

def part_one(data):
    used_ptrs = set()
    ptr = 0
    acc = 0
    while ptr < len(data):
        instr, arg = data[ptr]
        if ptr in used_ptrs:
            return acc, False
        used_ptrs.add(ptr)
        if instr == 'acc':
            acc += arg
            ptr += 1
        elif instr == 'jmp':
            ptr += arg
        elif instr == 'nop':
            ptr += 1
    return acc, True

def part_two(data):
    substitutes = { 'jmp': 'nop', 'nop': 'jmp'}
    for ptr in range(len(data)):
        instr, arg = data[ptr]
        if instr in substitutes.keys():
            data_copy = data[:]
            data_copy[ptr] = (substitutes[instr], arg)
            acc, is_terminated = part_one(data_copy)
            if is_terminated:
                return acc
    return None

def main():
    data = read_input()
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
    