#!/usr/bin/python3
# calc.py
# from the internet somewhere

import sys

args = sys.argv[1:]

operation = args[0]
num1 = int(args[1])
num2 = int(args[2])

functions = {
    'add': lambda num1, num2: num1 + num2,
    'subtract': lambda num1, num2: num1 - num2,
    'multiply': lambda num1, num2: num1 * num2,
    'divide': lambda num1, num2: num1 / num2
}

total = functions[operation](num1, num2)

print(total)
