# messing with numpy
# Author: Nur Bujang

import numpy as np

list_of_numbers=[1,2,3,"asdf"]
list_of_numbers=list_of_numbers+[3]
print ("list", list_of_numbers)

# with numpy arrays, u can only put 1 variable type
numbers=np.array([1,2,3,4])
numbers=numbers*[1,2,3,4]
print("array", numbers)

#you want 30 numbers between 100 and 200
rando=np.random.randint(100,200,30)
print (rando)

normalrando=np.random.normal(loc=50,scale=20,size=100)
print(normalrando)



'''
numbers=np.array([1,2,3,4,5.6])
print(numbers)

numbers=np.array([1,2,3,4,"ere"])
print(numbers)
'''