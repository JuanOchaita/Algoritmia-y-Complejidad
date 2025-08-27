'''
Merge sort implementation.
'''

import math


def merge(left_arr, right_arr):
    # New array and indexes    
    merged = []
    i, j = 0, 0

    # Sentinels
    left_arr.append(math.inf)
    right_arr.append(math.inf)

    # Merge lists respectively
    while left_arr[i] != math.inf or right_arr[j] != math.inf:
        if left_arr[i] < right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1

    # Remove sentinels
    left_arr.pop()
    right_arr.pop()

    return merged


def merge_sort(arr):
    # Conquer
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Combine
    return merge(left, right)

def main():
    # # Test
    arr = [7, 8, 9, 5, 10, 15, 11, 12]
    sorted_arr = merge_sort(arr)
    print("Unsorted array:", arr)
    print("Sorted array:", sorted_arr)


    # arr_a = [2, 5, 8, 9]
    # arr_b = [1, 1, 7, 16]
    # print(merge(arr_a, arr_b))

if __name__ == "__main__":
    main()
