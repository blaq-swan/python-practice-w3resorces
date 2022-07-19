#!/usr/bin/python3
'''11-question'''


def common_elements(list_1=[], list_2=[]) -> bool:
    '''
    checks if two lists have at list one common element
    Args:
        list_1: first list
        list_2: second list

    Returns:
        True if lists have at least one common element
        False if no common element
    '''

    for x in list_1:
        for y in list_2:
            if x in list_2 or y in list_1:
                return True
            return False
