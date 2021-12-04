# pylint: disable = C0111
# pylint: disable = C0103
INPUT_LENGTHS = [227, 169, 3, 166, 246, 201, 0, 47, 1, 255, 2, 254, 96, 3, 97, 144]
INPUT_LENGTHS_ASCII = '227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144'
EXAMPLE_LENGTHS = [3, 4, 1, 5]


def reverse_circular(array, start, end):
    temp = []
    size = len(array)
    index = start
    while index != end:
        temp.append(array[index])
        index = (index + 1) % size
    temp.append(array[index])
    index = start
    temp = temp[::-1]
    i = 0
    while i != len(temp):
        array[index] = temp[i]
        index = (index + 1) % size
        i += 1


def knot_hash_function_round(data, len_array, hash_size=256, skip=0, index=0):
    for length in len_array:
        end = (index + length - 1) % hash_size
        if length > 0 and length <= hash_size:
            reverse_circular(data, index, end)
        index = (index + length + skip) % hash_size
        skip += 1
    result = data[0] * data[1]
    return data, result, skip, index


def knot_hash_function(string):
    # type: (str) -> str
    skip = 0
    index = 0
    data = [i for i in range(256)]
    len_array = [ord(c) for c in string]
    len_array.extend([17, 31, 73, 47, 23])
    for i in range(64):
        data, _, skip, index = knot_hash_function_round(data, len_array, 256, skip, index)
    xored = []
    for i in range(16):
        val = 0
        for j in range(16):
            val ^= data[16*i + j]
        xored.append(val)
    xored_hex = ['{0:02x}'.format(n) for n in xored]
    knot_hash = ''.join(xored_hex)
    return knot_hash

if __name__ == 'main':
    data_array = [i for i in range(256)]
    _, res, _, _ = knot_hash_function_round(data_array, INPUT_LENGTHS)
    print("Part 1: {}".format(res))
    print("Part 2: {}".format(knot_hash_function(INPUT_LENGTHS_ASCII)))
