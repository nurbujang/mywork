# Messing with for loops
# Author: Nur Bujang

# for elem in list:
    # do something

# for number in range(1,10):
    # do something

# boats=['Sigma','x yacht','Swan'] # make boats into a list with 3 strings in it

# for boat in boats:
#     print("i'd rather be out in a ", boat) # boat is a different variable from boats

# # # add in a separator: string inserted between values, default space
# boats=['Sigma','x yacht','Swan'] # make boats into a list with 3 strings in it

# for boat in boats:
#     print("i'd rather be out in a ", boat, sep="") # boat is a different variable from boats

# # # add in a separator and if you want it to be in the same line
# boats=['Sigma','x yacht','Swan'] # make boats into a list with 3 strings in it

# for boat in boats:
#     print("i'd rather be out in a ", boat, sep="",end="") # boat is a different variable from boats

# # if you want it to be double spaced, look in print statement in builtin function:
# boats=['Sigma','x yacht','Swan'] # make boats into a list with 3 strings in it

# for boat in boats:
#     print("i'd rather be out in a ", boat, sep="",end="\n\n") # boat is a different variable from boats

# back to separator:
boats=['Sigma','x yacht','Swan'] # make boats into a list with 3 strings in it

for boat in boats:
    print("i'd rather be out in a ", boat, sep="") # boat is a different variable from boats

for i in range(0,10):
    print (i)

print("all done i is now", i) 
# # notice it only did i is 0-9, which is 1 less than 10, so be careful with range. 
# # unlike while loop which goes until 10, so be careful with range, bc it does not let u do the last one. 
# # it will go up to, but not including that last value


# # in list
# #if "Swan" in boats:
#     #print("that is a boat")

# # in list
# if "swan" in boats: # small letter swan is not in the list
#     print("that is a boat")  