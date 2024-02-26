# logic errors are errors within the code, runtime exceptions arent picked up until running
"""
print("Hello")


# normal statements
a = 5
b = 0

# critical statement
try:
    print(a/b)
except Exception:
    print("cannot divide by zero")
print("bye")
"""
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Connection opened")
except ZeroDivisionError as e:
    print("Something went wrong. ", e)
except ValueError as e:
    print("Something went wrong. ", e)
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print("Connection closed")

print("End")
