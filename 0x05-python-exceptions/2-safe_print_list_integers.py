#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, num = 0, 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (TypeError, ValueError):
            continue
    print()
    return num
