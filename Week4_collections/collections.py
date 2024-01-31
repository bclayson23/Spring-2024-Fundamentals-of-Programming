'''
# Lists #
# 1. Allow us to hold duplicate values
# 2. Order is maintained
# 3. Can hold heterogeneous data

list1 = [10, 'test', True, 20.24, 10]
print(list1)

# len() --> returns the number of elements in a list
print(len(list1))

# index and slice
print(list1[2])  # accessing elements at third position
print(list1[1:4])
print(list1[-2])

# lists can hold other lists too
list2 = [10, 'hi', False, 22.12, ['Hello', True, 20]]
print(list2)

# creating an empty list
countries = []

# elements can be added to a list using either append, insert, or extend
countries.append('USA')
countries.append('Canada')
countries.append('Mexico')
print(countries)  # append always adds elements at the end

countries.insert(1, 'France')
print(countries)  # insert is based off index position

countries2 = ['Germany', 'Russia', 'Italy']
countries.extend(countries2)
print(countries)  # extend adds a new list at the end of previous list


countries.append(countries2)
print(countries)  # adds as a list rather than elements


# Remove an element - can use either remove or pop method
countries.remove('France')
print(countries)

countries.pop()
print(countries)

removed_country = countries.pop()
print(removed_country)
print(countries)

print(countries.pop(2))  # pop by default removes last element but can also be specified

# sorting lists
countries.sort()  # in-place functions. modifying the internal contents of the list
print(countries)

num_list = [3434, 2193, 12, 43, 7]
num_list.sort(reverse=True)
print(num_list)

# membership test
print("USA" in countries)

# creating a string from list elements
countries_str = '-'.join(countries)
print(countries_str)

print(type(countries))
print(type(countries_str))

# creating a list by breaking string into different elements
countries3 = countries_str.split('-')
print(countries3)

# Tuples #
# similar to lists but once they are created, we cannot add new elements to it or remove any elements from it

tuple1 = (36, 45, 32, 45, 3468)
print(tuple1)  # order maintained, duplicates allowed
print(tuple1[2])

# tuple1[2] = 89 #cannot modify, add, or remove
# can access or slice a tuple

# Sets #
# 1. do not allow duplicate values
# 2. order is not guaranteed

courses = {'Networking', 'English', 'Math', 'English', 'History'}
print(courses)
print('math' in courses)

# widely used for 'set' operations
courses1 = {'Networking', 'Physics', 'Programming'}
print(courses.intersection(courses1))
print(courses.union(courses1))

print(courses.difference(courses1))
print(courses1.difference(courses))

courses.add('Psychology')
courses.remove('Math')
print(courses)

# Dictionaries #
# store key-value pairs
employees = {
    'id': 2133,
    'name': 'Jane Doe',
    'salary': 4500,
    'skills': ['Java', 'SQL', 'C#'],
    'address': {
        'city': 'NYC',
        'state': 'NY',
        'zip-code': 12213
    }
}

print(employees)

# accessing dictionary values
print(employees['name'])
print(employees['address']['city'])

employees['name'] = 'Ryan'
print(employees)

employees.update({'name': 'Jane Watson', 'salary': 5000})
print(employees)

# deleting keys
del employees['salary']
print(employees)

# accessing keys
print(employees.get('address'))
print(employees.get('phone'))  # comes back with none
print(employees.get('phone', 'Not found!'))


# creating empty collection
list1 = []
tuple1 = ()

# tuple with a single element
tuple2 = (10,)
print(type(tuple2))

# set1 = {}  # will create a dictionary
set1 = set()
print(type(set1))
dict1 = {}
'''

# Accessing collection items
list1 = [34, 43, 65, 7, [45, 56, 20, [1234, 233, 6578]], 4]
print(list1[4][3][1])
list1[2] = 99  # modifying a value - possible for lists and tuples
list1.index(7)  # returns the position of a given value in the list
# returns the position of first occurrence in case of duplicates

# tuples also support indexing and slicing

set1 = {34, 235, 32, 1}
# print(set1[2])
# set1[1] won't work because sets don't maintain order

dict1 = {
    'name': 'John',
    'age': 25,
    'address': {
        'city': 'Boston',
        'state': 'MA',
        'zip': 12434
    },
    'skills': ['Java', 'SQL', 'PHP']
}
print(dict1['address']['state'])
print(dict1['skills'][1])

employee_details = [
    {
        'name': 'John',
        'age': 25,
        'address': {
            'city': 'Boston',
            'state': 'MA',
            'zip': 12434
        },
        'skills': ['Java', 'SQL', 'PHP']
    },

    {
        'name': 'Alex',
        'age': 35,
        'address': {
            'city': 'NYC',
            'state': 'NY',
            'zip': 12434
        },
        'skills': ['Java', 'SQL', 'PHP']
    }
]


# list and tuple to a set
list2 = [343, 3, 5, 8, 10, 3]
set2 = set(list2)
print(set2)
