#!/usr/bin/python3
"""get the difference between the two lists"""


def difference_lists(l1, l2) -> list:
    """
    gets the difference between l1 and l2
    """
    unique = []

    for x in l1:
        if x not in l2:
            unique += [x]
    for y in l2:
        if y not in unique and y not in l1:
            unique += [y]

    return unique
