#!/usr/bin/python3
'''A class Rectangle that defines a rectangle by:

    Private instance attribute: width:
    property def width(self): to retrieve it
    property setter def width(self, value): to set it

    Prvate instance attribute: height:
    property deheight(self): to retrieve it
    if property setter def height(self, value): to set it

    Instantation with optional width and height:
    def__init__(self, width=0, height=0):
    '''


class Rectangle:
    '''Class that defines a rectangle

    Args:
        width: int
        height: int
    '''

    def __init__(self, width=0, height=0):
        '''Initializes the class'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''retrieves the private instance attribute: width'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''property setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''retrieves the private instance attribute: height'''
        return (self.__height)

    @height.getter
    def height(self, value):
        '''property setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
