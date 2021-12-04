INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    lines = []
    with open(INPUT_NAME) as file:
        for line in file:
            line = line.replace(':', '')
            line = line.replace('-', ' ')
            lines.append(line.split())
    return lines


def part_one(data):
    """
        Time: O(n)
    """
    valid = 0
    for line in data:
        [min_occ, max_occ, letter, passwd] = line
        occ = passwd.count(letter)
        if occ >= int(min_occ) and occ <= int(max_occ):
            valid += 1
    return valid


def part_two(numbers):
    """
        Time: O(n)
    """
    valid = 0
    for line in data:
        [pos_1, pos_2, letter, passwd] = line
        if (passwd[int(pos_1)-1] == letter and passwd[int(pos_2)-1] != letter) or (passwd[int(pos_1)-1] != letter and passwd[int(pos_2)-1] == letter):
            valid += 1
    return valid


if __name__ == "__main__":
    data = read_input()
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")
