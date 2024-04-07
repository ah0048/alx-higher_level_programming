#!/usr/bin/python3
'''module for text identation'''


def text_indentation(text):
    '''method for text identation'''

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    buf = ""
    for ch in text:
        if ch == " " and not buf:
            continue
        elif ch in ['.', '?', ':']:
            buf += ch
            print(buf.strip())
            print()
            buf = ""
        else:
            buf += ch
    if buf:
        print(buf, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
