from functools import lru_cache

def fibonacchi(n):
    x1, x2 = 1, 1
    for i in range(n):
        print(x1, end= ',')
        x1, x2 = x2, x1 + x2

print(fibonacchi(25))

@lru_cache()
def fibonacchi(n):
    x1, x2 = 1, 1
    for i in range(n):
        print(x1, end= ',')
        x1, x2 = x2, x1 + x2

print(fibonacchi(25))


@lru_cache(maxsize=10)
def fibonacchi(n):
    x1, x2 = 1, 1
    for i in range(n):
        print(x1, end= ',')
        x1, x2 = x2, x1 + x2

print(fibonacchi(25))


@lru_cache(maxsize=16)
def fibonacchi(n):
    x1, x2 = 1, 1
    for i in range(n):
        print(x1, end= ',')
        x1, x2 = x2, x1 + x2

print(fibonacchi(25))

