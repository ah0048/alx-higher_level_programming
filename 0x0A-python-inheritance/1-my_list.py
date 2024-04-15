#!/usr/bin/python3
'''module for mylist class'''


class MyList(list):
    '''class to sort lists'''

    def print_sorted(self):
        '''prints the list, but sorted (ascending sort)'''
        new_list = sorted(self)
        print("{}".format(new_list))
