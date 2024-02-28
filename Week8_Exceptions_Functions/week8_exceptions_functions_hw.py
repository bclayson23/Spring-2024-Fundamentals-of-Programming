"""
# Question 1: write a program to check whether strings are palindromes
def checkPalindrome(str1, str2):  # the function
    result = ""
    if str1 == str2:  # checking for equal
        result = True
    else:
        result = False
    return result


string1 = input("Enter a string: ")
string2 = (string1[::-1])  # putting string in reverse

isPalindrome = checkPalindrome(string1, string2)  # running function
print(isPalindrome)


# Question 2: write a program to check whether strings are anagrams
def checkAnagram(str1, str2):  # the function
    result = ""
    if string1 == string2:  # checking for match
        result = True
    else:
        result = False
    return result


string1 = sorted(input("Enter a string: "))  # sorting letters to see if they match
string2 = sorted(input("Enter another string: "))

isAnagram = checkAnagram(string1, string2)  # running function
print(isAnagram)


# Question 3: write a function that takes users name, birth year, budget, price of product as inputs and does the
# following
# A: calculates age based on birth year
# B: calculates number of products that can be bought base on budget and price per product(round down)
# C: display the sample output
# D: identify the potential exceptions and structure your code using try, catch, else, excepts, and finally blocks

name = input("Please enter your name: ")  # input from user

current_year = 2024  # setting year

age = ""
amount = ""

try:
    year = int(input("Please enter your birth year: "))  # taking input
    budget = int(input("Please enter your budget: "))
    price = int(input("Please enter the product price: "))
    age = current_year - year  # calculating
    amount = round(budget / price, 0)

except ValueError as e:  # checking for letters
    print(e)
except ZeroDivisionError as e:  # cant divide by zero
    print(e)

finally:
    print(f"Hello {name}! You are {age} years old and you can buy {amount} products!")  # printing result




# Question 4: Write a program to check whether we can create a triangle or not
# If you are given three sticks, you may or may not be able to arrange them in a triangle.
# For example, if one of the sticks is 12 inches long and the other two are one inch long, it is
# clear that you will not be able to get the short sticks to meet in the middle. For any three
# lengths, there is a simple test to see if it is possible to form a triangle:
# If any of the three lengths is greater than the sum of the other two, then you cannot form a
# triangle. Otherwise, you can. (If the sum of two lengths equals the third, they form what is
# called a "degenerate" triangle.)
# Write a function named is_triangle that takes three integers as arguments, and that prints
# either "Yes" or "No," depending on whether you can or cannot form a triangle from sticks
# with the given lengths.
def is_triangle(x, y, z):  # creating the function
    if z > (x + y) or y > (x + z) or x > (y + z):  # checking side lengths
        print("No")
    else:
        print("Yes")


def triangle():
    side1 = int(input("Enter length of the first stick: "))  # asking user for lengths
    side2 = int(input("Enter length of the second stick: "))
    side3 = int(input("Enter length of the third stick: "))

    is_triangle(side1, side2, side3)  # running the function


triangle()  # printing yes or no
"""