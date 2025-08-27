from merge_sort import merge_sort
from counting_sort import counting_sort

def my_benchmark(func, arr):
    func(arr)

# Benchmark para n grande, k pequeño
def test_merge_sort_small_k(benchmark):
    n = 10000
    arr = list(range(n, 0, -1))  # Orden inverso
    benchmark.pedantic(
        my_benchmark,
        args=(merge_sort, arr),
        rounds=5,
        warmup_rounds=1,
        iterations=1
    )

def test_counting_sort_small_k(benchmark):
    n = 10000
    arr = [0] * n  # Todos iguales, fuerza el recorrido completo de conteo
    benchmark.pedantic(
        my_benchmark,
        args=(counting_sort, arr),
        rounds=5,
        warmup_rounds=1,
        iterations=1
    )
