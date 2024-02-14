'''
# Question 1: Write a program to print a list of all prime numbers till a given target number
target_num = int(input("Enter a number greater than one: "))
prime_list = []

if target_num <= 1:
    print("Enter a number greater than one")
elif target_num == 2:
    prime_list.append(target_num)
    print(prime_list)
else:
    for num in range(2, target_num):
        isPrime = True
        for i in range (2, num):
            if num % i == 0:
                isPrime = False
                break
        if isPrime is True:
            prime_list.append(num)
    print(prime_list)


# Question 2: Write a list to print a list of all even numbers till a given target number
target_num = int(input("Enter a number greater than one: "))
even_list = []

if target_num <= 1:
    print("Enter a number greater than one")

for num in range(2, target_num +1, 2):
    even_list.append(num)

print(even_list)


# Question 3: Use a loop to display elements from a given list present at odd index positions

list1 = [10, 20, 30, 40, 50, 60]

print(list1[1::2])

# Question 4: Find the highest number from a given list of numbers using for loop. Do not use any in-built functions.

list1 = [10, 24, 8, 187, 34, 100]
highest_number = 0

for num in list1:
    if highest_number < num:
        highest_number = num

print(highest_number)
'''
