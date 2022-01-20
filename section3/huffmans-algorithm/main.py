class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''


class Huffman(object):
    def __init__(self, freqs):
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
        self.chars = chars[:len(freqs)]
        self.nodes = []
        for x in range(len(self.chars)):
            self.nodes.append(Node(freqs[x], chars[x]))

    def solve(self):
        self.create_tree()
        self.print_nodes(self.nodes[0])

    def create_tree(self):
        while len(self.nodes) > 1:
            self.nodes = sorted(self.nodes, key=lambda y: y.freq)

            left = self.nodes[0]
            right = self.nodes[1]

            left.huff = 0
            right.huff = 1

            new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

            self.nodes.remove(left)
            self.nodes.remove(right)
            self.nodes.append(new_node)

    def print_nodes(self, node, val=''):
        new_val = val + str(node.huff)
        if node.left:
            self.print_nodes(node.left, new_val)
        if node.right:
            self.print_nodes(node.right, new_val)
        if not node.left and not node.right:
            print(f"{node.symbol} -> {new_val}")


if __name__ == '__main__':
    freq = [5, 9, 12, 13, 16, 45]
    h = Huffman(freq)
    h.solve()
