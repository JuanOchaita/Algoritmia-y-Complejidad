from merge_sort import merge_sort
from counting_sort import counting_sort

def my_benchmark(func, arr):
    func(arr)

# Benchmark para n grande, k mucho mayor que n
def test_merge_sort_large_k(benchmark):
    n = 10000
    k = 100000000
    arr = list(range(k, k-n, -1))  # n valores únicos, muy dispersos
    benchmark.pedantic(
        my_benchmark,
        args=(merge_sort, arr),
        rounds=5,
        warmup_rounds=1,
        iterations=1
    )

def test_counting_sort_large_k(benchmark):
    n = 10000
    k = 100000000
    arr = list(range(k, k-n, -1))  # n valores únicos, muy dispersos
    benchmark.pedantic(
        my_benchmark,
        args=(counting_sort, arr),
        rounds=5,
        warmup_rounds=1,
        iterations=1
    )
