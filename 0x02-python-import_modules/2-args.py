#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    for i in range(0, args):
        if i == 0:
            if args - 1 != 1:
                print("{:d} arguments".format(args - 1), end="")
                if args == 1:
                    print(".")
                else:
                    print(":")
                continue
            else:
                print("{:d} argument:".format(args - 1))
                continue
        print("{:d}: {:s}".format(i, argv[i]))
        
