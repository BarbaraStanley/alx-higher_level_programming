#!/usr/bin/python3
''' A function that returns True if the object is an instance of a class,
    that inherited (directly or indirectly) from the specified class
    ;otherwise False
'''


def inherits_from(obj, a_class):
    '''checks if an object is an instance of a class that inherites
    from given class
    '''
    if type(obj) == int:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
