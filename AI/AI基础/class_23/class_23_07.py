import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x * 3
x_1 = np.arange(0, 100, step=0.1)
y_1 = np.sin(x_1)
x_2 = [1, 2, 3, 4]
y_2 = [50, 30, 70, 100]
plt.subplot(2, 2, 1)
plt.plot(x, y)

plt.subplot(2, 2, 2)
plt.plot(x_1, y_1)

plt.subplot(2, 2, 3)
plt.plot(x_2, y_2)
plt.show()
