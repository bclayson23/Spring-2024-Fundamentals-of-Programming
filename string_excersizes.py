# Question 1: take an input string from the user and create a new string with the
# first, middle, and last characters of the input string

'''
test_string = "score"
print(test_string[0])
print(test_string[-1])
mid_index = int(len(test_string)/2)
print(test_string[mid_index])


user_string = input("please enter a string: ")
print(user_string)

first_char = user_string[0]
last_char = user_string[-1]

# to get the middle character, find length and index of middle character
str_length = len(user_string)
mid_index = int(str_length/2)  # since indies can only be integers
mid_char = user_string[mid_index]  # to access the char at mid_index

result_str = first_char + mid_char + last_char
print(result_str)
'''

# Question 2: : Take an input string from the user and create a new string made of the middle three
# characters of the input string

'''
user_string = input("Please enter a string")
print(user_string)

str_length = len(user_string)
mid_index = int(str_length/2)
mid_char = user_string[mid_index]
print(mid_char)

left_index = mid_index - 1
right_index = mid_index + 1

left_char = user_string[left_index]
right_char= user_string[right_index]

print(left_char + mid_char + right_char)
'''

# Question 3: : Take 2 strings as inputs from the user. Append the second string in the middle of the first
# string

'''
input_str1 = input("please enter the first string: ")
input_str2 = input("please enter the second string: ")

print(input_str1)
mid_index = int(len(input_str1)/2)

first_half = input_str1[:mid_index:1]

first_half = first_half + input_str2

final_str = first_half + input_str1[mid_index:]

print(final_str)
'''

# Question 4: Take a string from the user and reverse it

'''
input_str = input('Please enter a string: ')
print(input_str)
reverse_str = input_str[::-1]
print(reverse_str)
'''

# Question 5:  Extract the amount from the below string

'''
 given_str = "The total value of the 10 products purchased along with the tax is $150"
 print(given_str[-3:1])
'''

# Question 6:  Try to change the 4th character of a given string. Were you able to do it?
# to do this you would use something like str[3] = 'r'




