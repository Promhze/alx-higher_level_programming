#!/usr/bin/python3
"""Creates a student class"""


class Student:
    """class defines a student with public instance"""

    def __init__(self, first_name, last_name, age):
        """Initialise the student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method that returns the dictionary
        representation of the public instance"""

        return self.__dict__
