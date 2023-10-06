#!/usr/bin/python3
"""
    A function that divides all ellement of a matrix
    The function takes two arguments and (matrix) and (div)
"""


def matrix_divided(matrix, div):
    """divides all element in matrix by div
    Args:
        matrix list(int): X by X list matrix
        div (int): the divider
    Return:
        returns a new matrix
    """
    list_err = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or type(matrix) is not list:
        raise TypeError(list_err)

    for mat in matrix:
        if type(mat) is not list:
            raise TypeError(list_err)
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    first_matrix_len = len(matrix[0])
    size_err = "Each row of the matrix must have the same size"

    for mat in matrix:
        if len(mat) != first_matrix_len:
            raise TypeError(size_err)
        for i in range(first_matrix_len):
            if type(mat[i]) is not int and type(mat[i]) is not float:
                raise TypeError(list_err)
    new_matrix = []
    for i in range(len(matrix)):
        row = []
        for element in matrix[i]:
            result = element / div
            result = round(result, 2)
            row.append(result)
        new_matrix.append(row)

    return (new_matrix)
