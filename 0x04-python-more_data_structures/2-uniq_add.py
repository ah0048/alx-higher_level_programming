#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    print(my_set)
    sum = 0
    for num in my_set:
        sum = sum + num
    return sum
