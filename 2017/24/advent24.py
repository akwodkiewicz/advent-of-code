def parse_input(filename):
    with open(filename) as file:
        components = []
        for line in file:
            components.append(tuple(int(x) for x in line.split('/')))
        return components


def backtrack(port_in, left_components):
    left = left_components[:]
    strength = 0
    max_strength = 0

    for i, component in enumerate(left):
        try:
            idx = component.index(port_in)
            strength = sum(component)
            strength += backtrack(component[idx ^ 1], left[:i] + left[i + 1:])
        except ValueError:
            continue
        if strength > max_strength:
            max_strength = strength

    return max_strength


def backtrack2(port_in, left_components, length=0):
    left = left_components[:]
    max_len = length
    deep_len = length
    max_strength = 0
    for i, component in enumerate(left):
        try:
            idx = component.index(port_in)
            strength = sum(component)
            deep_strength, deep_len = backtrack2(
                component[idx ^ 1], left[:i] + left[i + 1:], length + 1)
            strength += deep_strength
        except ValueError:
            continue
        if deep_len > max_len:
            max_strength = strength
            max_len = deep_len
        elif deep_len == max_len and strength > max_strength:
            max_strength = strength

    return max_strength, max_len


def main():
    components = parse_input('advent24_input.txt')
    print(backtrack(0, components))
    print(backtrack2(0, components))


if __name__ == '__main__':
    main()
