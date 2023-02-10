# floor.py
# Author: Nur Bujang
# to create a program that takes in a float and outputs an int rounded down, you will need the math module math.floor()
# (floors a number)

import math # math is a built-in module
number_to_floor=float(input("Enter a float number:"))
floored_number=math.floor(number_to_floor)
print("{} floored is {}".format(number_to_floor,floored_number)) # " used instead of '