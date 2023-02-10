# randomFruit2.py
# Author: Nur Bujang
# to create a program that prints out a random fruit, but a tuple () instead of a list []

import random
fruits=('Apple','Orange','Banana','Pear') # tuple is round brackets

# we want a random number between 0 and length-1
index=random.randint(0,len(fruits)-1)
fruit=fruits[index]
print("A Random Fruit:{}".format(fruit))