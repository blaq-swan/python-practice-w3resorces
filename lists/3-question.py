#!/usr/bin/python3
"""3-question"""


def get_largest_number(my_list):
    """
    Gets the largets nu,ber in a list
    """

    for item in my_list:
        if not isinstance(item, (int, float)):
            raise TypeError("list must have numbers only")

    return sorted(my_list)[-1]
