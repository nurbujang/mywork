# more messing with functions
# variable scope
# Author: Nur Bujang

# I don't want you to use global variables

x = 999 # this is the global x

def fun(num):
    print(num)

def fun2(x2):
    print(f"in fun2 x {x2}")
    x = 21 # this x doesnt affect global x
    print(f"in fun2 x {x2}")
    
    
fun2(x)
print(f"after fun2 x is {x}")