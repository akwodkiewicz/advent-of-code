from functools import reduce
from collections import Counter,defaultdict
from pprint import pprint
from itertools import product, starmap, chain
import string
import operator
INPUT_NAME = __file__.split('.')[0]+'-input.txt'


def read_input():
    decks = []
    with open(INPUT_NAME) as file:
        deck = []
        for line in file:
            if "Player" in line:
                continue
            if line.strip() == '':
                decks.append(deck)
                deck = []
                continue
            deck.append(int(line.strip()))
        decks.append(deck)
    return decks


def combat(data):
    player_one, player_two = data
    while len(player_one) > 0 and len(player_two) > 0:
        one, two = player_one.pop(0), player_two.pop(0)
        if one > two:
            player_one.append(one)
            player_one.append(two)
        else:
            player_two.append(two)
            player_two.append(one)
    winner = 0 if len(player_two) == 0 else 1
    return winner

def part_one(data):
    winner = combat(data)
    result = 0
    for idx, card in enumerate(reversed(data[winner])):
        result += (idx+1) * card
    return result


def recursive_combat(decks, game):
    # print(f"Game {game}")
    used = [set(), set()]
    player_one, player_two = decks
    # round_num, fixed_game = 1, game
    while len(player_one) > 0 and len(player_two) > 0:
        # print(f"- Round {round_num} (Game {fixed_game})")
        # print(f"\tP1: {player_one}")
        # print(f"\tP2: {player_two}")

        hashes = list(map(hash, map(tuple, decks)))
        if hashes[0] in used[0] or hashes[1] in used[1]:
            # print("Infinite recursion detected")
            # print("Winner of game {fixed_game}: player 1")
            return 0, player_one, game
        else:
            used[0].add(hashes[0])
            used[1].add(hashes[1])

        one, two = player_one.pop(0), player_two.pop(0)
        if len(player_one) >= one and len(player_two) >= two:
            round_winner, winning_deck, game = recursive_combat(
                [player_one[0:one], player_two[0:two]], game+1
            )
            # print(f"...back to game {fixed_game}...")
        else:
            round_winner = 0 if one > two else 1
        
        if round_winner == 0:
            player_one.append(one)
            player_one.append(two)
        else:
            player_two.append(two)
            player_two.append(one)
        # round_num += 1
    
    game_winner = 0 if len(player_two) == 0 else 1
    # print(f"Winner of game {fixed_game}: player {game_winner+1}")
    return game_winner, decks[game_winner], game

def part_two(decks):
    _, winning_deck, _ = recursive_combat(decks, 1)
    result = 0
    for idx, card in enumerate(reversed(winning_deck)):
        result += (idx+1) * card
    return result


def main():
    data = read_input()
    print(f"Part one: {part_one(data)}")
    data = read_input()
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
