import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# X = array of numbers [1..100]
X = np.arange(1,101)
Y = X**2

# create the plot
plt.plot(X,Y)

# show the plot
plt.show()

