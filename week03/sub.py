# sub.py
# Author: Nur Bujang
# to create a program that reads in two numbers and subtracts the first one from the second one (program to subtract one number from another)


# input reads in a string, so we need to convert it into an int so we can perform mathematical operations
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
answer=x-y
print("{} minus {} is {} ".format(x,y,answer))

# what happens if we enter something which is not an integer, eg: hello
# ValueError: invalid literal for int() with base 10: 'hello'

# what happens if we enter something which is not an integer, eg: 1.1
# ValueError: invalid literal for int() with base 10: '1.1'

