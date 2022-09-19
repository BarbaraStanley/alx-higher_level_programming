#!/usr/bin/python3
''' a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
'''


class Square:
    '''A square class'''
    def __init__(self, size):
        '''Class initialization'''
        self.__size = size
