from functools import reduce
from collections import Counter,defaultdict
from pprint import pprint
from itertools import product, starmap, chain
import string
import ast
INPUT_NAME = __file__.split('.')[0]+'-input.txt'

def tokenize():
    equations = []
    with open(INPUT_NAME, 'r') as file:
        for line in file:
            tokens = []
            number_buffer = []
            for c in line.strip():
                if c in string.digits:
                    number_buffer.append(c)
                    continue
                if number_buffer:
                    tokens.append(''.join(number_buffer))
                    number_buffer = []
                if c in '()+*':
                    tokens.append(c)
            if number_buffer:
                tokens.append(''.join(number_buffer))
            equations.append(tokens)
    return equations

class Expression_One:
    def __init__(self, tokens, left_term=None):
        if left_term:
            self.left_term = left_term
        else:
            self.left_term = Term_One(tokens)
        operator_token = tokens.pop(0)
        if operator_token not in '+*':
            raise Exception('SANITY CHECK 3 FAILED')
        self.operator = operator_token
        self.right_term = Term_One(tokens)

    def __repr__(self):
        return f"({self.left_term} {self.operator} {self.right_term})"

    def calculate(self):
        left_val = self.left_term.calculate()
        right_val = self.right_term.calculate()
        if self.operator == '+':
            return right_val + left_val
        else:
            return right_val * left_val


class Term_One:
    def __init__(self, tokens):
        self.expr = None
        token = tokens.pop(0)
        if token == '(':
            self.expr = Expression_One(tokens)
            while tokens[0] != ')':
                self.expr = Expression_One(tokens, self.expr)
            tokens.pop(0)
            
        elif all(c in string.digits for c in token):
            self.expr = Int(token)
        else:
            raise Exception('SANITY CHECK 2 FAILED')

    def __repr__(self):
        return str(self.expr)

    def calculate(self):
        return self.expr.calculate()

class Int:
    def __init__(self, value):
        self.value = int(value)
    
    def __repr__(self):
        return str(self.value)

    def calculate(self):
        return self.value

class Expression_Two:
    def __init__(self, tokens, left_term=None):
        print("E")
        if left_term:
            self.left_term = left_term
        else:
            self.left_term = Factor_Two(tokens)
        if tokens and tokens[0] == '*':
            token = tokens.pop(0)
            print(f"E pop: {token}")
            self.right_term = Factor_Two(tokens)
        else:
            self.right_term = None

    def __repr__(self):
        return f"({self.left_term} * {self.right_term})"

    def calculate(self):
        left_val = self.left_term.calculate()
        if self.right_term:
            right_val = self.right_term.calculate()
        else:
            right_val = 1
        return right_val * left_val


class Factor_Two:
    def __init__(self, tokens, left_factor=None):
        print("F")
        if left_factor:
            self.left_factor = left_factor
        else:
            self.left_factor = Term_Two(tokens)
        
        if tokens and tokens[0] == '+':
            token = tokens.pop(0)
            print(f"F pop: {token}")
            self.right_factor = Factor_Two(tokens)
        else:
            self.right_factor = None

    def __repr__(self):
        return f"({self.left_factor} + {self.right_factor})"

    def calculate(self):
        left_val = self.left_factor.calculate()
        if self.right_factor:
            right_val = self.right_factor.calculate()
        else:
            right_val = 0
        return right_val + left_val

class Term_Two:
    def __init__(self, tokens):
        print("T")
        self.expr = None
        token = tokens.pop(0)
        print(f"T pop: {token}")
        if token == '(':
            self.expr = Expression_Two(tokens)
            while tokens[0] != ')':
                self.expr = Expression_Two(tokens, self.expr)
            print(f"T pop: {tokens.pop(0)}")
            
        elif all(c in string.digits for c in token):
            self.expr = Int(token)
        else:
            raise Exception('SANITY CHECK T FAILED')

    def __repr__(self):
        return str(self.expr)

    def calculate(self):
        return self.expr.calculate()

def parse_one(tokens):
    main_expr = Expression_One(tokens,)
    while tokens:
        main_expr = Expression_One(tokens, main_expr)
    return main_expr

def part_one():
    equations = tokenize()
    results = []
    for equation in equations:
        expr = parse_one(equation)
        results.append(expr.calculate())
    print(sum(results))

def parse_two(tokens):
    main_expr = Expression_Two(tokens,)
    while tokens:
        main_expr = Expression_Two(tokens, main_expr)
    return main_expr

def part_two():
    equations = tokenize()
    results = []
    for equation in equations:
        expr = parse_two(equation)
        print(expr)
        results.append(expr.calculate())
    print(sum(results))

def main():
   part_one()
   part_two()


if __name__ == "__main__":
    main()
