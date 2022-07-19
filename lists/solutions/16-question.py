#!/usr/bin/python3
'''16-question'''


def first_last_squares(n=21) -> list:
    '''
    generate and print a list of first and last 5 elements squared
    '''

    my_list = [pow(x, 2) for x in range(1, n)]
    return my_list[:5] + my_list[-5:]
