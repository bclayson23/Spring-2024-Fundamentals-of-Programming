from functools import reduce
nums = [3, 2, 6, 8, 4, 6, 2, 9]
# Question 1 Product of 2 arguments
product = lambda x, y: x * y
print(product(4, 5))

# Question 2 IIFE for difference
print((lambda m, n: m - n)(5, 3))

# Question 3 filter and lambda for numbers greater than 5
greater_five = filter(lambda g: g > 5, nums)
print(list(greater_five))

# Question 4 Lambda num/5 if number greater than 10. otherwise num + 5
greater_ten = lambda t: t/5 if t > 10 else t + 5
print(greater_ten(15))

# Question 5 map and lambda multiply every number by 2
doubles = map(lambda num: num * 2, nums)
print(list(doubles))

# Question 6
# i odd numbers in given list
odd_nums = list(filter(lambda o: o % 2 != 0, nums))
print(odd_nums)

# ii square of each odd number
square = list(map(lambda odds: odds * odds, odd_nums))
print(square)

# iii sum of squared odd numbers
sum_square = reduce(lambda a,b: a + b, square)
print(sum_square)