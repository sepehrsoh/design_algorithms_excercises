import binarysearch as bs

if __name__ == '__main__':
    # test data
    arr = [2, 3, 4, 10, 40]
    x = 10

    binary_search = bs.Binary_Search(arr, x)

    result = binary_search.solve()
    if result == -1:
        print("element in array not found")
    else:
        print("your element found in {}th elements of your array".format(result + 1))
