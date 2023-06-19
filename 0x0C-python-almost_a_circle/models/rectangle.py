#!/usr/bin/python3
"""
Rectangle Module
"""

class Rectangle:
    """
    Rectangle class
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
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            int: Area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Prints the rectangle using '#' characters
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance
        in the format [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Assigns attributes to the Rectangle instance
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle instance
        Returns:
            dict: Dictionary representation of the Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

