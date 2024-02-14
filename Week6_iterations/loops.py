'''
x = 1

while x < 5:
    print(x)
    x += 1
# x = x + 1


# print first 10 natural numbers (start from one)

x = 1

while x <= 10:
    print(x)
    x += 1


# break

x = 1

while x <= 10:
    if x == 5:
        # break  # breaks out of the loop as soon as condition is satisfied
        print("Found 5")
        continue  # will skip the next lines and continue with next iteration once if condition is satisfied
    print(x)
    x += 1


# For Loops #
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num + 2)
    if num == 3:
        break


# Range Function
for i in range(10):
    print(i)


# sum of first 100 numbers
sum = 0
for i in range(101):
    sum = sum + i
    print(sum)



# multiplication table
user_num = int(input("Enter a number"))

for i in range(1, 11, 2):  # range(start, stop, step)
    print(f'{user_num} * {i} = {user_num * i}')
    # print(f'{num}*{i}: ', num*i)


# printing negatives

for i in range(-10, 0):
    print(i)


# Nested Loops
nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in "abc":
        print(num, letter)


# for letter in "abcde":
    # print(letter)


for num in "1":
    print(num)
    for numb in "2":
        print(num, numb)
        for numbe in "3":
            print(num, numb, numbe)
            for number in "4":
                print(num, numb, numbe, number)
                for numbers in "5":
                    print(num, numb, numbe, number, numbers)


rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
'''

rows = int(input("Enter the number of rows: "))
for i in range(0, rows):
    for j in range(rows-i, 0, -1):
        print(j, end=" ")
    print()
