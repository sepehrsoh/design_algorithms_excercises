import ShortestPath as sp
import sys

if __name__ == '__main__':
    INF = sys.maxsize
    graph = [[0, 3, INF, 7],
             [8, 0, 2, INF],
             [5, INF, 0, 1],
             [2, INF, INF, 0]]
    shortest_path = sp.ShortestPath(graph)
    shortest_path.solve()
