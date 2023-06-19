#!/usr/bin/python3
"""
Rectangle Module
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): x-coordinate of the rectangle's position
            y (int): y-coordinate of the rectangle's position
            id (int): Unique id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x attribute
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y attribute
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the Rectangle instance with '#' characters
        taking into account the x and y coordinates
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance
        in the format [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """
        Assigns arguments to each attribute in the following order:
        1st argument -> id attribute
        2nd argument -> width attribute
        3rd argument -> height attribute
        4th argument -> x attribute
        5th argument -> y attribute
        """
        if args and len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                if i < len(attrs):
                    setattr(self, attrs[i], args[i])

