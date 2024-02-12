'''
# Question 1: Write a program that takes a digit as an input and returns the corresponding word.

list1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  # bases off of the index

num = int(input("Enter a digit between 0 and 9: "))

if 0 <= num <= 9:
    print(list1[num])

else:
    print("Invalid Input")

# other way
dict1 = {
    0: "zero",
    1: "one",
    2: "two",
}

print(dict1.get(num))  #uses the index of the corresponding input
'''

# Question 2: Rock Paper Scissors
import random

# rand_num = random.random()  # generates random value between 0 and 1
# print(round(rand_num,2))

# Rock Paper Scissors ASCII Art

# Rock
user_choice = "yes"

while user_choice.lower() == "yes":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

    # Paper
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

    # Scissors
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

    user_move = (input("Pick a move: rock/paper/scissors")).lower()  # simple rock paper scissors rules

    rand_num = round(random.random(), 2)  # this number generator will decide the computers choice
    comp_move = ""



    if 0 <= rand_num < 1 / 3:
        comp_move = "rock"
    elif 1 / 3 <= rand_num < 2/3:
        comp_move = "paper"
    else:
        comp_move = "scissors"

    result = ""

    if user_move == comp_move:
        result = "Tie."
    elif user_move == "rock":
        if comp_move == "paper":
            result = "You Lose."
        else:
            result = "You Win."
    elif user_move == "paper":
        if comp_move == "rock":
            result = "You Win."
        else:
            result = "You Lose."
    elif user_move == "scissors":
        if comp_move == "rock":
            result = "You Lose."
        else:
            result = "You Win."
    else:
        print("Invalid Input")


    print(f"You Picked {user_move}. Computer Picked {comp_move}. {result}")  # gives the user results
    user_choice = input("Do you want to continue? Enter yes or no: ")

print("Thank you!")



'''
# Question 3: Write a program that takes year as input and checks whether the given year is leap or not.

year = int(input("Please enter a year: "))

if year % 4 == 0:  #this checks if they are divisible by four if not it is an automatic fail, if so it runs through more
    if year % 100 == 0:  #this checks if they are divisible by 100
        if year % 400 == 0:  #this checks if they are divisible by 400
            print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it is a leap year")
else:
    print("it is not a leap year")


# Question 4: Write a program that simulates the logic shown in the below flowchart

print("Welcome to Treasure Island. Your mission is to find the treasure!")

first_choice = (input("To begin your adventure will you go left or right? ")).lower()  # if the user chooses the right option,
# they will be able to continue
if first_choice == "left":
    print("You head towards a big lake.")

    second_choice = (input("The waters seem rough, will you swim or wait? ")).lower()
    if second_choice == "wait":
        print("You wait until the water dies down and swim across. You find three doors.")

        last_choice = (input("You see a red door, a blue door, and a yellow door. Which one will you enter? ")).lower()
        if last_choice == "red":
            print("You have been burned by scolding fire. Game Over!")
        elif last_choice == "blue":
            print("You have been eaten by giant beasts. Game Over!")
        elif last_choice == "yellow":
            print("You have found the treasure. You Win!")
        else:
            print("You did not choose a door and died of boredom. Game Over!")

    else:
        print("You have been attacked by a swarm of trout. Game Over!")

else:
    print("You have fallen into a snake pit and died! Game Over!")

'''
