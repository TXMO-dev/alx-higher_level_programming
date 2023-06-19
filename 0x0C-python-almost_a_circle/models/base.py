#!/usr/bin/python3
"""
Base Module
"""

import json
import turtle


class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance
        Args:
            id (int): Unique id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): List of dictionaries
        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): List of instances
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        Args:
            json_string (str): JSON string
        Returns:
            list: List of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Args:
            **dictionary: Double pointer to a dictionary
        Returns:
            instance: Instance with attributes set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads and returns a list of instances from a file
        Returns:
            list: List of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                obj_list = cls.from_json_string(json_data)
                return [cls.create(**obj) for obj in obj_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes and writes the CSV representation of list_objs to a file
        Args:
            list_objs (list): List of instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    elif cls.__name__ == "Square":
                        row = [obj.id, obj.size, obj.x, obj.y]
                    writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes and returns a list of instances from a CSV file
        Returns:
            list: List of instances
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                obj_list = []
                for row in reader:
                    row = [int(val) for val in row]
                    if cls.__name__ == "Rectangle":
                        obj = cls(row[1], row[2], row[3], row[4], row[0])
                    elif cls.__name__ == "Square":
                        obj = cls(row[1], row[3], row[2], row[0])
                    obj_list.append(obj)
                return obj_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles (list): List of Rectangle instances
            list_squares (list): List of Square instances
        """
        turtle.bgcolor("white")
        turtle.title("Draw")
        turtle.setup(800, 600)

        pen = turtle.Turtle()
        pen.speed(2)
        pen.penup()

        for rect in list_rectangles:
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.penup()

        for square in list_squares:
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)
            pen.penup()

        turtle.done()
