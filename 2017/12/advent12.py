def process_connections(stream):
    connections = {}
    for line in stream:
        line = line.replace(',', '')
        stuff = line.split()
        pipe = int(stuff[0])
        connected = [int(x) for x in stuff[2:]]
        connections[pipe] = connected
    return connections   

def group_connections(connections, start_number=0):
    visited = set()
    visited.add(start_number)
    stack = [start_number]

    while len(stack) > 0:
        current = stack[-1]
        stack.remove(current)
        for pipe in connections[current]:
            if pipe not in visited:
                visited.add(pipe)
                stack.append(pipe)
    return visited

def group_all_connections(connections):
    groups = {}
    visited = set()
    for i in range(len(connections)):
        if i in visited:
            continue
        group = group_connections(connections, start_number=i)
        visited = visited.union(group)
        groups[i] = len(group)
    return groups



from pprint import pprint 
with open("advent12_input.txt") as f:
    connections = process_connections(f)
    group_lengths = group_all_connections(connections)
    print('Part 1: size_of_zero_group = {}'.format(group_lengths[0]))
    print('Part 2: num_of_groups = {}'.format(len(group_lengths)))
