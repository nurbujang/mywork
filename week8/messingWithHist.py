# messing with histograms and pie chart
# Author: Nur Bujang

import numpy as np
import matplotlib.pyplot as plt
'''
np.random.seed(1)
normData=np.random.normal(size=10000)
plt.hist(normData)
plt.show()
'''
fruit = np.array(['Apples', 'Orange','Banana'])
numbers = np.array([23, 77,500])

plt.pie(numbers, labels=fruit)
plt.legend()
plt.show()