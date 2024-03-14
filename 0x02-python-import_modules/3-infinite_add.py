#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    sum = 0
    for i in range(1, args):
        sum = sum + int(argv[i])
    print("{:d}".format(sum))
