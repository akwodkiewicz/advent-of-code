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
    answers_num = 0
    for group in data:
        chars = set()
        for person in group:
            for char in person:
                chars.add(char)
        answers_num += len(chars)
    return answers_num

def part_two(data):
    """Collecting answers using a multiset"""
    answers_num = 0
    for group in data:
        chars = Counter()
        for person in group:
            for char in person:
                chars[char] += 1
        for char in chars:
            if chars[char] == len(group):
                answers_num += 1
    return answers_num


def main():
    data = read_input()
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
    