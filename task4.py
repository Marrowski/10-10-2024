import time
from functools import lru_cache

def time_func(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        time_in_sec = end - start
        time_in_msec = time_in_sec * 1000
        print(f'Time to execute program {time_in_msec} msec')
        return result
    return wrapper

@time_func
def fibonacchi(n):
    x1, x2 = 1, 1
    for i in range(n):
        print(x1, end= ',')
        x1, x2 = x2, x1 + x2

print(fibonacchi(25))

@time_func
@lru_cache()
def fibonacchi(n):
    x1, x2 = 1, 1
    for i in range(n):
        print(x1, end= ',')
        x1, x2 = x2, x1 + x2

print(fibonacchi(25))

@time_func
@lru_cache(maxsize=10)
def fibonacchi(n):
    x1, x2 = 1, 1
    for i in range(n):
        print(x1, end= ',')
        x1, x2 = x2, x1 + x2

print(fibonacchi(25))

@time_func
@lru_cache(maxsize=16)
def fibonacchi(n):
    x1, x2 = 1, 1
    for i in range(n):
        print(x1, end= ',')
        x1, x2 = x2, x1 + x2

print(fibonacchi(25))
