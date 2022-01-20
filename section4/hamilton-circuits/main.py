def print_solution(path):
    print("Solution Exists: Following",
          "is one Hamiltonian Cycle \npath :")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0], "\n")


class HamiltonCircuits(object):
    def __init__(self, g):
        self.graph = g
        self.V = len(graph)

    def is_safe(self, v, pos, path):

        if self.graph[path[pos - 1]][v] == 0:
            return False

        for vertex in path:
            if vertex == v:
                return False

        return True

    def hamilton_cycle_util(self, path, pos):
        if pos == self.V:
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False
        for v in range(1, self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v
                if self.hamilton_cycle_util(path, pos + 1):
                    return True
                path[pos] = -1

        return False

    def solve(self):
        path = [-1] * self.V
        path[0] = 0

        if not self.hamilton_cycle_util(path, 1):
            print("Solution does not exist\n")
            return False

        print_solution(path)
        return True


if __name__ == '__main__':
    graph = [[0, 1, 0, 1, 0],
             [1, 0, 1, 1, 1],
             [0, 1, 0, 0, 1],
             [1, 1, 0, 0, 1],
             [0, 1, 1, 1, 0]]
    hp = HamiltonCircuits(graph)
    hp.solve()
    graph2 = [[0, 1, 0, 1, 0],
              [1, 0, 1, 1, 1],
              [0, 1, 0, 0, 1],
              [1, 1, 0, 0, 0],
              [0, 1, 1, 0, 0]]
    hp = HamiltonCircuits(graph2)
    hp.solve()
