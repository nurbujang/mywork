import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# this is so that the "random" numbers are the same each time
np.random.seed(1)

# create data
ages = np.random.normal(size=1000)
salaries = np.random.normal(loc=21, scale=30, size=1000)

#create normal distribution curve
sns.displot(salaries, kde=True)
plt.show()
'''
#plt.show() # if you do this the proram will halt here until the plot is closed
# add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply each entry by itself
plt.plot(xpoints, ypoints, color='r', label = "x squared")
plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()
plt.show() # see how the axis have changed
#plt.savefig('prettier-plot.png')
'''