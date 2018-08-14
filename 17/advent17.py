STEPS = 370

def create_buffer():
    buffer = [0]
    position = 0
    for i in range(1, 2018):
        position = (STEPS + position) % len(buffer)
        buffer = buffer[:(position+1)] + [i] + buffer[(position+1):]
        position += 1
    return buffer


def find_value_after_2017(buffer):
    index = buffer.index(2017)
    return buffer[index+1]


def find_second_value():
    position = 0
    second_value = 0
    for i in range(1, 50_000_001):
        position = ((STEPS + position) % i)
        if position == 0:
            second_value = i
        position += 1
    return second_value


if __name__ == '__main__':

    print('Part 1: {}'.format(find_value_after_2017(create_buffer())))
    print('Part 2: {}'.format(find_second_value()))
