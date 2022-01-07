import sys

INF = sys.maxsize


class ShortestPath:
    def __init__(self, values):
        self.length = len(values)
        self.graph = values
        self.dis = [[0 for _ in range(self.length)] for _ in range(self.length)]
        self.Next = [[0 for _ in range(self.length)] for _ in range(self.length)]
        self.initialise()
        self.shortest_path()

    def initialise(self):
        for i in range(self.length):
            for j in range(self.length):
                self.dis[i][j] = self.graph[i][j]
                if self.graph[i][j] == INF:
                    self.Next[i][j] = -1
                else:
                    self.Next[i][j] = j

    def construct_path(self, u, v):
        if self.Next[u][v] == -1:
            return {}
        path = [u]
        while u != v:
            u = self.Next[u][v]
            path.append(u)
        return path

    def shortest_path(self):
        for k in range(self.length):
            for i in range(self.length):
                for j in range(self.length):
                    if self.dis[i][k] == INF or self.dis[k][j] == INF:
                        continue
                    if self.dis[i][j] > self.dis[i][k] + self.dis[k][j]:
                        self.dis[i][j] = self.dis[i][k] + self.dis[k][j]
                        self.Next[i][j] = self.Next[i][k]

    @staticmethod
    def print_path(path):
        result = ""
        n = len(path)
        for i in range(n - 1):
            result += str(path[i])
            result += " -> "
        result += str(path[n - 1])
        return result

    def solve(self):
        for i in range(self.length):
            for j in range(self.length):
                if i != j:
                    path = self.construct_path(i, j)
                    print("Shortest path from {} to {} is : {}".format(i, j, self.print_path(path)))
