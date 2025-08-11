'''
Optimized implementation of bubble sort.
'''


def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        is_sorted = True
        
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False

        if is_sorted:
            return arr

    return arr
