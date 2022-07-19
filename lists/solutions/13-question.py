#!/usr/bin/python3
'''13-question'''


def three_by_four_by_six_array():
    '''
    generates a 3*4*6 3D array whose each element is *
    '''

    return [[['*' for x in range(6)]
            for x in range(4)] for x in range(6)]
