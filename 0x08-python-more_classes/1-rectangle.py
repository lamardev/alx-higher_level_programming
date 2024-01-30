#!/usr/bin/python3
""" Module 1-rectangle
Defines a Rectangle class

"""


class Rectangle:
    """ Creates a class Rectangle with width and height """

    def __init__(self, width=0, height=0):
        """ Initializes a new `Rectangle` """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets the width value """
        return self.__width

    @property
    def height(self):
        """ Gets the height value """
        return self.__height

    @width.setter
    def width(self, value):
        """ Sets the value of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Sets the value of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
