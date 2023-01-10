#!/usr/bin/python3
""" A class that demonstrates inheritance."""


class MyList(list):
    """ My list is inherited from list class"""

    def print_sorted(self):
        """prints the list in ascending order."""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
