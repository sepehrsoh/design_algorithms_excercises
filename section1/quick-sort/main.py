import quicksort as qs
if __name__ == '__main__':
    # test data
    arr = [10, 7, 8, 9, 1, 5]
    quick_sort = qs.QuickSort(arr)
    print("list has been sorted \n result : {}".format(quick_sort.solve()))
