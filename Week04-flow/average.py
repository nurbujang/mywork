# average.py
# This program reads in numbers until the user enters 0 
# (the program should append each of them into a list)
# it will them print back out the numbers again and their average
# Author: Nur Bujang

numbers=[]

# first number then we check if it is 0 in the while loop
number=int(input("enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    # read the next number and check if 0
    number=int(input("enter another (0 to quit): "))

for value in numbers:
    print (value)

# I want average to be a float
average=float(sum(numbers)) / len(numbers)
print(f"The average is {average}")


