# adding a comment in the remote repo
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


# accessing string characters
emp_name = "Jane Doe"
print(emp_name[3])
# print(emp_name[8]) # throws index out of bounds error because the last char is at idx 7

print(emp_name.index('n'))
'''

# string slicing #
emp_name = "Jane Doe"
print(emp_name[2:6])  # chars from 2 to 6, not including 6
print(emp_name[:4])  # starts from start until 4, not including 4
print(emp_name[2:])  # from 2 til the end
print(emp_name[-4:-1])  # -1 is the last char so -4 is 3 before that
print(emp_name[1:6:2])  # from 1 to 6 by 2

print(emp_name.count('e'))
print(emp_name.find('Doe'))
print(emp_name.replace('Jane', 'John'))

emp_name = emp_name.replace('Jane', 'John')
print('oh' in emp_name)

# String Formatting
student_name = "Alice"
score = 87
print(student_name + ": " + str(score))  # need str to print the number
print("Name: {} Score: {}".format (student_name, score))
# f-strings
print(f'Name: {student_name} Score: {score}')
print(f'10 times 3 is {10*3}')

# testing the connection
