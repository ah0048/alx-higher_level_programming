#!/usr/bin/python3
'''module for mylist class'''


class MyList(list):
    '''class to sort lists'''
    pass

    def print_sorted(self):
        '''prints the list, but sorted (ascending sort)'''
        new_list = sorted(list(self))
        print(new_list)
