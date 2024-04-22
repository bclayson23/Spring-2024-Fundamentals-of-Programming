# Question 24

number = 250  # flipped number and the value

while number <= 1000:  # word not in all caps
    if number >= 750:  # flipped symbols and added colon
        print(number)
        number = number + 100
    else:  # added colon
        print(number * 2)
        number = number + 50  # moved line in to keep contained in loop

# Question 25
val = 25  # flipped the word and value

for i in range(0, val):  # took out the word "the" and added a colon
    if i % 2 == 0:
        print(i + 1)
    else:
        print(i - 1)  # added a parentheses

# Question 26
weather = "raining"

if weather == "sunny":  # added a second "=" sign to check
    print("wear sunblock")
elif weather == "snow":  # added a second "=" sign to check
    print("going skiing")
else:
    print(weather)
