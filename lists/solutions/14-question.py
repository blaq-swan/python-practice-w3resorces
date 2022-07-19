#!/usr/bin/python3
'''14-question'''


def remove_even(my_list=[]) -> list:
    '''removes even nu,bers from a list'''

    return [x for x in my_list if not x % 2 == 0]
