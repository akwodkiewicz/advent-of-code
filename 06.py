from collections import Counter

INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    groups = []
    with open(INPUT_NAME) as file:
        group = []
        for line in file:
            if line.strip() == '':
                groups.append(group)
                group = []
                continue
            group.append(line.strip())
        groups.append(group)
    return groups

def part_one(data):
    """Collecting answers using a set"""
    yes_num = 0
    for group in data:
        answers = set(''.join(group))
        yes_num += len(answers)
    return yes_num

def part_two(data):
    """Collecting answers using a multiset"""
    yes_num = 0
    for group in data:
        answers = Counter(''.join(group))
        yes_num += len([c for c in answers if answers[c] == len(group)])
    return yes_num


def main():
    data = read_input()
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
    