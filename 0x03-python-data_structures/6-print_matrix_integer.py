#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for s in i:
            print('{:d}'.format(s), end=' ')
        print('')
