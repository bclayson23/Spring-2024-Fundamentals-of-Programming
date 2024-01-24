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


