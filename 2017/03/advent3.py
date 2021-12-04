def manhattan_spiral(index):
    import itertools, math 

    nearest_sqrt = int(math.floor(math.sqrt(index)))
    if nearest_sqrt % 2 == 0:
        nearest_sqrt -= 1
    x = int(nearest_sqrt/2)
    y = -x
    dx = 1
    dy = 0
    nearest_square = nearest_sqrt * nearest_sqrt

    for step in range(nearest_square, index):
        #print("[{}] --> ({},{})".format(step, x, y), flush=True)
        if step == nearest_square + 1:
            dx = 0
            dy = 1
        elif step == nearest_square +  nearest_sqrt + 1:
            dx = -1
            dy = 0
        elif step == nearest_square + 2 * nearest_sqrt + 2:
            dx = 0
            dy = -1
        elif step == nearest_square + 3 * nearest_sqrt + 3:
            dx = 1
            dy = 0
        x += dx
        y += dy
    return abs(x)+abs(y)
        

print("Example 1:    [1] -> {} (should be 0)".format(manhattan_spiral(1)))
print("Example 2:   [12] -> {} (should be 3)".format(manhattan_spiral(12)))
print("Example 3:   [23] -> {} (should be 2)".format(manhattan_spiral(23)))
print("Example 4: [1024] -> {} (should be 31)".format(manhattan_spiral(1024)))
print("Answer:  [265149] -> {}".format(manhattan_spiral(265149)))


def manhattan_spiral2(maximum):
   
    board = {}
    x = 0
    y = 0

    def get_adjacent_sum():
        sum = 0
        sum += board.get((x+1,y), 0)
        sum += board.get((x+1,y+1), 0)
        sum += board.get((x,y+1), 0)
        sum += board.get((x-1,y+1), 0)
        sum += board.get((x-1,y), 0)
        sum += board.get((x-1,y-1), 0)
        sum += board.get((x,y-1), 0)
        sum += board.get((x+1,y-1), 0)
        return sum

    dx = 1
    dy = 0
    delta = 1
    delta_decrem = 1
    state = 0
    board[(x,y)] = 1
    import itertools
    for i in itertools.count(1):
        if delta_decrem > 0:
            delta_decrem -= 1
            x += dx
            y += dy
            board[(x,y)] = get_adjacent_sum()
            print("({},{}) --> [{}]".format(x,y,board[(x,y)]))
            if board[(x,y)] > maximum:
                break
        else:
            state = (state + 1) % 4
            if state == 0:
                delta += 1
                dx = 1
                dy = 0
            elif state == 1:
                dx = 0
                dy = 1
            elif state == 2:
                delta += 1
                dx = -1
                dy = 0
            elif state == 3:
                dx = 0
                dy = -1
            delta_decrem = delta
    return board[(x,y)]
            

print("Answer 2:  [265149] -> {}".format(manhattan_spiral2(265149)))
