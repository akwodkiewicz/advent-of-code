from functools import reduce
from pprint import pprint 
INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def read_input():
    seat_codes = []
    with open(INPUT_NAME) as file:
        for line in file:
            seat_codes.append(line.strip())
    return seat_codes


def find_row(seat_code):
    a = 0
    b = 127
    m = -1
    for char in seat_code:
        if a+1 == b:
            if char =='F':
                return a
            if char =='B':
                return b
        m = (a + b) // 2
        if char == 'F':
            b = m
        elif char == 'B':
            a = m +1

def find_column(seat_code):
    a = 0
    b = 7
    m = -1
    for char in seat_code:
        if a+1 == b:
            if char =='L':
                return a
            if char =='R':
                return b
        m = (a + b) // 2
        if char == 'L':
            b = m
        elif char == 'R':
            a = m + 1
    return m

def calculate_id(row, column):
    return row * 8 + column

def part_one(data):
    max_seat_id = -1
    max_seat = None
    for entry in data:
        row = find_row(entry)
        column = find_column(entry)
        seat_id = calculate_id(row, column)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
            max_seat = (row, column)
    return max_seat_id

def part_two(data):
    seats = []
    seats_num = 0
    for y in range(128):
        seats.append([])
        for x in range(8):
            seats[y].append(' ')
    for entry in data:
        row = find_row(entry)
        column = find_column(entry)
        if seats[row][column] == 'X':
            raise AssertionError('wat', row, column, entry)
        seats[row][column] = 'X'
    
    prev_x = False
    candidate = None
    for row, seats_row in enumerate(seats):
        for column, seat in enumerate(seats_row):
            if seat == 'X':
                prev_x = True
                if candidate:
                    return candidate
            if seat == ' ':
                if prev_x:
                    candidate = calculate_id(row, column)
                else:
                    prev_x = False                



def main():
    data = read_input()
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
    