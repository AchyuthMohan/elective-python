import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)

y_sin = np.sin(x)
y_cos = np.cos(x)
y_minus_sin = -np.sin(x)

plt.plot(x, y_sin, color='red', label='sin(x)')
plt.plot(x, y_cos, color='green', linestyle='dashed', label='cos(x)')
plt.plot(x, y_minus_sin, color='blue', linestyle='dotted', label='-sin(x)')
plt.title('Trigonometric Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
