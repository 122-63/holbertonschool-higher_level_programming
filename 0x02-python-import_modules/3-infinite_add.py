#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg = len(sys.argv) - 1
    if arg == 0:
        print("0")
    suma = 0
    for i in range(arg):
        suma = suma + int(sys.argv[i + 1])
    print("{}".format(suma))
