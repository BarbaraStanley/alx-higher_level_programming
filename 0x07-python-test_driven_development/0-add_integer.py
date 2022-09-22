#!/usr/bin/python3
'''Addition f two integers using a function'''


def add_integer(a, b=98):
    '''A function that adds 2 integers
    Args:
    a:int
    b:int
    add_integer(2, 3)
    >>> 5
    '''
    if (type(a) is not int or type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int or type(b) is not float):
        raise TypeError("b must be an integer")
    else:
        sum = int(a) + int(b)
        return sum
