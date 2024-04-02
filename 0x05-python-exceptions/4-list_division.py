#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    res = []
    for i in range(0, list_length):
        try:
            res.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            res.append(0)
            print("wrong type")
            continue
        except IndexError:
            res.append(0)
            print("out of range")
            continue
        except ZeroDivisionError:
            res.append(0)
            print("division by 0")
            continue
        finally:
            pass
    return res
