import OptimalBST as bst
from random import randint


class Node:
    def __init__(self, key, freq):
        self.key = key
        self.freq = freq

    def __str__(self):
        return f"Node(key={self.key}, freq={self.freq})"


if __name__ == '__main__':
    nodes = [Node(i, randint(1, 50)) for i in range(10, 0, -1)]
    optimal_bst = bst.OptimalBST(nodes)
    print(optimal_bst.solve())
