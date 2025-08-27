'''
Optimized implementation of bubble sort.
python -m memory_profiler bubble_sort_opt.py 
'''

from memory_profiler import profile

def main():
    numbers_05k = [i for i in range(5000, 0, -1)]
    opt_bubble_sort(numbers_05k.copy())

@profile
def opt_bubble_sort(arr):

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

if __name__ == "__main__":
    main()