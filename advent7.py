def parse_line(line):
    arr = line.replace(',', '').split()
    base = arr[0]
    weight = int(arr[1][1:-1])
    upper_list = arr[3:]
    return base, weight, upper_list


def parse_file(filename):
    arr = []
    with open(filename, 'r') as f:
        for line in f:
            result = parse_line(line)
            arr.append(result)
    return arr


def find_base_program(array):
    potential_bases = set([base for (base, _, _) in array])
    for _, _, upper_list in array:
        for program in upper_list:
            if program in potential_bases:
                potential_bases.remove(program)
    return potential_bases.pop()


class Node:
    def __init__(self, name, weight, children=None):
        self.name = name
        self.weight = weight
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)


    def __repr__(self):
        return '{} ({})'.format(self.name, self.weight)


    def add_child(self, node):
        assert isinstance(node, Node)
        self.children.append(node)


    def print(self, depth=0, last=False):
        if depth == 0:
            line = self
        else:
            if last:
                line = "{}└{} {}".format(4*(depth-1)*' ', 2*'─', self)
            else:
                line = "{}├{} {}".format(4*(depth-1)*' ', 2*'─', self)
        print(line)
        for i, child in enumerate(self.children):
            if i == len(self.children) - 1:
                child.print(depth+1, True)
            else:
                child.print(depth+1)


    def find_imbalance(self):
        if len(self.children) == 0:
            return False, self.weight, self.name

        branches_weights = []
        branches = {}
        for child in self.children:
            imbalanced, branch_weight, branch_name = child.find_imbalance()
            if imbalanced:
                return True, branch_weight, branch_name
            else:
                branches_weights.append(branch_weight)
                branches[branch_weight] = branch_name

        weights_dict = {weight: branches_weights.count(weight) for weight in branches_weights}
        if len(weights_dict) != 1:
            for key, value in weights_dict.items():
                if value == 1:
                    wrong_weight = key
                else:
                    good_weight = key
            wrong_name = branches[wrong_weight]
            wrong_child = next(child for child in self.children if child.name == wrong_name)
            return True, (wrong_child.weight - (wrong_weight-good_weight)), wrong_name
        return False, self.weight + sum(branches_weights), self.name  


def prepare_nodes(array):
    nodes = {}
    for tup in array:
        name, weight, _ = tup
        nodes[name] = Node(name, weight)
    for tup in array:
        name, _, children_names = tup
        parent = nodes[name]
        for child_name in children_names:
            child = nodes[child_name]
            parent.add_child(child)
    return nodes


example_array = parse_file("advent7_example.txt")
input_array = parse_file("advent7_input.txt")


print('Part 1:')

example_result = find_base_program(example_array)
print("Example: {} (should return 'tknk')".format(example_result))

input_result = find_base_program(input_array)
print("Result: {} ".format(input_result)) # vtzay

print()
print('Part 2:')

example_nodes = prepare_nodes(example_array)
example_nodes[example_result].print()

_, example_result2, _ = example_nodes[example_result].find_imbalance()
print("Example: {} (should return 60)".format(example_result2))

input_nodes = prepare_nodes(input_array)
_, input_result2, _ = input_nodes[input_result].find_imbalance()
print("Result: {} ".format(input_result2)) # 910
