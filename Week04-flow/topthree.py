# topthree.py
# This program generates 10 random numbers (0-100).
# prints them out, then prints out the top 3
# I will use a list to store and manipulate the numbers
# Author: Nur Bujang

# import random
# # I programming the general case
# how_many=10
# top_how_many=3
# range_from=0
# range_to=100

# numbers=[]

# for i in range(0,how_many):
#     numbers.append(random.randint(range_from,range_to))
# print (f"{how_many} random numbers\t {numbers}")
# # I am keeping the original list maybe I don't need to 
# top_ones=numbers.copy()
# top_ones.sort(reverse=True)
# print(f"The top {top_how_many} are \t\t {top_ones[0:top_how_many]}")

# or you could go with a while loop
import random

how_many=10
top_how_many=3
range_from=0
range_to=100

numbers=[]

count=0
while count <10:
    numbers.append(random.randint(range_from,range_to))
    count+=1
print (f"{how_many} random numbers\t {numbers}")
# I am keeping the original list maybe I don't need to 
top_ones=numbers.copy()
top_ones.sort(reverse=True)
print(f"The top {top_how_many} are \t\t {top_ones[0:top_how_many]}")

