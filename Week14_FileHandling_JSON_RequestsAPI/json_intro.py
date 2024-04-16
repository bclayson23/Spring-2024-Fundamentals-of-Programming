# JSON - java script object notation

emp_data = """{
    "employees": [
        {
            "name": "John",
            "age": 29,
            "email": ["john@gmail.com", "john@outlook.com"]
        },
        {
            "name": "Jane",
            "age": 48,
            "email": null
        }
    ]
}
"""

import json
# to load JSON string into a python object
json_data = json.loads(emp_data)
# print(json_data)
# print(type(json_data))
# print(json_data["employees"])
#
# for emp in json_data["employees"]:
#     print(emp["name"])

"""
# Delete the email for each employee and then load it into a json string
for emp in json_data["employees"]:
    del emp["email"]


print(json_data)

# convert a python object into json string
new_string = json.dumps(json_data, indent=2)
print(new_string)
print(type(new_string))
"""

# load json data from a file into python object
with open("states.json", "r") as files_obj:
    data = json.load(files_obj)

# print(data)
# print(type(data))

for state in data["states"]:
    print(state["name"], state["abbreviation"])

    # remove the area code for each state
    del state["area_codes"]

print(data["states"])

# to write json data to a file
with open("new_states.json", "w") as file_obj:
    json.dump(data, file_obj, indent=2)


# API --> Application Programming Interface

"""
Address --> user entered address, recommended address 16701-12345
web application --> USPS API --> valid and return appropriate address
"""

"""
Fidelity Investments --> facebook page, twitter handle, linkedin
Facebook API - JSON Format
posts, comments, replies, etc.
"""

# import random
#
# random.random()
# random.choice()

