#!/usr/bin/python3
"""4-question"""


def get_smallest_number(my_list):
    """
    Gets the smallest number in a list
    """

    for item in my_list:
        if not isinstance(item, (int, float)):
            raise TypeError("list must have numbers only")

    return sorted(my_list)[0]
