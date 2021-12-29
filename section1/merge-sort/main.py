import mergesort as ms

if __name__ == '__main__':
    # test data
    array = [12, 11, 13, 5, 6, 7]
    merge_sort = ms.MergeSort(array)
    print("list has been sorted \n result : {}".format(merge_sort.solve()))
