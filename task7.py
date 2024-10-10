from functools import partial

#Звичайна
prod = lambda a, b: a * b
print(prod(20, 5))

#Карована
product = partial(prod, 2)
result = product(7)
print(result)
