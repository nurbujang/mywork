# Program to show the format of an if statement
# Author: Nur Bujang

# format of an if statement
# if condition:
#   statements

# if condition:
#   statements(if true)
# else:
#   statements(if false)

# if condition1:
#   statements(if true)
# elif condition2:
#   statements(if condition1 is false but 2 is true)
# else:
#   statements(if both false)

# if True:
#     print("we are in the if statement")

# print("sanity")

# if False:
#    print("we are in the if statement")

# print("sanity") # notice the first one did not print. it prints the next one

# in Python, the IF statement will do whatever is indented. You can also do multiple statements.
# b=1
# if False:
    # print("we are in the if statement")
    # b=22

# print("sanity",b) 

# in Python, the IF statement will do whatever is indented. You can also do multiple statements.
# b=1
# if True:
    # print("we are in the if statement")
    # b=22

# print("sanity",b) 

# else
# b=1
# if True:
    # print("we are in the if statement")
    # b=2

# c=1
# if c==1:
    # print("c is one")
# else:
    # print("c is not one")    
# print("sanity",b) 

# else
b=1
# if True:
    # print("we are in the if statement")
    # b=2

# c=-1
# if c==1:
    #print("c is one")
#else:
    #print("c is not one")    
#print("sanity",b) 

# else
# if c is some text (string)
#b=1
#if True:
    #print("we are in the if statement")
    #b=2

#c="akakajdfakfda"
#if c==1:
    #print("c is one")
#else:
    #print("c is not one")    
#print("sanity",b) 

# else
# if c is some text, even if the text (string) is "1"
#b=1
#if True:
    #print("we are in the if statement")
    #b=2

#c="akakajdfakfda"
#if c==1:
    #print("c is one")
#else:
    #print("c is not one")    
#print("sanity",b) 

# IF, ELSE, INSTANCE
# if c is a string, it doesnt even check if c==1
#b=1
#if True:
    #print("we are in the if statement")
    #b=2

#c=1
#if isinstance(c,int) and c==1:     # normally the int is unnecessary
    #print("c is one")
#else:
    #print("c is not one")    
#print("sanity",b) 

# IF, ELSE, INSTANCE
# if c is a string, it doesnt even check if c==1
#b=1
#if True:
    #print("we are in the if statement")
    #b=2

#c="abc"
#if isinstance(c,int) and c==1: 
    #print("c is one")
#else:
    #print("c is not one")    
#print("sanity",b) 

# normally the int is unnecessary, just to check if c is an integer. So, should just be this:
#if, elif, else
#b=1
#if True:
    #print("we are in the if statement")
    #b=2

#c=1
#if c==1: 
    #print("c is one")
#else:
    #print("c is not one")

#d=4
#if d<0:
    #print("d is negative")    
#elif d>10:
    #print("d is 10 or higher")
#else:
    #print("d is between 0 and 9 (inclusive)")
#print("sanity",b) 

# if d is a string (text), check if d is integer
#b=1
#if True:
    #print("we are in the if statement")
    #b=2

#c=1
#if c==1: 
    #print("c is one")
#else:
    #print("c is not one")

#d="maxi;is;cute"
#if not isinstance(d,int):
    #print("please give me an int")
#elif d<0:
    #print("d is negative")    
#elif d>10:
    #print("d is 10 or higher")
#else:
    #print("d is between 0 and 9 (inclusive)")
#print("sanity",b) 

# if d is a number
b=1
if True:
    print("we are in the if statement")
    b=2

c=1
if c==1: 
    print("c is one")
else:
    print("c is not one")

d=10
if not isinstance(d,int):
    print("please give me an int")
elif d<0:
    print("d is negative")    
elif d>=10:
    print("d is 10 or higher")
else:
    print("d is between 0 and 9 (inclusive)")
print("sanity",b) 
