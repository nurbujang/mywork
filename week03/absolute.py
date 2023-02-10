# absolute.py
# Author: Nur Bujang
# to create a program that takes in number and give its absolute value (ie -4 or 4 would both output 4)
# (Give the absolute value of a number)

# In the question, number is ambiguous but the output implies that we should be dealing with floats
# So I am casting the input to a float
number=float(input("Enter a number:"))
absolute_value=abs(number) # underscore is used instead of absoluteValue
# print('The absolute value of {} is {}'.format(number,absolute_value))

# what if we use " instead of '?
print("The absolute value of {} is {}".format(number,absolute_value)) # same answer if we use " instead of '