import re
from pprint import pprint
import math
from typing import List, Tuple


ITERATIONS = 5


def parse_input(filename):
    rules2x2 = []
    rules3x3 = []
    with open(filename) as file:
        for line in file:
            rules, result = [tuple(x.strip().split('/'))
                             for x in re.split(r'=>', line)]
            if len(rules) == 2:
                rules2x2.append((rules, result))
            else:
                rules3x3.append((rules, result))
    return rules2x2, rules3x3


def create_more_rules(rules):

    def transpose(pattern):
        return tuple(''.join(iterable) for iterable in zip(*pattern))

    def reverse_rows(pattern):
        return tuple(line[::-1] for line in pattern)

    set_of_patterns = set()
    new_rules = {}

    for pattern, result in rules:
        set_of_patterns.add(pattern)
        new_rules[pattern] = result
        new_patterns = []

        # Rotated right
        new_patterns.append(reverse_rows(transpose(pattern)))
        # Rotated left
        new_patterns.append(transpose(reverse_rows(pattern)))
        # Rotated 180
        new_patterns.append(reverse_rows(
            transpose(reverse_rows(transpose(pattern)))))

        # Flipped
        new_patterns.append(reverse_rows(pattern))
        # Flipped and rotated right
        new_patterns.append(reverse_rows(transpose(reverse_rows(pattern))))
        # Flipped and rotated left
        new_patterns.append(transpose(pattern))
        # Flipped and rotated 180
        new_patterns.append(transpose(reverse_rows(transpose(pattern))))

        for new_pattern in new_patterns:
            if new_pattern in set_of_patterns:
                continue
            set_of_patterns.add(new_pattern)
            new_rules[new_pattern] = result

    return new_rules


def divide(art):
    width = len(art[0])
    if width % 2 == 0:
        size = 2
    else:
        size = 3
    n = width // size
    divided_art = []
    for y in range(0, width, size):
        for x in range(n):
            small_art = []
            for i in range(size):
                small_art.append(art[y + i][x * size: x * size + size])
            divided_art.append(tuple(small_art))
    return divided_art


def merge(divided_art):
    m_in_row = int(math.sqrt(len(divided_art)))
    size = len(divided_art[0])
    art = []
    for height in range(m_in_row):
        big_row = divided_art[height * m_in_row: height * m_in_row + m_in_row]
        for y in range(size):
            art.append(''.join(m[y] for m in big_row))
    return art


def show_art(art):
    printable = ''.join(line + '\n' for line in art)
    print(printable)


def extend(
        divided,  # type: List[Tuple[str, ...]]
        rules2x2, # type: List[Tuple[Tuple[str, str], Tuple[str, str, str]]]
        rules3x3  # type: List[Tuple[Tuple[str, str, str], Tuple[str, str, str, str]]]
    ):
    # type: (...) -> List[Tuple[str, ...]]

    extended_art = []
    if len(divided[0]) % 2 == 0:
        rules = rules2x2
    else:
        rules = rules3x3
    
    for matrix in divided:
        extended_art.append(rules[matrix])
    return extended_art


def generate_some_art(rules2x2, rules3x3):
    art = ['.#.', '..#', '###']
    # art = ['##.##.', '#..#..', '......', '##.##.', '#..#..', '......']
    print('i = 0:')
    show_art(art)

    for i in range(ITERATIONS):
        divided = divide(art)
        extended = extend(divided, rules2x2, rules3x3)
        art = merge(extended)
        print('i = %d:' % (i+1))
        show_art(art)
    
    return art


def main():
    rules2x2, rules3x3 = parse_input('advent21_input.txt')
    rules2x2 = create_more_rules(rules2x2)
    rules3x3 = create_more_rules(rules3x3)
    art = generate_some_art(rules2x2, rules3x3)
    result = sum(row.count('#') for row in art)
    print('Number of active pixels [#] = %d' % result)


if __name__ == '__main__':
    main()
