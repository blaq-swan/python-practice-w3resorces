#!/usr/bin/python3
"""10-question"""


def find_those_words(n, my_list=[]):
    """finds words that are longer than n

    Args:
        my_list: a list of words
        n: integer to compare against"""

    return [x for x in my_list if len(x) > n]
