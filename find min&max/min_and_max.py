def min_max(array):
    if len(array) == 1:
        return a[0], a[0]
    if len(array) == 2:
        if array[0] < array[1]:
            return array[0], array[1]
        else:
            return array[1], array[0]
    mid = len(array) // 2
    min1, max1 = min_max(array[:mid])
    min2, max2 = min_max(array[mid:])
    return min(min1, min2), max(max1, max2)


if __name__ == "__main__":
    a = [2, 1, 3, 4, 5, 19, 11, 20]
    minimum, maximum = min_max(a)
    print("min = {} , max = {}".format(minimum, maximum))
