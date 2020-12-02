SUM = 2020

def read_input():
    numbers = []
    with open("01-input.txt") as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers

def part_one(numbers):
    """
        Time: O(n)
        Space: O(2021)
    """
    exists = [False for _ in range(SUM+1)]
    for number in numbers:
        if exists[SUM-number]:
            return number * (SUM-number)
        exists[number] = True
    return None

def part_two(numbers):
    """
        Time: O(n^3)
        Space: O(1)
    """
    for first in numbers:
        for second in numbers:
            for third in numbers:
                if first + second + third == SUM:
                    return first * second * third
    return None


if __name__ == "__main__":
    numbers = read_input()
    print(f"Part one: {part_one(numbers)}")
    print(f"Part two: {part_two(numbers)}")
