from time import sleep


''' Funciones a evaluar '''
def func_constant(n: int):

    sleep(0.01)
    return None


def func_linear(n: int):

    for _ in range(n):
        sleep(0.01)
    
    return None


def func_quadratic(n: int):

    for _ in range(n):
        for _ in range(n):
            sleep(0.01)

    return None


''' Wrapper '''
def my_benchmark(option):
    n = 25
    option(n)


''' Ejecucion de tests '''
def test_constant(benchmark):
    # benchmark(my_benchmark, func_constant)
    benchmark.pedantic(
        my_benchmark,
        args=(func_constant,),
        rounds=5,
        iterations=2
    )


def test_linear(benchmark):
    # benchmark(my_benchmark, func_linear)
    benchmark.pedantic(
        my_benchmark,
        args=(func_linear,),
        rounds=5,
        iterations=2
    )

def test_quadratic(benchmark):
    # benchmark(my_benchmark, func_quadratic)
    benchmark.pedantic(
        my_benchmark,
        args=(func_quadratic,),
        rounds=5,
        iterations=2
    )




'''
# Syntax y ejecución de benchmarks 
def test_func_a(benchmark):
    benchmark(my_benchmark, func_constant)
    # benchmark.pedantic(
    #     my_benchmark,
    #     args=(func_constant,),
    #     rounds=1,
    #     iterations=1
    # )

def test_func_b(benchmark):
    benchmark(my_benchmark, func_linear)
    # benchmark.pedantic(
    #     my_benchmark,
    #     args=(func_linear,),
    #     rounds=1,
    #     iterations=1
    # )
    

def test_func_c(benchmark):
    benchmark(my_benchmark, func_quadratic)
    # benchmark.pedantic(
    #     my_benchmark,
    #     args=(func_quadratic,),
    #     rounds=1,
    #     iterations=1
    # )
'''