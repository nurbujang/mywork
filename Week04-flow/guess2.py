# guess2.py
# prompts the user to guess a number and stops when they get it right
# the program will tell the user if they were too high or too low
# Author: Nur Bujang

# number_to_guess = 30

# guess=int(input("Please guess the number:"))
# while guess != number_to_guess:
#     if guess < number_to_guess:
#         print("too low")
#     else: # I know it cant be equal or too low, so it must be too high
#         print("too high")
#     guess=int(input("Please guess again:"))

# print("Well done! Yes the number was ", number_to_guess)

# extra: get the program to generate a random number between 0 and 100 to guess

import random
random_num=random.randint(1,100)

guess=int(input("Please guess the number:"))
while guess != random_num:
    if guess < random_num:
        print("too low")
    else: # I know it cant be equal or too low, so it must be too high
        print("too high")
    guess=int(input("Please guess again:"))

print("Well done! Yes the number was ", random_num)
