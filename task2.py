import time

def time_function(func):
    def wrapper(*args):
        seconds = time.time()
        print(f'Time to execute function: {seconds} seconds.')
        return func(*args)
    return wrapper

@time_function
def product_num(a: int, b:int):
    result = a * b
    return result

print(product_num(5, 4))