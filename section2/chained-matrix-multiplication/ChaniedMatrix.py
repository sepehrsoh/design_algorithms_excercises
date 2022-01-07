import sys


class ChainedMatrix:
    def __init__(self, values):
        self.values = values
        self.result = ""

    def chained_matrix(self):
        n = len(self.values)
        rows, cols = (n, n)
        m = [[0 for i in range(cols)] for _ in range(rows)]
        s = [[i + 2 for i in range(cols)] for _ in range(rows)]
        for i in range(1, n):
            m[i][i] = 0

        for L in range(2, n):
            for i in range(1, n - L + 1):
                j = i + L - 1
                m[i][j] = sys.maxsize
                for k in range(i, j):

                    q = m[i][k] + m[k + 1][j] + self.values[i - 1] * self.values[k] * self.values[j]
                    if q < m[i][j]:
                        m[i][j] = q
                        s[i][j] = k
        self.print_optimal_parent(s, 1, n - 1)
        return m[1][n - 1]

    def print_optimal_parent(self, s, i, j):
        if i == j:
            self.result += "A{}".format(i)
        else:
            self.result += "("
            self.print_optimal_parent(s, i, s[i][j])
            self.print_optimal_parent(s, s[i][j] + 1, j)
            self.result += ")"

    def solve(self):
        m = self.chained_matrix()
        print("order : {}".format(self.result))
        return m
