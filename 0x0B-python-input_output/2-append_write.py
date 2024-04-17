#!/usr/bin/python3
'''module for append function'''


def append_write(filename="", text=""):
    '''function to append to a file'''
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
