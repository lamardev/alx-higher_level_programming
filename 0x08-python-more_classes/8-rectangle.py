#!/usr/bin/python3
""" Module 1-rectangle
Defines a Rectangle class

"""


class Rectangle:
    """ Creates a class Rectangle with width and height """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes a new `Rectangle` """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """ Returns the user firendly string reprsentation of Rectangle
        """
        rect = []
        if self.width == 0 or self.height == 0:
            return ''
        return '\n'.join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """  Return a string representation of the rectangle to be able to
        recreate a new instance by using eval()
        """
        return f"{type(self).__name__}({self.width}, {self.height})"

    def __del__(self):
        """ Called when an instance of Rectangle is deleted """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """ Calculates for the area of the Rectangle

        Returns:
            area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Claculates the perimeter of the Rectangle

        Return:
            0 if width or height is 0
            else: (l + h) * 2
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
