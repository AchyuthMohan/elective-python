import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 12))
ax1.plot(x, y_sin, color='red')
ax1.set_title('sin(x)')

ax2.plot(x, y_cos, color='green')
ax2.set_title('cos(x)')
ax3.plot(x, y_tan, color='blue')
ax3.set_title('tan(x)')
plt.tight_layout()
plt.show()
