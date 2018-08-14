
def solve(instructions):
    registers = {}
    samples = []
    i = 0
    while True:
        command, arg1, raw_arg2 = instructions[i]
        
        if registers.get(arg1) is None:
            registers[arg1] = 0

        if raw_arg2 is not None:    
            if type(raw_arg2) is not int:
                if registers.get(raw_arg2) is None:
                    registers[raw_arg2] = 0
                arg2 = registers.get(raw_arg2)
            else:
                arg2 = raw_arg2

        if command == 'set':
            registers[arg1] = arg2
        elif command == 'add':
            registers[arg1] += arg2
        elif command == 'mul':
            registers[arg1] *= arg2
        elif command == 'mod':
            registers[arg1] = registers[arg1] % arg2
        elif command == 'jgz' and registers[arg1] > 0:
                i += (arg2 - 1)
        elif command == 'snd':
            samples.append(registers[arg1])
        elif command == 'rcv' and registers[arg1] > 0:
            return samples[-1]
        i += 1


def solve2(instructions):
    queue0, queue1 = [], []
    registers0, registers1 = {}, {}
    index0, index1 = 0, 0
    counter = 0

    def run_until_rcv(init_val, index, registers, own_queue, other_queue):
        nonlocal counter

        while True:
            command, arg1, raw_arg2 = instructions[index]


            if isinstance(arg1, str) and registers.get(arg1) is None:
                registers[arg1] = init_val

            if raw_arg2 is not None:    
                if isinstance(raw_arg2, str):
                    if registers.get(raw_arg2) is None:
                        registers[raw_arg2] = init_val
                    arg2 = registers.get(raw_arg2)
                else:
                    arg2 = raw_arg2

            if command == 'set':
                registers[arg1] = arg2
            elif command == 'add':
                registers[arg1] += arg2
            elif command == 'mul':
                registers[arg1] *= arg2
            elif command == 'mod':
                registers[arg1] = registers[arg1] % arg2
            elif command == 'jgz':
                if (isinstance(arg1, str) and registers[arg1] > 0) or (isinstance(arg1, int) and arg1 > 0):
                    index += (arg2 - 1)

            elif command == 'snd':
                if init_val == 1:
                    counter += 1
                if isinstance(arg1, str):
                    arg1 = registers[arg1]
                other_queue.append(arg1)

            elif command == 'rcv':
                if own_queue:
                    registers[arg1] = own_queue.pop(0)
                else:
                    return index
            index += 1


    index1 = run_until_rcv(1, index1, registers1, queue1, queue0)
    index0 = run_until_rcv(0, index0, registers0, queue0, queue1)

    while queue0 or queue1:
        index1 = run_until_rcv(1, index1, registers1, queue1, queue0)
        index0 = run_until_rcv(0, index0, registers0, queue0, queue1)

    return counter




with open('advent18_input.txt') as f:
    instructions = []
    for line in f:
        args = line.split()
        arg1 = args[1]
        if len(args) == 3:
            arg2 = args[2]
            try:
                arg2 = int(arg2)
            except Exception as e:
                pass
            try:
                arg1 = int(arg1)
            except Exception as e:
                pass
        else:
            arg2 = None
        instructions.append((args[0], arg1, arg2))
    print(solve(instructions))
    print(solve2(instructions))
