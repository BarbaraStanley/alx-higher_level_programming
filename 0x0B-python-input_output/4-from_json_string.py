#!/usr/bin/python3
''' A function that returns an object (Python data structure)
    represented by a JSON string '''


import json


def from_json_string(my_str):
    ''' converts a json sting to a python object'''
    json_str = json.loads(my_str)
    return json_str
