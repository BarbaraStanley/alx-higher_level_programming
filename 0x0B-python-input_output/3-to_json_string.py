#!/usr/bin/python3
''' A function that returns the JSON representation of an object (string)'''


import json


def to_json_string(my_obj):
    ''' Converts given object to JSON representation
        Args:
        MY_OBJ(object): a python object
    '''
    y = json.dumps(my_obj)
    return y
