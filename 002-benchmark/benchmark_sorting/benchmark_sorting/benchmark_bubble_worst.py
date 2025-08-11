''' Bubble sort benchmark. '''

from bubble_sort import bubble_sort
from bubble_sort_opt import bubble_sort as bubble_sort_opt


''' Wrapper '''
def my_benchmark(option):
    n = 2000
    arr_test = [num for num in range(n, 0, -1)]
    option(arr_test)


''' Ejecucion de tests '''
def test_baseline(benchmark):
    benchmark.pedantic(
        my_benchmark,
        args=(bubble_sort,),
        rounds=5,
        iterations=3
    )


def test_optimized(benchmark):
    benchmark.pedantic(
        my_benchmark,
        args=(bubble_sort_opt,),
        rounds=5,
        iterations=3
    )
