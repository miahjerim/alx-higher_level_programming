#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """A class representing a Rectangle."""
    def __init__(self, width=0, height=0):
        """
        Initialisze the Rectangle object.

        Parameters:
            width, height (int): of the rectangle.

        Raises:
            TypeError: Parameters are not int.
            ValueError: Parameters are less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
