# messingWithLists.py
# messing with lists
# Author: Nur Bujang

# boats=['Sigma', 23, [1,2,3], {}]  # {} is a function
# boats=boats+[1,2,3]
# print(boats)
'''
# if u want to use For loop
boats=['Sigma', 23, [1,2,3], {}]  # {} is a function
for boat in boats:
    print(type(boat))
'''

# ages=[12,21,23,34, "dfas"]
# sum=0
# for age in ages:
#     sum += age
# print(sum)

# list = [2, 4, 5, 6]
# sum = 0
# for x in list:
#     sum += x
#     print (sum)

# wrong way
#for i in range(0,len(list)):
#    print ("value of index ", i, " is ", list[i] )

'''
# dont do this:
length_of_list=len(ages)
for i in range (0,length_of_list):
    sum+=ages[i]
print(sum)
'''

# string="1234567890"
# print(string[6:])


# t=(1,2,3)
# print(t)

t=(1,2,3)
x,y,z=t
print(y)