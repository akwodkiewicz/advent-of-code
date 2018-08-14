# pylint: disable=C0103
# pylint: disable=C0111
BILLION = 1_000_000_000

def process_instructions(file):
    data = file.read().split(',')
    instructions = []
    for raw in data:
        command = raw[0]
        if command == 's':
            arg1 = raw[1:]
            arg2 = None
        else:
            args = raw[1:].split('/')
            arg1 = args[0]
            arg2 = args[1]
        instructions.append((command, arg1, arg2))
    return instructions


def dance_round(instructions, dancers=None):
    if dancers is None:
        dancers = [chr(i) for i in range(ord('a'), ord('q'))]
    for command, arg1, arg2 in instructions:
        if command == 's':
            dancers = dancers[-int(arg1):] + dancers[:-int(arg1)]
        elif command == 'x':
            dancers[int(arg1)], dancers[int(arg2)] = dancers[int(arg2)], dancers[int(arg1)]
        elif command == 'p':
            a, b = dancers.index(arg1), dancers.index(arg2)
            dancers[a], dancers[b] = dancers[b], dancers[a]
    return dancers


def dance(instructions):
    init_dancers = [chr(i) for i in range(ord('a'), ord('q'))]
    dancers = init_dancers[:]
    for i in range(1, BILLION):
        dancers = dance_round(instructions, dancers)
        if dancers == init_dancers:
            cycle_length = i
            break
    rounds = BILLION % cycle_length
    dancers = init_dancers
    for i in range(rounds):
        dancers = dance_round(instructions, dancers)
    return ''.join(dancers)


with open("advent16_input.txt") as f:
    instr = process_instructions(f)
    print('         Part 1 (1 round): {}'.format(''.join(dance_round(instr))))
    print('Part 2 (1 billion rounds): {}'.format(dance(instr)))
    