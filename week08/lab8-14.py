# normalized random data
import numpy as np
import matplotlib.pyplot as plt

#you want 30 numbers between 100 and 200
np.random.seed(1)
normData=np.random.normal(loc=5555,scale=20,size=22000)

plt.hist(normData)
plt.show()
