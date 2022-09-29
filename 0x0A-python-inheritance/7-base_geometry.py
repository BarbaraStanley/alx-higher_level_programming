#!/usr/bin/python3
'''A class that calculates area and validates a value'''


class BaseGeometry:
    ''' Class for geometry calculations '''
    def area(self):
        '''function to calculate area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name='', value):
        ''' A function that validates value'''
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
