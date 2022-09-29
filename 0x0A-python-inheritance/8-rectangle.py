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


'''A class that inherits from base geometry'''


class Rectangle(BaseGeeometry):
    '''A class that defines a rectangle'''
    def __init__(self, width, height):
        '''method to initialize class'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
