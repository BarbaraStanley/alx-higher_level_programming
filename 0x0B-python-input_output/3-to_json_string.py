#!/usr/bin/python3
import json
''' A function that returns the JSON representation of an object (string)'''


def to_json_string(my_obj):
    ''' Converts given object to JSON representation
        Args:
        MY_OBJ(object): a python object
    '''
    y = json.dumps(my_obj)
    return y
