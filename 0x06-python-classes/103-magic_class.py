#!/usr/bin/python3
"""
This module defines the MagicClass that performs various calculations related to circles.
"""

import math

class MagicClass:
    """
    Represents a circle and provides methods to calculate its area and circumference.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with the given radius.

        Args:
            radius (float or int): The radius of the circle. Defaults to 0.
        
        Raises:
            TypeError: If the radius is not a number (float or int).
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
