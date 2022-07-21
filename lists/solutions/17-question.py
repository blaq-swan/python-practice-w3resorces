#!/usr/bin/python3
"""17-question"""


def except_first_last(n=31):
    """
    print a list except for the first 5 elements squared
    """

    return [pow(x, 2) for x in range(n)][6:]
