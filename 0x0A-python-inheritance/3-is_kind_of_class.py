#!/usr/bin/python3
''' A function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
'''


def is_kind_of_class(obj, a_class):
    ''' function to check if an object is an instance of the specified class,
    or a class tha inherited from it'''

    if isinstance(obj, a_class):
        return True
    else:
        return False
