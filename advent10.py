INPUT_LENGTHS = [227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144]
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


def knot_hash_function(data_array, len_array, hash_size=256, skip=0, index=0):
    from pprint import pprint
    for length in len_array:
        end = (index + length - 1) % hash_size
        if length > 0 and length <= hash_size:
            reverse_circular(data_array, index, end)
        index = (index + length + skip) % hash_size
        skip += 1
    result = data_array[0]*data_array[1]
    return data_array, result, skip, index


def run_full_64_rounds(len_array):
    skip = 0
    index = 0
    data = [i for i in range(256)]
    len_array = [ord(c) for c in len_array]
    len_array.extend([17, 31, 73, 47, 23])
    for i in range(64):
        data, _, skip, index = knot_hash_function(data, len_array, 256, skip, index)
    xored = []
    for i in range(16):
        val = 0
        for j in range(16):
            val ^= data[16*i + j]
        xored.append(val)
    xored_hex = ['{0:02x}'.format(n) for n in xored]
    knot_hash = ''.join(xored_hex)
    return knot_hash


#example_data_array = [i for i in range(5)]
#print(knot_hash_function(example_data_array, EXAMPLE_LENGTHS, 5))

data_array = [i for i in range(256)]
array, result, _, _ = knot_hash_function(data_array, INPUT_LENGTHS)
print("Part 1: {}".format(result))

print("Part 2: {}".format(run_full_64_rounds(INPUT_LENGTHS_ASCII)))
