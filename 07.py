from pprint import pprint

INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    rules = defaultdict(list)
    inverse_rules = defaultdict(list)
    with open(INPUT_NAME) as file:
        for line in file:
            line = line.strip()
            tokens = line.split(' ')
            main_bag = line.split(' bags')[0]
            inside_bags = [inside_bag.replace(' bags', '').replace(' bag', '') for inside_bag in line.split('contain ')[1].replace('.', '').split(', ')]
            if inside_bags[0] == 'no other':
                details = None
            else:
                details = [(int(bag[0]), bag[2:]) for bag in inside_bags]
                for _, bag in details:
                    inverse_rules[bag].append(main_bag)
            rules[main_bag] = details
    return rules, inverse_rules


def part_one(inverse_rules):
    visited = set()
    stack = ['shiny gold']
    while len(stack) > 0:
        current = stack.pop()
        containing = inverse_rules[current]
        for bag in containing:
            if bag in visited:
                continue
            visited.add(bag)
            stack.append(bag)
    return len(visited)


def part_two(rules):
    num_of_bags = 0
    stack = [x for x in rules['shiny gold']]
    while len(stack) > 0:
        num, type = stack.pop()
        num_of_bags += num
        if rules[type] is None:
            continue
        for rule in rules[type]:
            nested_num, nested_type = rule
            stack.append((nested_num * num, nested_type))
    return num_of_bags


def main():
    rules, inverse_rules = read_input()
    print(f"Part one: {part_one(inverse_rules)}")
    print(f"Part two: {part_two(rules)}")


if __name__ == "__main__":
    main()
    