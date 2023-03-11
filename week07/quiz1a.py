# Look at the program below, if the file test-a.txt does not exist. 
# What will happen when the program runs?

# the with statement will automatically close the file
# when it is finished with it
with open("test-a.txt") as f:
    data = f.read()
    print (data)
# the old way of doing this is
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()