
STEPS = 12_919_244

def solve():
    q = 'A'
    delta = {
        ('A', 0): ('B', 1, 'R'),
        ('A', 1): ('C', 0, 'L'),
        ('B', 0): ('A', 1, 'L'),
        ('B', 1): ('D', 1, 'R'),
        ('C', 0): ('A', 1, 'R'),
        ('C', 1): ('E', 0, 'L'),
        ('D', 0): ('A', 1, 'R'),
        ('D', 1): ('B', 0, 'R'),        
        ('E', 0): ('F', 1, 'L'),
        ('E', 1): ('C', 1, 'L'),
        ('F', 0): ('D', 1, 'R'),
        ('F', 1): ('A', 1, 'R'),        
    }
    head = 0
    tape = {0: 0}
    for i in range(STEPS):
        symbol = tape.get(head)
        if symbol is None:
            symbol = 0
            tape[head] = 0
        q, tape[head], move = delta[(q, symbol)]
        if move == 'R':
            head += 1
        else:
            head -= 1
    checksum = len([v for v in tape.values() if v == 1])
    return checksum


def main():
    from pprint import pprint
    pprint(solve())


if __name__ == '__main__':
    main()
