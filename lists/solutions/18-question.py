#!/usr/bin/python3
"""18-question"""


def permutation(my_list):
    """
    permutation of elements of a list
    """

    if len(my_list) == 0:
        return []

    if len(my_list) == 1:
        return [my_list]

    output = []

    for i in range(len(my_list)):
        m = my_list[i]

        new_list = my_list[:i] + my_list[i+1:]

        for p in permutation(new_list):
            output.append((m,) + tuple(p))
    return output
