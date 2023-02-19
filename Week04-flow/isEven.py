# isEven.py
# Lab 4.1
# Author: Nur Bujang
# to write a program that asks the user to enter in a number, 
# and the program will tell the user if the number is even or odd.

# if, elif, else

#number=int(input("enter an integer:"))

#if (number % 2) == 0:
    #print(f"{number} is an even number")
#else:
    #print(f"{number} is an odd number")

# How would you use a while loop to modify 1 so that it keeps prompting the user for a number until the user enters -1
# sentinal controled loop
# Method 1
# number=int(input("enter an integer:"))
# while number != -1:

#     if (number % 2) == 0:
#         print(f"{number} is an even number")
#     else:
#         print(f"{number} is an odd number")
#     break

#Method 2
# while True:
#     number=int(input("enter an integer:"))

#     if number==-1:
#         break

#     elif (number % 2) == 0:
#         print(f"{number} is an even number")
#     else:
#         print(f"{number} is an odd number")

#Method 3
x=True
while x is True:
    number=int(input("enter an integer:"))

    if number==-1:
        x=False
    elif (number % 2) == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")