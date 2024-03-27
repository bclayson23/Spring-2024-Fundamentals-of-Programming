# Function that takes in a number and returns the square of it
"""
def square_num(a):
    return a * a


print(square_num(5))

square_num1 = lambda x: x * x
print(square_num1(5))

hello = lambda x: f"Hello {x}"
print(hello("Billy"))

# Write a lambda function that checks whether a number is even or not
check_even = lambda num: "Even number" if num % 2 == 0 else "Odd Number"
# print(check_even(int(input("Enter a number: "))))
print(check_even(17))

# Immediately Invoked Function Expressions or IIFEs
print((lambda x: f"Hello {x}")("Ryan"))

print((lambda x: x * 5)(2))


add_nums = lambda x,y: x+y
print(add_nums(2, 3))


# HIGHER ORDER FUNCTIONS --> filter, map, reduce

# USING FILTER -> filters out numbers
nums = [3, 2, 6, 8, 4, 6, 2, 9]


def is_even(n):
    return n % 2 == 0


even_nums = filter(is_even, nums)
print(list(even_nums))

# As a lambda
even_nums1 = filter(lambda n: n % 2 == 0, nums)
print(list(even_nums1))


# USING MAP -> effects all in list
def update_num(n):
    return n * 2


doubles = map(update_num, nums)
print(list(doubles))

doubles1 = map(lambda n: n * 2, nums)
print(list(doubles1))


# Length of strings in list
cities = ["Boston", "New York", "Miami", "Los Angeles", "Phoenix"]

str_length = map(lambda n: len(n), cities)
print(list(str_length))
"""

# USING REDUCE -> used to reduce a given list to a single number
nums = [3, 2, 6, 8, 4, 6, 2, 9]
from functools import reduce


def add_all(a, b):
    return a + b


sum_value = reduce(add_all, nums)
print(sum_value)

sum_value1 = reduce(lambda a,b: a + b, nums)
print(sum_value1)