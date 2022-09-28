#!/usr/bin/python3
''' A function that writes an Object to a text file,
    using a JSON representation
'''


import json


def save_to_json_file(my_obj, filename):
    '''converts an object to JSON representation and writes to a text file
        Args:
            my_obj: Python object
            filename(str): name of desired file to write to
    '''
    with open(filename, mode="w", encryption="utf-8") as json_file:
        conv = json.dumps(my_obj)
        json_file.write(conv)
