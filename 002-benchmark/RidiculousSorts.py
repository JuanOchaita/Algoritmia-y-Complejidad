import random

def bogosort(arr):
    while arr != sorted(arr):
        random.shuffle(arr)
    return arr

def stalin_sort(arr):
    if not arr:
        return []
    result = [arr[0]]
    for x in arr[1:]:
        if x >= result[-1]:
            result.append(x)
    return result

def my_benchmark(func, n):
    arr = [i for i in range(n,0,-1)]
    func(arr)

def test_bogosort_pedantic(benchmark):
    benchmark.pedantic(
        my_benchmark,
        args=(bogosort, 10),
        rounds=100,
        warmup_rounds=10,
        iterations=1
    )

def test_stalin_sort_pedantic(benchmark):
    benchmark.pedantic(
        my_benchmark,
        args=(stalin_sort, 1000),
        rounds=100,
        warmup_rounds=10,
        iterations=1
    )