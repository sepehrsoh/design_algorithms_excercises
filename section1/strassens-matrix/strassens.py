import math
from typing import List, Tuple


def split_matrix(a: List, ) -> Tuple[List, List, List, List]:
    if len(a) % 2 != 0 or len(a[0]) % 2 != 0:
        raise Exception("Odd matrices are not supported!")

    matrix_length = len(a)
    mid = matrix_length // 2

    top_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
    bot_right = [
        [a[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)
    ]

    top_left = [[a[i][j] for j in range(mid)] for i in range(mid)]
    bot_left = [[a[i][j] for j in range(mid)] for i in range(mid, matrix_length)]

    return top_left, top_right, bot_left, bot_right


def matrix_dimensions(matrix: List) -> Tuple[int, int]:
    return len(matrix), len(matrix[0])


class Strassen:
    def __init__(self, matrix_a: List, matrix_b: List):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    def strassen(self):
        if matrix_dimensions(self.matrix_a)[1] != matrix_dimensions(self.matrix_b)[0]:
            raise Exception(
                f"Unable to multiply these matrices, please check the dimensions. \n"
                f"Matrix A:{self.matrix_a} \nMatrix B:{self.matrix_b}"
            )
        dimension1 = matrix_dimensions(self.matrix_a)
        dimension2 = matrix_dimensions(self.matrix_b)

        if dimension1[0] == dimension1[1] and dimension2[0] == dimension2[1]:
            return self.matrix_a, self.matrix_b

        maximum = max(max(dimension1), max(dimension2))
        maxim = int(math.pow(2, math.ceil(math.log2(maximum))))
        new_matrix1 = self.matrix_a
        new_matrix2 = self.matrix_b

        # Adding zeros to the matrices so that the arrays dimensions are the same and also
        # power of 2
        for i in range(0, maxim):
            if i < dimension1[0]:
                for j in range(dimension1[1], maxim):
                    new_matrix1[i].append(0)
            else:
                new_matrix1.append([0] * maxim)
            if i < dimension2[0]:
                for j in range(dimension2[1], maxim):
                    new_matrix2[i].append(0)
            else:
                new_matrix2.append([0] * maxim)

        final_matrix = self.actual_strassen(new_matrix1, new_matrix2)

        # Removing the additional zeros
        for i in range(0, maxim):
            if i < dimension1[0]:
                for j in range(dimension2[1], maxim):
                    final_matrix[i].pop()
            else:
                final_matrix.pop()
        return final_matrix

    def actual_strassen(self, matrix_a: List, matrix_b: List) -> List:
        if matrix_dimensions(matrix_a) == (2, 2):
            return default_matrix_multiplication(matrix_a, matrix_b)

        a, b, c, d = split_matrix(matrix_a)
        e, f, g, h = split_matrix(matrix_b)

        t1 = self.actual_strassen(a, matrix_subtraction(f, h))
        t2 = self.actual_strassen(matrix_addition(a, b), h)
        t3 = self.actual_strassen(matrix_addition(c, d), e)
        t4 = self.actual_strassen(d, matrix_subtraction(g, e))
        t5 = self.actual_strassen(matrix_addition(a, d), matrix_addition(e, h))
        t6 = self.actual_strassen(matrix_subtraction(b, d), matrix_addition(g, h))
        t7 = self.actual_strassen(matrix_subtraction(a, c), matrix_addition(e, f))

        top_left = matrix_addition(matrix_subtraction(matrix_addition(t5, t4), t2), t6)
        top_right = matrix_addition(t1, t2)
        bot_left = matrix_addition(t3, t4)
        bot_right = matrix_subtraction(matrix_subtraction(matrix_addition(t1, t5), t3), t7)

        new_matrix = []
        for i in range(len(top_right)):
            new_matrix.append(top_left[i] + top_right[i])
        for i in range(len(bot_right)):
            new_matrix.append(bot_left[i] + bot_right[i])
        return new_matrix

    def solve(self):
        return self.strassen()


def default_matrix_multiplication(a: List, b: List) -> List:
    if len(a) != 2 or len(a[0]) != 2 or len(b) != 2 or len(b[0]) != 2:
        raise Exception("Matrices are not 2x2")
    new_matrix = [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]
    return new_matrix


def matrix_addition(matrix_a: List, matrix_b: List):
    return [
        [matrix_a[row][col] + matrix_b[row][col] for col in range(len(matrix_a[row]))]
        for row in range(len(matrix_a))
    ]


def matrix_subtraction(matrix_a: List, matrix_b: List):
    return [
        [matrix_a[row][col] - matrix_b[row][col] for col in range(len(matrix_a[row]))]
        for row in range(len(matrix_a))
    ]
