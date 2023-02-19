# grade.py
# Lab 4.1
# Author: Nur Bujang
# to write a program that reads in a student’s percentage mark 
# and prints out corresponding the grade 
# (the program should check that the percentage is valid:
# Under 40% => Fail
# Between 40% and 49% => Pass
# Between 50% and 59% => Merit 2
# Between 60% and 69% => Merit 1
# Over 70% => Distinction

#percentage=float(input("Enter the percentage: "))
#print (percentage) # this is for dubugging
#percentage=round(percentage)

# Be careful with the or operator boolean algebra can be tricky
#if percentage < 0 or percentage > 100:
    # Later we will show you error handling
    # This should really throw an error
    #print("Please enter a number between 0 and 100")
#elif percentage < 40: # we know it is greater than 0
    #print("Fail")
#elif percentage < 50: # between 40 and 49
    #print("Pass")
#elif percentage < 60: # between 50 and 59
    #print("Merit1")
#elif percentage < 70: # between 60 and 69
    #print("Merit2")
#else: # the only option left is betwen 70 and 100
    #print ("Distinction")


# In practice the percentages are rounded ie 69.5 gets rounded to 70 so is equal to a Distinction.
# How would you modify the program in 1 to deal with this? I see two ways.
# Method 1
#percentage=float(input("Enter the percentage: "))

# Be careful with the or operator boolean algebra can be tricky
#if percentage < 0 or percentage > 100:
    # Later we will show you error handling
    # This should really throw an error
    #print("Please enter a number between 0 and 100")
#elif percentage < 40: # we know it is greater than 0
    #print("Fail")
#elif percentage < 50: # between 40 and 49
    #print("Pass")
#elif percentage < 60: # between 50 and 59
    #print("Merit1")
#elif percentage < 70: # between 60 and 69
    #print("Merit2")
#else: # the only option left is betwen 70 and 100
    #print ("Distinction")


# In practice the percentages are rounded ie 69.5 gets rounded to 70 so is equal to a Distinction.
# How would you modify the program in 1 to deal with this? I see two ways.
# Method 2?????????
percentage = float(input("Enter the percentage: "))
#print(percentage) # this is for dubugging

# Be careful with the or operator boolean algebra can be tricky
if percentage < 0 or percentage > 100:
    # Later we will show you error handling
    # This should really throw an error
    print("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
    print("Fail")
elif percentage < 50: # between 40 and 49
    print("Pass")
elif percentage < 60: # between 50 and 59
    print("Merit1")
elif percentage < 70: # between 60 and 69
    print("Merit2")
else: # the only option left is betwen 70 and 100
    print ("Distinction")

# Shimanja's - not good
# if 70-percentage<=.5:
    #print("Distinction")
# I believe that data camp has some exercises in python you may want to look at them