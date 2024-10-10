import random
from random import randrange

list_nums = [random.randrange(1, 101) for i in range(100)]

def nums_func():
    for i in list_nums:
        if i % 2 != 0:
            print(i ** 2) #return??
print(nums_func())
