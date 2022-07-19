#!/usr/bin/python3
"""1-question"""


def add_elements(my_list=[]) -> int:
    """
    Gets sum of all elements in list

    Args:
        my_list: list of numbers

    Returns:
        sum of all elements in list
    """

    for item in my_list:
        if not isinstance(item, (int, float)):
            raise TypeError("list must have numbers only")

    return __import__('functools').reduce(lambda x, y: x + y, my_list)
