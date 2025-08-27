'''
Counting sort implementation.
'''


def counting_sort(arr):

    if not arr: 
        return []

    # Find n
    n = len(arr)

    # Find k
    k = max(arr) + 1

    # Create array C
    C = [0] * k

    # Count values in A
    for i in range(n):
        C[arr[i]] += 1

    # Transform C
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    # Create new sorted array B
    B = [None] * n

    for i in range(n - 1, -1, -1):
        C[arr[i]] -= 1
        B[C[arr[i]]] = arr[i]
    
    return B

def main():
    # Test
    print(counting_sort([2, 3, 1, 1, 99]))
    # print(counting_sort([]))

if __name__ == "__main__":
    main()
