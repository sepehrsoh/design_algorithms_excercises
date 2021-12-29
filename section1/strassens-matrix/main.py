import strassens as s
import numpy as np

if __name__ == '__main__':
    # test data
    matrix_a = [
        [2, 3, 4, 5],
        [6, 4, 3, 1],
        [2, 3, 6, 7],
        [3, 1, 2, 4],
        [2, 3, 4, 5],
        [6, 4, 3, 1],
        [2, 3, 6, 7],
        [3, 1, 2, 4],
        [2, 3, 4, 5],
        [6, 2, 3, 1],
    ]
    matrix_b = [
        [0, 2, 1, 1],
        [16, 2, 3, 3],
        [2, 2, 7, 7],
        [13, 11, 22, 4],
    ]
    strassen = s.Strassen(matrix_a, matrix_b)
    print("result: {}".format(strassen.solve()))
