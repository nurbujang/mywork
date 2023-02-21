# guess1.py
# prompts the user to guess a number and stops when they get it right
# Author: Nur Bujang

number_to_guess = 30

guess = int(input("Please guess the number:"))
while guess != number_to_guess:
    print ("Wrong")
    guess = int(input("Please guess again:"))

# this is another way of printing out variables
print("Well done! Yes the number was ", number_to_guess)
