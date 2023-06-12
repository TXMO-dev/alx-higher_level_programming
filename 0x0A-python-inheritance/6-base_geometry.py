#!/usr/bin/python3
"""
this is the improvement on the base geometry
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
