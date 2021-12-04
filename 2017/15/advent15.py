# pylint: disable=C0103
# pylint: disable=C0111
A_FACTOR = 16807
B_FACTOR = 48271
MODULO = 2147483647
PAIRS = 40000000
PAIRS_2 = 5000000

A_INPUT = 873
B_INPUT = 583

def count_pairs():
    counter = 0
    a_state = A_INPUT
    b_state = B_INPUT
    for _ in range(PAIRS):
        if a_state & 0xFFFF == b_state & 0xFFFF:
            counter += 1

        a_state = (a_state * A_FACTOR) % MODULO
        b_state = (b_state * B_FACTOR) % MODULO
    return counter



def count_pairs_2():
    counter = 0

    def a_generator():
        a_state = A_INPUT
        while True:
            a_state = (a_state * A_FACTOR) % MODULO
            if a_state & 0x3 == 0:
                yield a_state

    def b_generator():
        b_state = B_INPUT
        while True:
            b_state = (b_state * B_FACTOR) % MODULO
            if b_state & 0x7 == 0:
                yield b_state

    a = a_generator()
    b = b_generator()

    for _ in range(PAIRS_2):
        if next(a) & 0xFFFF == next(b) & 0xFFFF:
            counter += 1
    return counter

print('Part 1: {}'.format(count_pairs()))
print('Part 2: {}'.format(count_pairs_2()))
