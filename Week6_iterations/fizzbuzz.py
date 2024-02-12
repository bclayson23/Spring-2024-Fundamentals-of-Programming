'''
Take an input value for n

print out numbers from 1 to n with the below conditions
1. If num is divisible by 3 --> print "FIZZ"
2. If num is divisible by 5 --> print "BUZZ"
3. If num is divisible by both 3 and 5 --> print "FIZZBUZZ"
If none of the conditions are satisfied, print the number
'''

target_num = int(input("Enter a target number: "))

for num in range(1, target_num + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
