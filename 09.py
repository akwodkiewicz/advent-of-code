INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    numbers = []
    with open(INPUT_NAME) as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers

def part_one(data):
    buffer = data[:25]
    for i in range(25, len(data)):
        current = data[i]
        for p_i, potential in enumerate(buffer):
            if (current-potential) in buffer[:p_i]+buffer[p_i+1:]:
                break
            buffer[p_i] = potential
        else:
            return current
        buffer = buffer[1:] + [current]

def part_two(data, checksum):
    for start in range(len(data)):
        partial = data[start]
        for stop in range(start+1, len(data)):
            partial += data[stop]
            if partial == checksum:
                minimum, maximum = min(data[start:stop]), max(data[start:stop])
                return minimum + maximum
            elif partial < checksum:
                continue
            else:
                break

def main():
    data = read_input()
    part_one_result = part_one(data)
    print(f"Part one: {part_one_result}")
    print(f"Part two: {part_two(data, part_one_result)}")

if __name__ == "__main__":
    main()
    