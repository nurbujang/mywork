# testBoolean.py
# Author: Nur Bujang
# messing with booleans
# booleans can be True or False
# boolean is the return type of the mathematical operators
# =  <  >  <=  >=
#
# flipped with the not keyword
# be careful using and or

is_alive=True
# print(is_alive)

# Make it neater
print(f"is_alive={is_alive}")

# var=2==4 # not easy to read, eventhough it will work. So:
# var=(2==4) # Means, you're saying the variable var is going to be equal to...
# I asked the question, is 2 equal to 4?
# print(f"var is {var}")

# if you want to check if it's not equal to:
# var=(2!=4) # Means, you're saying the variable var is NOT going to be equal to...
# I asked the question, is 2 equal to 4?
# print(f"var is {var}") # output will be True, because 2 is not equal to 4

# if you want to check if less than or equal to:
var=(2<=4) 
# I asked the question, is 2 less than or equal to 4?
print(f"var is {var}") # output will be True, because 2 is not equal to 4

# you can also have logic. Is logic going to be True or False?
# logic=(2<=100) and (3>=100)
# print(f"logic is {logic}")
# So True and False will turn out the logic of FALSE - because it's AND

# you can also have logic. Is logic going to be either of those things?
# logic=(2<=100) or (3>=100)
# print(f"logic is {logic}")
# So True and False will turn out the logic of FALSE - because it's OR

# but normally it would not be 2 or 3. Normally it would be some kind of variable
# Then you would want to put in var1 and var 2
# grade=400
# is it a valid grade?
# invalid=(grade<0) or (grade>100) # False or True, which will come out as True. it is invalid
# print(f"invalid is {invalid}")
# output is True

# but normally it would not be 2 or 3. Normally it would be some kind of variable
# Then you would want to put in var1 and var 2
grade=40
# is it a valid grade?
invalid=(grade<0) or (grade>100) # False or True, which will come out as True. it is invalid
print(f"invalid is {invalid}")
# output is False