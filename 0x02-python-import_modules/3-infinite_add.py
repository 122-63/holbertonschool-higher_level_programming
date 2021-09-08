#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg = len(sys.argv)
    suma = 0
    for i in range(1, arg):
        suma = suma + int(sys.argv[i])
    print("{}".format(suma))
