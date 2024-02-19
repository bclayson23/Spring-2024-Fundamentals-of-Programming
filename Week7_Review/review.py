'''
for i in range(11):
    if i > 5:
        break
    else:
        print(i)
# prints from 0 to 5

for i in range(11):
    if i % 2 == 0:
        continue
    else:
        print(i)
# will print odd numbers


# write a program to calculate the sum and average of digits present in a string

total = 0
count = 0

# string_ex = "random289$18@str849ing6"
input_str = input("Enter a string with digits and characters: ")

for char in input_str:
    if char.isdigit():
        total = total + int(char)
        count = count + 1
print(round(total, 2))
print(round(total/count, 2))


# write a program to print the number of digits, letters, and special symbols in a str

digits = 0
letters = 0
symbols = 0

input_str = input("Enter a string with letters, numbers and characters: ")

for char in input_str:
    if char.isalpha():
        letters = letters + 1
    elif char.isdigit():
        digits = digits + 1
    else:
        symbols = symbols + 1
print(f'Digits: {digits}, Letters: {letters}, Symbols: {symbols}')
'''

# do the rows
# 0
# 0 2
# 0 2 4
# 0 2 4 6
# 0 2 4 6 8

rows = int(input("Enter a number of rows: "))
count = 0
for i in range(0, rows):
    count = count + 1
    for j in range(0, i + count):
        if j % 2 == 0:
            print(j, end=" ")
    print()


# Things for exam:
#
# If - else conditions = just one condition
#
# If – elif – else = multiple conditions
#
# = vs == single is assigning double is checking
#
# While loop = x = 1,   while x < 10:,  x = x+1,  print(x)  FOR ITERATION
#
# For loop= for x in range(11):,  print(x)  FOR REPETITION
#
# Break and continue/ Break = breaks the loop/ continue = moves past
#
# Simple game using random module – RPS game
#
# List functions – length, pop, remove, append, insert, extend
#
# Set functions – union, intersection, difference
#
# Pattern Problems (triangle numbers)
#
# Creating empty collections
#
# String to list conversion, list to string conversion
#
# Creating set out of list or string
#
# Dictionaries
#
# Dict.keys, dict.values, dict.items
#
# For value in dict.values():
#
# Use for other operations
