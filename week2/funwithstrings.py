# funwithstrings.py
# Author: Nur Bujang
# messing with strings
# showing: 
## escape characters
## adding numbers to strings
## slicing

# escape character
astring="He said \"hello\""
print(astring)

#adding numbers to string
mark=33
string2="Your mark is: "+str(mark)
print(string2)

# slicing
# First, remember that ACCOUNT NUMBER IS A STRING
accountno="123456789"
# print the first 4 digits
# print (accountno[:4])
# or
# print (accountno[0:4])

# print characters from position 2 to position 5 (not included):
# print (accountno[2:5])

# slice to the end
# Get the characters from position 4, and all the way to the end:
# print(accountno[4:])

# slice to the end
# Get the characters from position 5, and all the way to the end (last 4 digits):
print(accountno[5:])
