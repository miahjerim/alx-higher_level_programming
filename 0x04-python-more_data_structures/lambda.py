#!/usr/bin/python3
from functools import reduce
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print("{}".format(list(squared_numbers)))
print()
product = reduce(lambda x, y: x * y, numbers)
print("{}".format(product))
print()
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print("{}".format(list(even_numbers)))