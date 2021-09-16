#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = []
    for fila in matrix:
        new_m.append(list(map(lambda x: x**2, fila)))
    return new_m
