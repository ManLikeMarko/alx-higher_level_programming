#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    """
    computes the square value of all integers of a matrix.
    Args:
    matrix=[]: inputmatrix
    Returns:
    squared matrix
    """
    result_matrix = []

    for row in matrix:
        result_row = []

        for element in row:

            result_row.append(element ** 2)

            result_matrix.append(result_row)

            return result_matrix
