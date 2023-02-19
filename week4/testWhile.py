# Messing with while loops
# Author: Nur Bujang

#while condition:
#    statements
#
# two types
#   Counter Controled
#       we usualy use for loops for counter conttroled loops
#   Sentinal Controled
#       if you are reading in from a user, one pattern is
#       read in from the user, check the while, and then read again in the 
#       body of the while loop
# be careful of infinite loops
#   make sure you modify what you are checking 

# COUNTER COUNTROLLED LOOPS
# first, initialize your variable
#count=0
#while (count<10):
    #print("count is ",count) # when you put comma inside print,it will print each of these variable, "" as a string, and the other as integer
    #count=count+1 # Always make sure you change your conditions-----IMPORTANT IN WHILE LOOPS!!!

#   Outside the While loop:
#print("at the end of count is ",count)

# if you want to count backwards
#count=10
#while count>=0:
    #print("countdown ",count)
    #count-=1 # will minus 1 every step, same as count=count-1
#print("blast off")

# SENTINEL CONTROLLED LOOPS - you do something until some event happens
val=input("type something (q to quit):")
while val!='q':   # if it's not equal to q, it will say hi mom, then asks user to type something again, so on until user types in q
    print("hi mom")
    val=input("q to quit: ")

print("all done")