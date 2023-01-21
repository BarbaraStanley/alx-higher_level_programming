#!/usr/bin/python3
''' imports all functions from calculator_1.py and handles basic operations '''

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operator = ['+', '-', '*', '/']
    if len(sys.argv)-1 != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op not in operator:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    if op == operator[0]:
        print('{} {} {} = {}'.format(a, op, b, add(a, b)))
    if op == operator[1]:
        print('{} {} {} = {}'.format(a, op, b, sub(a, b)))
    if op == operator[2]:
        print('{} {} {} = {}'.format(a, op, b, mul(a, b)))
    if op == operator[3]:
        print('{} {} {} = {}'.format(a, op, b, div(a, b)))
