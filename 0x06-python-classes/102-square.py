#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int or float): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int or float: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int or float: The area of the square.

        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if the area of the current square is equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Checks if the area of the current square is not equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.

        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Checks if the area of the current square is less than the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Checks if the area of the current square is less than or equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less than or equal, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """
        Checks if the area of the current square is greater than the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Checks if the area of the current square is greater than or equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
