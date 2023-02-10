# convert.py
# Author: Nur Bujang
# to create a program that takes in a float amount of dollars and returns that absolute amount in cent.

# I am writing an application, at the moment, in it I take an input of an amount in the form -9.44 (9 dollars and 44 cent)
# the issue there may or may not be a minus sign, and the bank takes in the amount in cent, (944).
# answer should be:
## Please enter am amount:-5.99
## That amount in cent is :599

# number=float(input("Please enter an amount:")) 
# absolute_value=abs(number*100)
# print("The amount in cent is :{}".format(absolute_value))
# gives this output:
## Please enter an amount:-9.44
## The amount in cent is :944.0

# SO, YOU HAVE TO CHANGE THE FLOAT INTO AN INTEGER AFTER AN AMOUNT IS ENTERED
number=float(input("Please enter an amount:")) # you have to enter a float
absolute_value=int(abs(number*100)) # change into an integer after an amount is entered
print("The amount in cent is :{}".format(absolute_value))

