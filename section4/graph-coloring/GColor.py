class Graph(object):
    def __init__(self, graph):
        self.V = len(graph)
        self.graph = graph

    def is_safe(self, v, colour, c) -> bool:
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def graph_colour_util(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, colour, c):
                colour[v] = c
                if self.graph_colour_util(m, colour, v + 1):
                    return True
                colour[v] = 0

    def solve(self, m) -> bool:
        colour = [0] * self.V
        if self.graph_colour_util(m, colour, 0) is None:
            return False

        print("Solution exist and Following are the assigned colours:")
        for c in colour:
            print(c, end=' ')
        return True
