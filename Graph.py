import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
plt.quiver(0, 0, 0, -6, color='r', angles='xy', scale_units='xy', scale=1)# this is a red vector
plt.quiver(0, 0, 4, 0, color='b', angles='xy', scale_units='xy', scale=1)# this is a blue vector
plt.quiver(0, 0, 4, -6, color='g', angles='xy', scale_units='xy', scale=1)# this is a green vector
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.show()