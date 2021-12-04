def part_one(data, stop=2020):
    round = 1
    value = None
    used = {}
    before_used = {}
    first_time = False
    while round <= stop:
        if round-1 < len(data):
            value = data[round-1]
        elif first_time:
            value = 0
        else:
            value = used[value] - before_used[value]
        
        if used.get(value) is None:
            first_time = True
        else:
            first_time = False
            before_used[value] = used[value]
        used[value] = round
        round += 1

    return value

def part_two(data):
    return part_one(data, 30000000)
   

def main():
    INPUT = '0,13,1,16,6,17'
    data = list(map(int, INPUT.split(',')))
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
