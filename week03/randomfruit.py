# randomfruit.py
# Author: Nur Bujang
# to create a program that prints out a random fruit

import random
fruits=['Apple','Orange','Banana','Pear'] # list is square brackets

# we want a random number between 0 and length-1
index=random.randint(0,len(fruits)-1)
fruit=fruits[index]
print("A Random Fruit:{}".format(fruit))