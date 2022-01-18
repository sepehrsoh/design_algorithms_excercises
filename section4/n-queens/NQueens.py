class NQueens(object):
    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.N = n

    def is_safe(self, board, row, col) -> bool:
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1),
                        range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.N, 1),
                        range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def print_solution(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.board[i][j], end=" ")
            print()

    def solve_nq_util(self, col) -> bool:
        if col >= self.N:
            return True
        for i in range(self.N):
            if self.is_safe(self.board, i, col):
                self.board[i][col] = 1
                if self.solve_nq_util(col + 1):
                    return True
                self.board[i][col] = 0
        return False

    def solve(self):
        if not self.solve_nq_util(0):
            print("Solution does not exist")
            return
        self.print_solution()
