#!/usr/bin/python3
'''A class Square that defines a square by:

    Private instane attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
    Instantation with optional size: def__init__(self, size=0):
Public instance method: def area(self): that returns the current square area
'''


class Square:
    '''A class that defines a square'''
    def __init__(self, size=0):
        ''' Class initialization
        Args:
            size(int): The size of the square

        '''
        self.size = size

    def size(self):
        '''retrieve private attribute size'''
        return self.__size

    def size(self, value):
        '''property setter for size'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Returns the current square area'''
        sq = self.__init * self.__init
        return (sq)
