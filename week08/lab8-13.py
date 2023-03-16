# real data

import numpy as np

# with numpy arrays, u can only put 1 variable type
numbers=np.array([1,2,3,4,5,6,7,8,9,10,11])
numbers=numbers*[1,2,3,4,5,6,7,8,9,10,11]
print("array", numbers)
'''
#you want 30 numbers between 100 and 200
rando=np.random.randint(100,200,30)
print (rando)

normalrando=np.random.normal(loc=50,scale=20,size=100)
print(normalrando)
'''
