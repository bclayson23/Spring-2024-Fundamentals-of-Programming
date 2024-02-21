'''
# Question 1 Coin Toss Game
import random

user_choice = "yes"

while user_choice.lower() == "yes":
    user_move = (input("The computer will flip a coin, pick heads or tails: ")).lower()

    rand_num = round(random.random(), 2) # assigning the computer choice
    coin = ""

    if rand_num <= 1 / 2:
        coin = "heads"
    else:
        coin = "tails"

    result = ""

    if user_move == coin:  # checking user against computer
        result = "Tie"
    elif user_move == "heads":
        if coin == "tails":
            result = "You Win"
    elif user_move == "tails":
        if coin == "heads":
            result = "You Lose"
    else:
        print("That is not a correct choice")

    print(f"You picked {user_move}, Computer picked {coin}, - {result}!")
    user_choice = (input("Would you like to play again? yes or no: ")).lower()


# Question 2 Write a program that prints the multiples of 5 from the given list with the following conditions.
list1 = [12, 75, 150, 180, 145, 525, 50]

for num in list1:
    if num % 5 == 0:
        if num > 500:  # stopping if over 5
            break
        elif num > 150:  # continuing with next iteration
            continue
        print(num, end=" ")


# Question 3 Create a pattern depending on number of rows
rows = int(input("Enter a number of rows: "))
count = 0
for i in range(1, rows + 1):  # determining range
    count = count + 1
    for j in range(0, i + count):
        if j % 2 == 0:  # only odd numbers
            continue
        else:
            print(j, end=" ")
    print()


# Question 4 Ask the user to input a target number. Write a program to display the list of factors for each of the
# numbers until target

target_num = int(input("Enter a target number: "))

list1 = []

for numbe in range(1, target_num + 1):  # making list of numbers
    list1.append(numbe)

for num in range(1, target_num + 1):
    end = []
    for numb in list1:
        if num % numb == 0:  # appending the factors into lists
            end.append(numb)
    print(f"Factors of {num}: {end}")
'''