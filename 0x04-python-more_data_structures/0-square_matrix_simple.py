#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = []
    for i in matrix:
        inner_list = []
        for s in i:
            inner_list.append(s**2)
        sqr.append(inner_list)
    return sqr
