def move(maze):
    dx = 0
    dy = 1
    letters = []

    def find_start():
        for i in range(len(maze[0])):
            if maze[0][i] == '|':
                return i

    def find_turn(center_x, center_y, dx, dy):
        for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if -dx == x and -dy == y:
                continue
            if (maze[center_y + y][center_x + x] == '|' and x == 0) \
            or (maze[center_y + y][center_x + x] == '-' and y == 0):
                return x, y


    x = find_start()
    y = 0
    counter = 0
    while True:
        char = maze[y][x]
        counter += 1
        if char == '+':
            dx, dy = find_turn(x, y, dx, dy)

        elif char == ' ':
            return ''.join(letters), counter - 1

        elif char not in ('|', '-'):
            letters.append(char)

        x += dx
        y += dy


def prepare_maze():
    maze = []
    with open('advent19_input.txt', 'r') as file:
        for line in file:
            maze.append(line[:-1])
        return maze


print(move(prepare_maze()))
