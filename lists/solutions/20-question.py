#!/usr/bin/python3
"""access the index of a list"""


def access_indexes(my_list):
    """
    accesses the indexes of items in a list
    """

    # [print(x, y) for x, y in enumerate(my_list)] # option 1
    [print(my_list.index(y), y) for y in my_list]
