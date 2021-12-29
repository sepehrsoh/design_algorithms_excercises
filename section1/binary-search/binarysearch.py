class Binary_Search:
    def __init__(self, array, element):
        self.arr = array
        self.x = element

    def binary_search(self):
        low = 0
        high = len(self.arr) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2

            if self.arr[mid] < self.x:
                low = mid + 1

            elif self.arr[mid] > self.x:
                high = mid - 1

            else:
                return mid

        return -1

    def solve(self):
        return self.binary_search()
