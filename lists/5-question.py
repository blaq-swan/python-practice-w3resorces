#!/usr/bin/python3


def count_string(my_list=[]):
    """
    counts the number of strings
    length of string should be 2 or more
    first and last character are the same
    """

    for item in my_list:
        if not isinstance(item, str):
            raise TypeError("list must have strings only")

    return len([x for x in my_list if len(x) >= 2 and x[0] == x[-1]])
