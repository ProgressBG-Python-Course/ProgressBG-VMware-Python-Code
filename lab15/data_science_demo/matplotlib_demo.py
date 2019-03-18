import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
X = np.arange(0.0, 2.0, 0.01)
Y = 1 + np.sin(2 * np.pi * X)

fig, ax = plt.subplots()
ax.plot(X, Y)

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()

# fig.savefig("test.png")
plt.show()