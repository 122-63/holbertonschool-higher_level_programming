#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for columna in fila:
            print("{}".format(columna), end="")
            if columna != fila[len(fila) - 1]:
                print(" ", end="")
        print("")
