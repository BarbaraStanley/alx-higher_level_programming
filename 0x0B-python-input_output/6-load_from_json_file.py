#!/usr/bin/python3
''' A function that creates an Object from a “JSON file” '''


import json


def load_from_json_file(filename):
    ''' Creates a python object from a JSON file'''
    with open(filename) as y:
        return json.load(y)
