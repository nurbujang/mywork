# queue.py
# lab 5
# Author: Nur Bujang
# Create a program that puts 10 random numbers into a queue(list), 
# the program should then output all the values in the queue, 
# then take the numbers from the queue one at a time, 
# print it and the current numbers still in the queue. 
# (the command pop(0) takes the first element out of a list)

import random
queue = []
number_of_numbers=10
range_to=100

for n in range(0,number_of_numbers):
    queue.append(random.randint(0,range_to))
print (f"queue is {queue}")

while len(queue) != 0:
    current_number = queue.pop(0)
    print (f"current Number is {current_number} and the queue is {queue} ")
print ("the queue is now empty")

