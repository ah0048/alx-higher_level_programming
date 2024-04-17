#!/usr/bin/python3
'''module for write function'''


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
