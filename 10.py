from functools import reduce
from collections import Counter
from pprint import pprint

INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    numbers = []
    with open(INPUT_NAME) as file:
        for line in file:
            numbers.append(int(line.strip()))
    numbers.append(0)
    numbers.append(max(numbers) + 3)
    return numbers

def part_one(data):
    sorted_data = sorted(data)
    print(sorted_data)
    diffs = [b-a for a,b in zip(sorted_data, sorted_data[1:])]
    print(diffs)
    return diffs.count(1) * diffs.count(3) 

def part_two(data):
    """
    Pen & paper solution.

    Feels like cheating, but hey, it works.

    It wouldn't, however, if data contained "non-locked" subseries of length > 3.
    """
    sorted_data = sorted(data)
    diffs = [b-a for a,b in zip(sorted_data, sorted_data[1:])]
    locked = [True] + [True if d == 3 else False for d in diffs]
    locked[-1] = True
    for i in range(len(locked)-1):
        if locked[i+1]:
            locked[i] = True

    subseries = Counter()
    is_false_subseries = False
    counter = 0
    for a in locked:
        if not a:
            is_false_subseries = True
            counter += 1
        elif is_false_subseries:
            subseries[counter] += 1
            counter = 0
            is_false_subseries = False

    return  (7 ** subseries[3]) * (4 ** subseries[2])  * (2 ** subseries[1])
   

def main():
    data = read_input()
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
    

# num_of_arrangements = 0
# def part_two_bad(data):
#     """
#     This takes too long
#     """
#     sorted_data = sorted(data)
#     print(sorted_data)
#     diffs = [b-a for a,b in zip(sorted_data, sorted_data[1:])]
#     print(diffs)
#     partial = []
#     def check(sorted_adapters, idx, partial_result):
#         global num_of_arrangements
#
#         if partial_result[-1] == sorted_adapters[-1]:
#             num_of_arrangements += 1
#             return
#         if idx >= len(sorted_adapters):
#             return
#         current_adapter = sorted_adapters[idx]
#         if current_adapter - partial_result[-1] > 3:
#             return
#         check(sorted_adapters, idx+1, partial_result+[current_adapter])
#         check(sorted_adapters, idx+1, partial_result)
#
#     check(sorted_data, 1, [0])
#     return num_of_arrangements
    