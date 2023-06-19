#!/usr/bin/python3
"""
Square Module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance
        Args:
            size (int): Size of the square (width and height)
            x (int): x-coordinate of the square's position
            y (int): y-coordinate of the square's position
            id (int): Unique id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for size attribute
        Returns:
            int: Size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute
        Args:
            value (int): New size value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns attributes to the Square instance
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the Square instance
        in the format [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
