#!/usr/bin/python3
"""
this is the second edition
"""
class BaseGeometry:
    """
    Base class for geometry objects.
    """

    def area(self):
        """
        Calculate the area of the geometry object.
        This method should be implemented in the subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer greater than 0.
        Args:
            name (str): The name of the value.
            value: The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
