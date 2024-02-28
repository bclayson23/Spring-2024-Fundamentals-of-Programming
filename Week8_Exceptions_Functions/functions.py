"""
# Functions - to reuse code



# num --> function parameter
def checkEven(num):
    result = ""
    if num % 2 == 0:
        result = True
    else:
        result = False
    return result


# making a function call
isEven = checkEven(4)
print(isEven)

isEven = checkEven(9)
print(isEven)


print("Hello")  # print function has no return type
import random
randNum = random.random()  # random functions return a number


# attempt at anagram
def checkAnagram(string1, string2):
    result = ""
    if string1 == string2:
        result = True
    else:
        result = False
    return result


one = str(input("Enter a string: "))
two = str(input("Enter a string: "))

isAnagram = checkAnagram(one, two)
print(isAnagram)
"""


# Check for Anagram
def checkAnagram(str1, str2):
    result = ""
    if string1 == string2:
        result = True
    else:
        result = False
    return result


string1 = sorted(input("Enter a string: "))
string2 = sorted(input("Enter another string: "))

isAnagram = checkAnagram(string1, string2)
print(isAnagram)
