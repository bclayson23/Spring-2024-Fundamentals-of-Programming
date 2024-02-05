# if-else
'''
height = int(input("Please enter your height in cm: "))

if height > 120:
    print("Can Ride")

else:
    print("Can't Ride")


#nested if-else

height = int(input("Please enter your height in cm: "))

if height > 120:
    print("Can Ride")
    age = int(input("Enter your age: "))
    if age > 18:
        print("Ticket is $12")
    else:
        print("Ticket is $7")
else:
    print("Can't Ride")


# nested if-else with elif
height = int(input("Please enter your height in cm: "))
bill = 0

if height > 120:
    print("Can Ride")
    age = int(input("Enter your age: "))
    if age < 12:
        ticket_price = 5
        print("Ticket is $5")
    elif 12 <= age < 18:
        ticket_price = 7
        print("Ticket is $7")
    elif 18 <= age < 45:
        ticket_price = 12
        print("Ticket is $12")
    else:
        ticket_price = 0
        print("Ticket is free")
    want_photos = input("Do you want a photo taken? Enter Y/y or N/n: ")

    if want_photos == "Y" or want_photos == "y":
        bill = ticket_price + 3

    if want_photos == "N" or want_photos == "n":
        bill = ticket_price

    print(f"Your final bill is ${bill}")


else:
    print("Can't Ride")


# grades question
grade = int(input("Enter your number grade: "))

if grade <= 60:
    print("F")

elif grade <= 70:
    if grade < 63:
        print("D-")
    elif grade < 67:
        print("D")
    else:
        print("D+")

elif grade <= 80:
    if grade < 73:
        print("C-")
    elif grade < 77:
        print("C")
    else:
        print("C+")

elif grade <= 90:
    if grade < 83:
        print("B-")
    elif grade < 87:
        print("B")
    else:
        print("B+")

elif grade <= 100:
    if grade < 93:
        print("A-")
    elif grade < 97:
        print("A")
    else:
        print("A+")

else:
    print("Invalid Input")
'''

# Exercise
# Ask user to enter a digit between 0 and 9
# Return corresponding word
# Ex: 1 is one

number = int(input("Enter a value between 0 and 9: "))

if number == 0:
    print("Zero")
elif number == 1:
    print("One")
elif number == 2:
    print("Two")
elif number == 3:
    print("Three")
elif number == 4:
    print("Four")
elif number == 5:
    print("Five")
elif number == 6:
    print("Six")
elif number == 7:
    print("Seven")
elif number == 8:
    print("Eight")
elif number == 9:
    print("Nine")
else:
    print("Invalid Number")
