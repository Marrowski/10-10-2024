import time

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
def product_nums(a: int, b:int):
    return a * b

print(product_nums(5, 4))