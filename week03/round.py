# round.py
# Author: Nur Bujang
# to create a program that should take in a float and output an int (rounded up or down)
# rounds a number
# be careful of round, it rounds to the nearest even number
# eg 4.5 rounds to 4
# but 5.5 rounds to 6
# so do not use it accuracy is essential

number_to_round=float(input("Enter a float number:")) # underscores are used instead of numberToRound
rounded_number=round(number_to_round)
print('{} rounded is {}'.format(number_to_round, rounded_number))