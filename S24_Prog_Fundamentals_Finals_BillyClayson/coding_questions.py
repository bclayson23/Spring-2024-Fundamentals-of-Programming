# Question 27: Using lambda
from functools import reduce
"""
list1 = [14, 17, -13, -75, 150, 15, 19, 10, -3, 16, 9, -145, 12, 50]


# a: find the odd numbers
odd_nums = list(filter(lambda o: o % 2 != 0, list1))
print(odd_nums)


# b: subtract 5 from odd numbers
minus_five = list(map(lambda odds: odds - 5, odd_nums))
print(minus_five)

# c: sum of all values in b
sums = reduce(lambda a,b: a + b, minus_five)
print(sums)
"""

# Question 28: reading a file
# a: creating the file
# b: read file and print in the console
"""
with open("sample.txt", "r") as file_obj:
    file_contents = file_obj.read()
    print(file_contents)
"""

# Question 29: Creating file and importing module
# it worked successfully


# Question 30: Using requests API, retrieve JSON data on products from http://dummyjson.com/products
# Access and print all the titles of the products
"""
from urllib.request import urlopen
import json

with urlopen("https://dummyjson.com/products") as response:
    api_response = response.read()

data = json.loads(api_response)

for product in data["products"]:
    print(product["title"])
"""
