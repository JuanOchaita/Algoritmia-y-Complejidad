'''
Implementation of bubble sort.
python -m memory_profiler bubble_sort.py 
'''

from memory_profiler import profile

def main():
    numbers_05k = [i for i in range(5000, 0, -1)]
    bubble_sort(numbers_05k.copy())

@profile
def bubble_sort(arr):

    n = len(arr)

    for _ in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == "__main__":
    
    main()
