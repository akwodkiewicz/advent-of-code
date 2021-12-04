def passphrase_checker(filename):
    valid = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            words = line.split()
            if len(words) == len(set(words)):
                valid += 1
        return valid

def strict_passphrase_checker(filename):
    valid = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            next_line = False
            words = line.split()
            word_dicts =[]
            for word in words:
                word_dict = {}
                word_dict = {char: word_dict.get(char,0)+1 for char in word}
                word_dicts.append(word_dict)
            for i, dict1 in enumerate(word_dicts):
                for j, dict2 in enumerate(word_dicts):
                    if i == j:
                        continue
                    if dict1 == dict2:
                        next_line=True
                        break
                if next_line:
                    break
            if not next_line:
                valid += 1
        return valid

print("Part 1 result: {}".format(passphrase_checker("advent4_input.txt")))
print("Part 2 result: {}".format(strict_passphrase_checker("advent4_input.txt")))
