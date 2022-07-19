#!/usr/bin/python3
'''12-question'''


def remove_elements(my_list=[]) -> list:
    '''
    removes element 0, 4, and 5 from my list
    Returns:
        list without the 0th, 4th, and 5th elements
    '''

    return [x for x in my_list if my_list.index(x)not in (0, 4, 5)]
