#!/usr/bin/env python3
import operator

op = {
     '+': operator.add,
     '-': operator.sub,
     '*': operator.mul,
     '/': operator.floordiv,
}

def calculate(arg):
    # stack for calculator
    tokens = arg.split()

    stack = []

    # process tokens
    while len(tokens) > 0:
        token = tokens.pop(0)
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            val2 = int(stack.pop())
            val1 = int(stack.pop())

            # Look up function in table
            func = op[token]
            result = func(val1, val2)
            
            tokens.insert(0, result)
            
    return result

def main():
    while True:
        result = calculate(input('rpn calc> '))
        print(result)

if __name__ == '__main__':
    main()
