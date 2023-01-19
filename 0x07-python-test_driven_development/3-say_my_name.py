#!/usr/bin/python3
"""Module containint a function to print first and last name"""


def say_my_name(first_name, last_name=""):
    """ prints first and last name
        Arguments:
            @first_name: first name to be printed
            @second_name: last_name to be printed
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(second)name) is not str:
        raise TypeError("second_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
