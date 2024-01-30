# part one is in the document string_excersizes

# Question 2: Take user input for first name, last name, age, ssn, height and weight and store them in
# corresponding variables.
# Use f-strings syntax to print below message to the console.

'''
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
ssn = input("Enter your SSN: ")
height = int(input("Enter your height in centimeters: "))
weight = int(input("Enter your weight in pounds: "))

inch_height = height * 0.394

kg_weight = weight * 0.454

print("Hello " + first_name + last_name + "! Thank you for applying. Please find your details below.")
print("Age: " + age)
print("SSN: " + ssn)
print(int("Height: " + str(inch_height)))
print(int("Weight: " + str(kg_weight)))
'''

# Question 3: Consider the below quote

'''
Seuss = "You have brains in your head. You have feet in your shoes. You can steer yourself in any direction you choose. -Dr. Seuss"


# part a: Slice out phrase
print(Seuss[67:110])

# part b: check if quote contains the word feet
print('feet' in Seuss)

# part c: replace
print(Seuss.replace('Dr. Seuss', "Dr Seuss, Oh, the Places You'll Go!"))
'''