from functools import reduce
import re

INPUT_NAME = __file__.split('.')[0]+'-input.txt'
VALID_TYPES = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])

def hgt_validator(x):
    if 'cm' not in x and 'in' not in x:
        return False
    if x[-2:] == 'cm':
        return int(x[:-2]) >= 150 and int(x[:-2]) <= 193
    if x[-2:] == 'in':
        return int(x[:-2]) >= 59 and int(x[:-2]) <= 76
    return None

TYPE_VALIDATOR = {
    'byr': (lambda x: len(x) == 4 and int(x) >= 1920 and int(x) <= 2002),
    'iyr': (lambda x: len(x) == 4 and int(x) >= 2010 and int(x) <= 2020),
    'eyr': (lambda x:  len(x) == 4 and int(x) >= 2020 and int(x) <= 2030),
    'hgt': hgt_validator,
    'hcl': (lambda x: x[0] == '#' and True if re.match('[0-9a-f]{6}', x[1:]) else False),
    'ecl': (lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
    'pid': (lambda x: len(x) == 9),
    'cid': (lambda x: True)
}

def read_input():
    entries = []
    with open(INPUT_NAME) as file:
        entry = []
        for line in file:
            if line.strip() == '':
                entries.append(entry)
                entry = []
                continue
            for x in line.split():
                entry.append(x)
    return entries


def part_one(data):
    valid_passports = 0
    for entry in data:
        valid_fields = set()
        for field in entry:
            field_type = field[:3]
            if field_type in VALID_TYPES:
                valid_fields.add(field_type)
        if len(valid_fields) == 8 or ('cid' not in valid_fields and len(valid_fields) == 7):
            valid_passports += 1
    return valid_passports


def part_two(data):
    valid_passports = 0
    for entry in data:
        valid_fields = set()
        for field in entry:
            field_type, field_value = field.split(':')
            if TYPE_VALIDATOR[field_type](field_value):
                valid_fields.add(field_type)
            print(valid_fields)
        if len(valid_fields) == 8 or ('cid' not in valid_fields and len(valid_fields) == 7):
            valid_passports += 1
    return valid_passports


def main():
    data = read_input()
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
    