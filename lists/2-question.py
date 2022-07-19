#!/usr/bin/python3
"""2-question"""


def multiply_elements(my_list=[]) -> int:
    """
    Multiplies all the items in a list

    Args:
        my_list: list of of numbers

    Returns:
        product of all numbers
    """

    for item in my_list:
        if not isinstance(item, (int, float)):
            raise TypeError("list must have numbers only")

    return __import__('functools').reduce(lambda x, y: x * y, my_list)
