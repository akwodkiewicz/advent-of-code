from functools import reduce
from collections import Counter,defaultdict
from pprint import pprint
from itertools import product, starmap, chain
import string
import operator
INPUT_NAME = __file__.split('.')[0]+'-input.txt'


def read_input():
    foods = []
    with open(INPUT_NAME) as file:
        for line in file:
            ingredients = line.split(' (')[0].split(' ')
            allergens = line.strip().split('contains ')[1][:-1].split(', ')
            foods.append((ingredients, allergens))
    return foods
  

def part_one(data):
    flat_ingredients = list(chain.from_iterable(tup[0] for tup in data))
    unique_ingredients = set(flat_ingredients)
    unique_allergens = set(chain.from_iterable(tup[1] for tup in data))
    allergenic_ingredients = {allergen: [] for allergen in unique_allergens}

    for allergen in unique_allergens:
        candidates = []
        for food_ingredients, food_allergens in data:
            if allergen not in food_allergens:
                continue
            candidates.append(set(food_ingredients))
        allergenic_ingredients[allergen] = reduce(set.intersection, candidates)
    
    suspicious_ingredients = set(chain.from_iterable(v for v in allergenic_ingredients.values()))
    safe_ingredients = unique_ingredients.difference(suspicious_ingredients)
    return sum([1 for i in flat_ingredients if i in safe_ingredients]), allergenic_ingredients
                

def part_two(potential_allergens):
    ingredients = [k for k in sorted(potential_allergens.keys())]
    allergens = [potential_allergens[k] for k in ingredients]

    solution = None
    def process(ingreds, allergs, partial, used):
        nonlocal solution

        if len(partial) == len(ingreds):
            solution = partial[:]
            return

        current_idx = len(partial)
        for ingredient in allergens[current_idx]:
            if ingredient not in used:
                partial.append(ingredient)
                used.add(ingredient)
                process(ingreds, allergs, partial, used)
                partial.pop()
                used.remove(ingredient)
        return solution

    process(ingredients, allergens, [], set())
    print(ingredients)
    print(solution)
    return ','.join(solution)


def main():
    data = read_input()
    result_one, allergenic_ingredients = part_one(data)
    print(f"Part one: {result_one}")
    print(f"Part two: {part_two(allergenic_ingredients)}")

if __name__ == "__main__":
    main()
