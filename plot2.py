import matplotlib.pyplot as plt
import numpy as np
x = np.array([10,9])
y = np.array([10,25])
plt.plot(x, linestyle='dotted', marker='o')
plt.plot(y)
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title("Plot Title")
plt.show()