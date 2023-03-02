# menu.py
# Last week I got you to make a complicated data structure called student 
# which has two attributes, name and modules which has an array of modules and grades.
# This week as an exercise I would like to create a program that allows a user 
# to create new students and to view students. 
# This will be a big program for you.
# So, we should break it up into smaller bits (this is where functions come in handy)
# 2. Write a function that prints out a menu of commands we can perform, ie add, view and quit. 
# The function should return what the user chose.
# Test the function. We don’t need to worry about error handling yet
# Author: Nur Bujang

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice
#test the function
choice = displayMenu()
print(f"you chose {choice}")