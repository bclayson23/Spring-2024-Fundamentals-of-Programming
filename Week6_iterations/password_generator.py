import random

letters = list('abcdefghijklmnopqrstuvwxyz')
print(letters)
numbers = list("0123456789")
symbols = list("!@#$%^&*()")

num_letters = int(input("How many letters do you want? "))
num_numbers = int(input("How many numbers do you want? "))
num_symbols = int(input("How many symbols do you want? "))

password_list = []

for letter in range(0, num_letters):
    password_list.append(random.choice(letters))

for number in range(0, num_numbers):
    password_list.append(random.choice(numbers))

for symbol in range(0, num_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = "".join(password_list)
print(password)