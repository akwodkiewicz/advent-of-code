def process_stream(stream, depth=0):
    value = depth
    garbage = False
    garbage_counter = 0
    char = stream.read(1)
    while char != "":
        if char == '!':
            stream.read(1)
            char = stream.read(1)
            continue
        if garbage:
            if char == '>':
                garbage = False
            else:
                garbage_counter += 1
        else:
            if char == '{':
                v, g = process_stream(stream, depth+1)
                value += v
                garbage_counter += g
            elif char == '}':
                return value, garbage_counter
            elif char == '<':
                garbage = True

        char = stream.read(1)
    return value, garbage_counter


import io
example = io.StringIO(r'{{<!>},{<!>},{<!>},{<a>}}')
example_result = process_stream(example)
print("Example: {} (should be (3, 13))".format(example_result))

with open("advent9_input.txt") as input_file:
    result = process_stream(input_file)
    print("Result: {}".format(result))
