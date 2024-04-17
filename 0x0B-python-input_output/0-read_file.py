#!/usr/bin/python3
'''module for read function'''


def read_file(filename=""):
    '''function to read a file'''
    with open(filename, encoding="utf-8") as file:
        print(file.read())
