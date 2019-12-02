
with open("02.txt", "r") as f:
    inp = f.read()

original = [int(x) for x in inp.split(',')]

def simulate(registers, noun, value):
    ops = { 1: lambda x, y: x+y, 2: lambda x, y: x*y}
    registers[1] = noun
    registers[2] = value
    curr = 0
    while registers[curr] != 99:
        opcode = registers[curr]
        val1 = registers[registers[curr+1]]
        val2 = registers[registers[curr+2]]
        store = registers[curr+3]
        if ops.get(opcode):
            registers[store] = ops[opcode](val1, val2)
        curr += 4
    return registers[0]

print(simulate(original[:], 12, 2))

expected = 19690720
noun = 0
delta = 10
quit = False
while True:
    for verb in range(delta):
        if simulate(original[:], noun, verb) == expected:
            quit = True
            break
    if quit:
        break
    noun += 1
    if noun % 10 == 0:
        delta += 10

print(noun*100 + verb)
