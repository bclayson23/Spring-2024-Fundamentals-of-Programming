import logging


# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


num1 = 12
num2 = 4

"""
add_res = add(num1, num2)
logging.warning(f"{num1} + {num2} = {add_res}")

sub_res = subtract(num1, num2)
logging.warning(f"{num1} - {num2} = {sub_res}")


# WARNING is current default level of logging
# Changing the default level of logging
logging.basicConfig(level=logging.DEBUG)

mul_res = multiply(num1, num2)
logging.debug(f"{num1} * {num2} = {mul_res}")
 
div_res = divide(num1, num2)
logging.debug(f"{num1} / {num2} = {div_res}")
"""

# Writing log statements to a file with a timestamp
logging.basicConfig(filename="log_sample.log", level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s")

add_res = add(num1, num2)
logging.debug(f"{num1} + {num2} = {add_res}")

sub_res = subtract(num1, num2)
logging.warning(f"{num1} - {num2} = {sub_res}")