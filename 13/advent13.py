# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=W0611
from typing import Any, IO, List, Tuple


def process_layers(stream):
    # type: (IO[Any]) -> List[Tuple[int, int]]
    layers = []
    for line in stream:
        stuff = line.replace(':', '').split()
        tup = (int(stuff[0]), int(stuff[1]))
        layers.append(tup)
    return layers


def calculate_severity(layers):
    # type: (List[Tuple[int, int]]) -> int
    severity = 0

    for layer, range_val in layers:             # layer != 1
        if layer % ((range_val - 1) * 2) == 0:
            severity += layer * range_val

    return severity


def calculate_delay(layers):
    # type: (List[Tuple[int, int]]) -> int
    i = 0

    while True:
        caught = False
        for layer, range_val in layers:
            if (layer + i) % ((range_val - 1) * 2) == 0:
                caught = True
                break

        if not caught:
            break
        i += 1
    return i


with open("advent13_input.txt") as f:
    l = process_layers(f)
    s = calculate_severity(l)
    print('Part 1: severity = {}'.format(s))
    d = calculate_delay(l)
    print('Part 2: minimum_delay = {}'.format(d))
