#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg = len(sys.argv) - 1
    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argumet:")
    else:
        print("{} arguments:".format(arg))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
