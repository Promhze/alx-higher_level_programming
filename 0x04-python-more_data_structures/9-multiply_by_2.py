#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for i in a_dictionary:
        new_dictionary[i] = 2 * a_dictionary[i]
    return new_dictionary
