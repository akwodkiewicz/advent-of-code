import re
from functools import reduce
from collections import Counter, defaultdict
from pprint import pprint
import itertools
import operator

INPUT_NAME = __file__.split('.')[0]+'-input.txt'


def read_input():
    rules = []
    tickets = []
    with open(INPUT_NAME) as file:
        for raw_line in file:
            line = raw_line.strip()
            if line.strip() == '':
                file.readline()
                break
            ranges = re.findall(r'(\d+-\d+)', line)
            num_ranges = [range(int(r.split('-')[0]), int(r.split('-')[1])+1) for r in ranges]
            rules.append([r for r in num_ranges])
        for raw_line in file:
            line = raw_line.strip()
            if line.strip() == '':
                file.readline()
                break
            tickets.append([int(x) for x in line.split(',')])
        for raw_line in file:
            line = raw_line.strip()
            tickets.append([int(x) for x in line.split(',')])

    return rules, tickets

def part_one(rules, tickets):
    error_rate = 0
    for ticket in tickets[1:]:
        for val in ticket:
            if not any(val in r for ruleset in rules for r in ruleset):
                error_rate += val
    return error_rate


def validate_tickets(rules, tickets):
    valid = []
    for ticket in tickets[1:]:
        for val in ticket:
            if not any(val in r for ruleset in rules for r in ruleset):
                break
        else:
            valid.append(ticket)
    return valid

def matches_rule(rule, value):
    return any(value in rng for rng in rule)

def part_two(rules, tickets):
    valid = validate_tickets(rules, tickets)
    
    candidate_rules = [set() for x in range(len(rules))]
    for idx in range(len(valid[0])):
        for rule_idx in range(len(rules)):
            if all(matches_rule(rules[rule_idx], ticket[idx]) for ticket in valid):
                candidate_rules[idx].add(rule_idx)

    used = set()

    while not all(len(s) == 1 for s in candidate_rules):
        current = None
        for candidate_set in candidate_rules:
            if len(candidate_set) == 1 and len(candidate_set.difference(used)) == 1:
                current = candidate_set.pop()
                candidate_set.add(current)
                used.add(current)
                break
        for candidate_set in candidate_rules:
            if len(candidate_set) != 1 and current in candidate_set:
                candidate_set.remove(current)
        
    solution = [s.pop() for s in candidate_rules]
    sorted_ticket = [v for k,v in sorted(zip(solution, tickets[0]))]
    return reduce(operator.mul, sorted_ticket[:6])

def main():
    rules, tickets = read_input()
    print(f"Part one: {part_one(rules, tickets)}")
    print(f"Part two: {part_two(rules, tickets)}")

if __name__ == "__main__":
    main()
