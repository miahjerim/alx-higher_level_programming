#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    # Square of matrix
    square_matrix = []
    for row in matrix:
        square_list = list(map(lambda num: num ** 2, row))
        square_matrix.append(square_list)
    return square_matrix
