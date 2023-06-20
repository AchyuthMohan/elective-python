import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 400)
y_tan = np.tan(x)
y_cot = 1 / np.tan(x)

plt.plot(x, y_tan, color='red', label='tan(x)')
plt.plot(x, y_cot, color='blue', label='cot(x)')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
plt.xlim(-2*np.pi, 2*np.pi)

plt.title('Trigonometric Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='lower right')

plt.show()
