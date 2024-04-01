import os

# get current working directory
print(os.getcwd())

# change the directory
# os.chdir("C:\\Users\\WJC30\\OneDrive - University of Pittsburgh\\Spring 2024 Fundamentals of Programming")
# print(os.getcwd())

# list all the files at the current location
print(os.listdir())

# create a new directory
# mkdir -> to create single directory
# makedirs -> to create hierarchy of directories
# os.mkdir("Dir1")
# print(os.listdir())

# os.makedirs("Dir2\\Dir2_1")
print(os.listdir())

# to remove dirs
# just delete one by one
# os.rmdir("Dir1")
# os.removedirs("Dir2\\Dir2_1")

# print(os.stat("test"))
# added_time = os.stat("test").st_atime
#
# from datetime import datetime
# print(datetime.fromtimestamp(added_time))

import calendar as cal
print(cal.month(2024, 4))
print(cal.calendar(2075))
print(cal.HTMLCalendar().formatmonth(2024, 4))