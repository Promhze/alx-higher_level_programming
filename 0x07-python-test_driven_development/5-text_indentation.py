#!/usr/bin/python3

"""A fuction that looks for text indentation"""


def text_indentation(text):

    """Prints 2 new lines after each of these
    characters {'.', '?', ':'}."""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
             [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
