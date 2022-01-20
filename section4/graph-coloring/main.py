import GColor as gc

if __name__ == '__main__':
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    g = gc.Graph(graph)
    numberOfColors = 3
    isTrue = g.solve(numberOfColors)
    if not isTrue:
        print("can't find solution")
