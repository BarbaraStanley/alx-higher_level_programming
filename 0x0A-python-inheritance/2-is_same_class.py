#!/usr/bin/python3
''' A function that returns True if the object is
    exactly an instance of the specified class ; otherwise False
'''


def is_same_class(obj, a_class):
    '''Checks if an objject is exactly an instance of given class'''
    if type(obj) == a_class:
        return True
    else:
        return False
