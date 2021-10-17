def find(array):
    if array[0] < array[1]:
        mini = array[0]
        maxi = array[1]
    else:
        mini = array[1]
        maxi = array[0]
    for i in range(0, len(array) - 2, 2):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
        if array[i] < mini:
            mini = array[i]
        if array[i + 1] > maxi:
            maxi = array[i + 1]
    if array[len(array) - 1] > maxi:
        maxi = array[len(array) - 1]
    return mini, maxi


if __name__ == "__main__":
    a = [2, 1, 3, 4, 5, 19, 11, 20, 21]
    minimum, maximum = find(a)
    print("min = {} , max = {}".format(minimum, maximum))
