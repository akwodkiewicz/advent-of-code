from functools import reduce
from collections import Counter,defaultdict, deque
from pprint import pprint
from itertools import product, starmap, chain
import string
import operator


def part_one(data):
    circle = deque(data)
    for step in range(100):
        picked_up = []
        current_cup = circle[0]

        circle.rotate(-1)
        for _ in range(3):
            picked_up.append(circle.popleft())
        circle.rotate(1)

        dest_cup = circle[0] - 1
        if dest_cup == 0:
            dest_cup = 9
        while dest_cup in picked_up:
            dest_cup -= 1
            if dest_cup == 0:
                dest_cup = 9
        
        dest_cup_idx = circle.index(dest_cup)
        circle.rotate(-(dest_cup_idx+1))

        while picked_up:
            circle.appendleft(picked_up.pop())
        circle.rotate(1)

        current_cup_idx = circle.index(current_cup)
        circle.rotate(-(current_cup_idx+1))

    cup_one_idx = circle.index(1)
    circle.rotate(-cup_one_idx)
    return circle
        
class Node:
    def __init__(self, v, prev_node):
        self.v = v
        self.prev_node = prev_node
        self.next_node = None

    def __repr__(self):
        return f"Node({self.v})"

def part_two(data):
    prev = None
    d = {}
    nodes = []
    for v in data + list(range(10, 1_000_001)):
        node = Node(v, prev)
        d[v] = node
        nodes.append(node)
        if prev is not None:
            prev.next_node = node
        prev = node
    nodes[0].prev_node = nodes[-1]
    nodes[-1].next_node = nodes[0]


    current_cup = nodes[0]
    for step in range(10_000_000):
        picked_up_start_ptr = current_cup.next_node
        picked_up_end_ptr = picked_up_start_ptr.next_node.next_node

        current_cup.next_node = picked_up_end_ptr.next_node
        picked_up_end_ptr.next_node.prev_node = current_cup

        picked_up_vals = set()
        tmp_ptr = picked_up_start_ptr
        for _ in range(3):
            picked_up_vals.add(tmp_ptr.v)
            tmp_ptr = tmp_ptr.next_node

        dest_cup_v = current_cup.v - 1
        if dest_cup_v == 0:
            dest_cup_v = 1_000_000
        while dest_cup_v in picked_up_vals:
            dest_cup_v -= 1
            if dest_cup_v == 0:
                dest_cup_v = 1_000_000
        
        dest_cup = d[dest_cup_v]

        picked_up_end_ptr.next_node = dest_cup.next_node
        dest_cup.next_node.prev_node = picked_up_end_ptr
        dest_cup.next_node = picked_up_start_ptr
        picked_up_start_ptr.prev_node = dest_cup

        current_cup = current_cup.next_node

    cup_one = d[1]
    return cup_one.next_node.v * cup_one.next_node.next_node.v

def main():
    data = [int(x) for x in "916438275"]
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
