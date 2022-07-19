#!/usr/bin/python3
'''15-question'''


def shuffle_list(my_list=[]) -> list:
    '''shuffles a list'''

    __import__('random').shuffle(my_list)
    return my_list
