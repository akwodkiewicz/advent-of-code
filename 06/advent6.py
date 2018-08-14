def mem_realloc(input_array):
    array = input_array.copy()
    counter = 0
    permutation_set = set()
    permutation = tuple(array)
    while permutation not in permutation_set:
        permutation_set.add(permutation)
        blocks = max(array)
        index = array.index(blocks)
        array[index] = 0
        while blocks > 0:
            index = (index + 1) % len(array)
            array[index] += 1
            blocks -= 1
        permutation = tuple(array)
        counter += 1
    return counter




example_array = [0, 2, 7, 0]
print("Example 1: {} (should be 5)".format(mem_realloc(example_array)))

with open("advent6_input.txt", 'r') as f:
    line = f.readline()
    input_array = [int(x) for x in line.split()]
print("Result: {}".format(mem_realloc(input_array)))


def mem_realloc2(input_array):
    array = input_array.copy()
    counter = 0
    permutation_set = set()
    permutation = tuple(array)
    count_loop = False
    while True:
        if count_loop:
            counter += 1 
            if permutation == repeated_permutation:
                break
        if not count_loop and permutation in permutation_set:
            count_loop = True
            repeated_permutation = permutation

        permutation_set.add(permutation)
        blocks = max(array)
        index = array.index(blocks)
        array[index] = 0
        while blocks > 0:
            index = (index + 1) % len(array)
            array[index] += 1
            blocks -= 1
        permutation = tuple(array)
    return counter

print("Example 1: {} (should be 4)".format(mem_realloc2(example_array)))
print("Result: {}".format(mem_realloc2(input_array)))
