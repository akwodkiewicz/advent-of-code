from functools import reduce
from collections import Counter,defaultdict
from pprint import pprint
from itertools import product, starmap, chain
import string
import operator
import re
INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    rules = {}
    inputs = []
    with open(INPUT_NAME) as file:
        for line in file:
            if line.strip() == '':
                break
            rule_num, rule = line.strip().split(": ")
            rules[int(rule_num)] = rule
        for line in file:
            inputs.append(line.strip())
    return rules, inputs
  
def part_one(rules, inputs):
    master_rule = rules[0]

    used_rules = set()
    rules_with_numbers = [(n, r) for n, r in rules.items() if re.search(r'\d+', r)]
    rules_without_numbers_stack = [(n, r) for n, r in rules.items() if not re.search(r'\d+', r)]
    while len(rules_without_numbers_stack) > 0:
        current_num, current_rule = rules_without_numbers_stack.pop()
        rules[current_num] = current_rule
        for i in range(len(rules_with_numbers)):
            rule_num, rule = rules_with_numbers[i]
            if not re.search(f'\\b{str(current_num)}\\b', rule):
                continue
            new_rule = re.sub(f"\\b{str(current_num)}\\b", f"({current_rule})", rule)
            if not re.search(r'\d+', new_rule):
                rules_without_numbers_stack.append((rule_num, new_rule))
            else:
                rules_with_numbers[i] = (rule_num, new_rule)

    master_rule = "^" + rules[0].replace('"', '').replace(' ', '') + "$"
    regex = re.compile(master_rule)
    matches = 0
    return sum([1 for inpt in inputs if re.match(regex, inpt)])


def part_two(_rules, inputs):
    """Observe logs to catch the answer early"""

    max_input_len = max(len(x) for x in inputs)
    pumping_factor = 1
    matches = set()
    while pumping_factor < max_input_len / 2:
        print(f"pumping factor: {pumping_factor}")
        rules = _rules.copy()
        rules[8] = "(42)+"
        rules[11] = f"{pumping_factor*'(42)'} {pumping_factor*'(31)'}"

        used_rules = set()
        rules_with_numbers = [(n, r) for n, r in rules.items() if re.search(r'\d+', r)]
        rules_without_numbers_stack = [(n, r) for n, r in rules.items() if not re.search(r'\d+', r)]
        while len(rules_without_numbers_stack) > 0:
            current_num, current_rule = rules_without_numbers_stack.pop()
            rules[current_num] = current_rule
            for i in range(len(rules_with_numbers)):
                rule_num, rule = rules_with_numbers[i]
                if not re.search(f'\\b{str(current_num)}\\b', rule):
                    continue
                new_rule = re.sub(f"\\b{str(current_num)}\\b", f"({current_rule})", rule)
                if not re.search(r'\d+', new_rule):
                    rules_without_numbers_stack.append((rule_num, new_rule))
                else:
                    rules_with_numbers[i] = (rule_num, new_rule)

        master_rule = "^" + rules[0].replace('"', '').replace(' ', '') + "$"
        regex = re.compile(master_rule)
        for inpt in inputs:
            if re.match(regex, inpt):
                matches.add(inpt)
        print(f"matching: {len(matches)}")
        pumping_factor += 1
    
    return len(matches)


def main():
    rules, inputs = read_input()
    print(f"Part one: {part_one(rules, inputs)}")
    rules, inputs = read_input()
    print(f"Part two: {part_two(rules, inputs)}")

if __name__ == "__main__":
    main()
