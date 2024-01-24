'''
print("Hello World")
# for variable names, do not use reserved keywords
print(help('keywords'))

# Assign multiple variables with the same value simultaneously
a = b = c = 10
print(a, b, c)  # works but not recommended

# Expression vs Statement
x = 47  # statement, just stating
y = 47 + 10  # expression, processing something


# type conversion #
# convert to int
print(int(10.24))
# print(int("10.24")) needs float
print(int("10"))
print(int(float("10.24")))

# convert to str
print(str(20))
print(type(str(20)))

print(list("hello"))


# strings #
# can be created either by using single, double, or triple quotes
first_name = 'jane'
print(first_name)

last_name = "doe"
print(last_name)

address = "10 Main St"
print(address)

job1 = "Physician's Assistant"
print(job1)


# string functions #
emp_name = "Jane Doe"
# len() -->returns the number of characters in a given string
print(len(emp_name))

# upper and lower --> these convert the string into corresponding cases
print(emp_name.upper())

# string concatenation
first_name = "Jane"
last_name = "Doe"
print(first_name + " " + last_name)

age = 24
print(first_name + " " + last_name + ": " + str(age))

# string multiplication
print("hello"*3)
# can only add 2 strings and can only multiply a string with an int
'''

# accessing string characters
emp_name = "Jane Doe"
print(emp_name[3])
# print(emp_name[8]) # throws index out of bounds error because the last char is at idx 7

print(emp_name.index('n'))


