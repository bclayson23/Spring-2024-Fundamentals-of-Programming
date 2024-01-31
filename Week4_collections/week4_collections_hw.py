'''
# Question 1: Access value 20 from the tuple. tuple1 = (“Car”, [34, 23, 8], False, [15, 20, 11])
tuple1 = ("car", [34, 23, 8], False, [15, 20, 11])
print(tuple1[3][1])


# Question 2: Slice the last 3 elements of the given list. List1 = [44, 12, 578, 21, 134, 67]
list1 = [44, 12, 578, 21, 134, 67]
print(list1[3:])


# Question 3: Write a program to replace 20 with 200 in list1 = [5, 10, 15, 20, 75, 100, 50]. Try this approach:
# Use list1.index to get the position of 20. Then do list[position] = 200
list1 = [5, 10, 15, 20, 75, 100, 50]
num_position = list1.index(20)
list1[num_position] = 200
print(list1)


# Question 4: Change the value of 33 to 66 in the given tuple. tuple1 = (11, [64, 33], 243, 123
tuple1 = (11, [64, 33], 243, 123)
tuple1[1][1] = 66
print(tuple1)


# Question 5: Return a new set with unique items from both sets by removing duplicates.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.union(set2)
print(set3)


# Question 6: Create a new list by picking the odd-index items from the first list and even indexed items from the
# second list. list1 = [3, 6, 9, 12, 15, 18, 21], list2 = [4, 8, 12, 16, 20, 24, 28]
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

odd = list1[1::2]
even = list2[0::2]

list3 = [odd + even]
print(list3)
'''

# Question 7
