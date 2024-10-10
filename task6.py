def even_numbers(func):
    def wrapper(*args):
        result = func(*args)
        for i in result:
            if i % 2 == 0:
                print(f'Even numbers: {i}')
        return result
    return wrapper

@even_numbers
def fibonacchi(n):
    x1, x2 = 1, 1
    fib = []
    for i in range(n):
        fib.append(x1)
        x1, x2 = x2, x1 + x2
    return fib


print(fibonacchi(10))