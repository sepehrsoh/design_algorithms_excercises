class SumOfSubsets(object):
    def __init__(self, inputList):
        self.subset_count = 0
        self.list = inputList
        self.results = []

    def subset_sum(self, lists, sums: int, startingIndex, targetSum):
        if sums == targetSum:
            self.subset_count += 1
            if startingIndex < len(lists):
                self.subset_sum(lists, sums - lists[startingIndex - 1], startingIndex, targetSum)
        else:
            for i in range(len(lists)):
                self.subset_sum(lists, sums + lists[i], i + 1, targetSum)

    def solve(self, want_sum: int):
        self.subset_sum(self.list, 0, 0, want_sum)
        print(self.subset_count)


if __name__ == '__main__':
    subsetList = [1, 3, 5, 2]
    ss = SumOfSubsets(subsetList)
    ss.solve(6)
