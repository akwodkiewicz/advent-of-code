def parse_line(line):
    arr = line.split()
    reg = arr[0]
    op = arr[1]
    arg = int(arr[2])
    if_reg = arr[4]
    if_op = arr[5]
    if_arg = int(arr[6])
    return reg, op, arg, if_reg, if_op, if_arg


def parse_file(filename):
    arr = []
    with open(filename, 'r') as f:
        for line in f:
            result = parse_line(line)
            arr.append(result)
    return arr


OPERATIONS = {
    'inc': (lambda a, b: a+b),
    'dec': (lambda a, b: a-b),
    '<': (lambda a, b: a < b),
    '<=': (lambda a, b: a <= b),
    '>': (lambda a, b: a > b),
    '>=': (lambda a, b: a >= b),
    '!=': (lambda a, b: a != b),
    '==': (lambda a, b: a == b)
    }


def process_instructions(array):
    registers = {}
    highest_value = 0
    for reg, op_code, arg, if_reg, if_op_code, if_arg in array:
        if reg not in registers:
            registers[reg] = 0
        if if_reg not in registers:
            registers[if_reg] = 0

        if_op = OPERATIONS[if_op_code]
        if not if_op(registers[if_reg], if_arg):
            continue

        op = OPERATIONS[op_code]
        registers[reg] = op(registers[reg], arg)
        if highest_value < registers[reg]:
            highest_value = registers[reg]

    values = [x for x in registers.values()]
    return max(values), highest_value



example_array = parse_file("advent8_example.txt")
print("Example: {} (should be (1, 10))".format(process_instructions(example_array)))
input_array = parse_file("advent8_input.txt")
print("Result: {}".format(process_instructions(input_array)))
