#!/usr/bin/python3
'''a class Rectangle that defines a rectangle by:

Private instane attribute: width:
    property def width(sef): to retrieve it
    property setter def width(self, value): to set it:

     Private instance attribute: height:
     property def height(self): to retrieve it
     property setter def height(self, value): to set it:

     Instantiation with optional width and height:
     def __init__(self, width=0, height=0):
     Public instance method: def area(self): that returns the rectangle area
     Public instance method: def perimeter(self):
     that returns the rectangle perimeter:
     if width or height is equal to 0, perimeter is equal to 0
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
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''retrieves the private instance attribute: height'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''property setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns the rectangle area'''
        return self.__height * self.__width

    def perimeter(self):
        '''Returns the rectangle perimeter'''
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return (2 * (self.__height + self.__width))
