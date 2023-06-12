#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)


# Test cases
if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
