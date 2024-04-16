# open command
# with open -> context manager

"""
# 1. using the open command
# with files --> read, write, append
file_obj = open("sample_text", "r")
# default mode is "r"

print(file_obj.name)
print(file_obj.mode)

# close the file obj
# file_obj.close()
"""

# "with open" --> context management
with open("sample_text", "r") as file_obj:
    # print(file_obj.name)
    # print("Inside the with open: ", file_obj.closed)
    # file_contents = file_obj.read()
    # print(file_contents)

    # to access one line at a time
    # for line in file_obj:
    # print(line)

    # prints a line for each line of code
    # file_content = file_obj.readline()
    # print(file_content)
    #
    # file_content = file_obj.readline()
    # print(file_content)
    #
    # file_content = file_obj.readline()
    # print(file_content)

    # prints certain characters for each line of code
    size_to_read = 100
    #
    # file_contents = file_obj.read(size_to_read)
    # print(file_contents)
    #
    # file_contents = file_obj.read(size_to_read)
    # print(file_contents)
    #
    # file_contents = file_obj.read(size_to_read)
    # print(file_contents)

    # when no more characters to return, read returns empty string

    file_contents = file_obj.read(size_to_read)
    while len(file_contents) > 0:
        print(file_contents, end="*")
        file_contents = file_obj.read(size_to_read)

    # unable to write in read more

# print(file_obj.closed)  # checking if closed
