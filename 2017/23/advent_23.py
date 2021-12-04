from pprint import pprint


def parse_input(filename):
    with open(filename) as f:
        instructions = []
        for line in f:
            args = line.split()
            arg1 = args[1]
            arg2 = args[2]
            try:
                arg2 = int(arg2)
            except ValueError:
                pass
            try:
                arg1 = int(arg1)
            except ValueError:
                pass

            instructions.append((args[0], arg1, arg2))
        return instructions


def solve(instructions, max_steps):
    registers = {}
    counter, i, step = 0, 0, 0
    while i < len(instructions) and step < max_steps:
        step += 1
        # print('[i={}]: {}'.format(i, instructions[i]))
        command, arg1, raw_arg2 = instructions[i]
        if isinstance(arg1, str) and registers.get(arg1) is None:
            registers[arg1] = 0

        if raw_arg2 is not None:
            if isinstance(raw_arg2, str):
                if registers.get(raw_arg2) is None:
                    registers[raw_arg2] = 0
                arg2 = registers.get(raw_arg2)
            else:
                arg2 = raw_arg2

        if command == 'set':
            registers[arg1] = arg2
        elif command == 'sub':
            registers[arg1] -= arg2
        elif command == 'mul':
            registers[arg1] *= arg2
            counter += 1
        elif command == 'jnz':
            if (isinstance(arg1, str) and registers[arg1] != 0) or (isinstance(arg1, int) and arg1 != 0):
                i += (arg2 - 1)
        i += 1

    return registers, counter, step


def optimized():
    import math
    h = 0
    for b in range(106700, 123701, 17):
        if b % 2 == 0:
            h += 1
            continue
        for i in range(3, int(math.sqrt(b) + 1), 2):
            if b % i == 0:
                h += 1
                break
    return h


def main():
    instructions = parse_input('advent23_input.txt')
    print(solve(instructions, 500_000))
    print(optimized())


if __name__ == '__main__':
    main()
