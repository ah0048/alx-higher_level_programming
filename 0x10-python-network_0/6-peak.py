#!/usr/bin/python3
'''module for peak function'''


def find_peak(list_of_integers):
    '''function to find peak integer in unsorted list'''
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    else:
        list_of_integers.sort()
        return (list_of_integers[-1])
