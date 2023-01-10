#!/usr/bin/python3
"""Creates a student class"""


class Student:
    """class defines a student with public instance"""

    def __init__(self, first_name, last_name, age):
        """Initialise the student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that returns the dictionary
        representation of the public instance"""

        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()
