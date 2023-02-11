# normalise.py
# Author: Nur Bujang
# to create a program that reads in a string and strips any leading or trailing spaces.
# the program should also convert the string to lower case (converts all the letters to lower case)'
# The program should also output the length of the input and output strings (It then outputs the lengths of the original string and the normalised one).
# https://www.w3schools.com/python/python_strings_methods.asp

raw_string=input("Please enter a string:")
normalised_string=raw_string.strip().lower()

length_of_raw_string=len(raw_string)
length_of_normalised=len(normalised_string)

print(f"That String normalised is:{normalised_string}")
print(f"we reduced the input string from {length_of_raw_string} to {length_of_normalised} characters")