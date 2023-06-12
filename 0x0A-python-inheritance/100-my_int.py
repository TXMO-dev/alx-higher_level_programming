#!/usr/bin/python3
"""
Defines a MyInt class that inherits from int.
"""

class MyInt(int):
    """
    Represents a rebellious integer.
    """

    def __init__(self, value):
        """
        Initializes a MyInt instance.
        Args:
            value (int): The value of the MyInt.
        """
        super().__init__(value)

    def __eq__(self, other):
        """
        Overrides the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator.
        """
        return super().__eq__(other)


# Test cases
if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
