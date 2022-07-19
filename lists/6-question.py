#!/usr/bin/python3
"""6-question"""


def sort_by_last_element(my_list=[]):
    """
    Sort by the last element
    """

    return sorted(my_list, key=lambda x: x[1])
