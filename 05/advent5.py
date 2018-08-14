def trampolines(array):
    counter = 0
    dest = 0
    while dest < len(array) and dest >= 0:
        delta = array[dest]
        array[dest] += 1
        dest += delta
        counter += 1
    return counter


example_array = [0, 3, 0, 1, -3]
example_array2 = example_array.copy()
print("Example 1: {} (should be 5)".format(trampolines(example_array)))

input_array = []
with open("advent5_input.txt", 'r') as f:
    for line in f:
        input_array.append(int(line))
input_array2 = input_array.copy()

print("Result: {}".format(trampolines(input_array)))


def trampolines2(array):
    counter = 0
    dest = 0
    while dest < len(array) and dest >= 0:
        delta = array[dest]
        if delta >= 3:
            array[dest] -= 1
        else:
            array[dest] += 1
        dest += delta
        counter += 1
    return counter

print("Example 1: {} (should be 10)".format(trampolines2(example_array2)))
print("Result: {}".format(trampolines2(input_array2)))
