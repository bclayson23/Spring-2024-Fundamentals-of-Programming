"""
def sayHello(name):
    print(f"Hello {name}!")


def userDetails():
    user_name = input("Enter a name: ")
    sayHello(user_name)
    user_city = input("Enter your city: ")
    print(f"You are from {user_city}")


userDetails()


def test1(n):
    if (n > 0):
        print("Printing the value")
        print(n)
        print("Calling the function")
        test1(n - 1)


test1(3)  # output 3, 2, 1
print()


def test2(n):
    if (n > 0):  # continues testing and the printing is paused until reaching 0 then it prints starting with 1
        print("Calling the function")
        test2(n - 1)
        print("Printing the value")  # forward then back/ keeps in memory until bottom is resolved, then backtracks
        print(n)


test2(3)  # output 1, 2, 3



# Factorial Ex: 4! = 4 x 3 x 2 x 1/  0! = 1
# can also be 4! = 4 x 3!
# it goes to the bottom of the change and goes back up when bottom gets resolved

def findFactorial(num):
    if num <= 1:
        return 1
    else:
        return num * findFactorial(num - 1)


number = int(input("Enter a number for factorial: "))  # adding a user input to test
factorial_value = findFactorial(number)  # recursion has maximum amount
print(factorial_value)  # printing the factorial answer
"""

# Data Structures and Algorithms use recursions
