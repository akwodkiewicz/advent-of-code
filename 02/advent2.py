def calculate_checksum(filename):
    with open(filename, "r") as f:
        import math
        result_sum = 0

        for line in f.readlines():
            min_val = math.
            max_val = -math.inf
            array = line.split()
            for value in array:
                number = int(value)
                min_val = min(min_val, number)
                max_val = max(max_val, number)
            result_sum += max_val - min_val
        return result_sum


def calculate_checksum2(filename):
    with open(filename, "r") as f:
        import math
        result_sum = 0

        for line in f.readlines():
            next_row = False
            smaller_val = 1
            bigger_val = 1           
            numbers = [int(x) for x in line.split()]
            for (i, bigger) in enumerate(numbers):
                if next_row:
                    break
                
                for (j, smaller) in enumerate(numbers):                    
                    if i == j:
                        continue         
                    whole, frac = divmod(bigger, smaller)
                    if frac == 0:
                        next_row = True
                        result_sum+=whole
                        break                  
        return result_sum


print("Example 1 result: {}  (should be 18)".format(calculate_checksum("advent2_example1.txt")))
print("Part 1 result:    {}".format(calculate_checksum("advent2_input.txt")))
print()
print("Example 2 result: {}  (should be 9)".format(calculate_checksum2("advent2_example2.txt")))
print("Part 2 result:    {}".format(calculate_checksum2("advent2_input.txt")))