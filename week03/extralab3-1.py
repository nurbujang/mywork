# extralab3-1.py
# Author: Nur Bujang
## Why does this expression cause an error? How can you fix it?
## how to fix it?
## Why is eggs a valid variable name while 100 is invalid?
## # What three functions can be used to get the integer, floating-point number, or string version of a value?

# Why does this expression cause an error? How can you fix it?
# message = 'I have eaten ' + 99 + ' burritos.'
# print (message)
# TypeError: can only concatenate str (not "int") to str

# how to fix it?
message = 'I have eaten ' + str("99") + ' burritos.'
print (message)

# Why is eggs a valid variable name while 100 is invalid?
# Answer: variable must start with a small letter, not a number or upper cases

# What three functions can be used to get the integer, floating-point number, or string version of a value?
# Answer: int(), float() and str()
# The int() , float() , and str( ) functions will evaluate to the integer, floating-point number, and string versions of the value passed to them.