#!/usr/bin/python3
'''Addition f two integers using a function'''


def add_integer(a, b=98):
    '''A function that adds 2 integers
    Args:
    a:int
    b:int
    >>> add_integer(3,4)
    7
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        sum = int(a) + int(b)
        return sum
