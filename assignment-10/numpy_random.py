import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

random_numbers = np.random.randint(1, 101, 50)
x = np.arange(1, 51)
y = random_numbers

plt.scatter(x, y)

plt.title('Random Numbers Scatter Plot')
plt.xlabel('Index')
plt.ylabel('Value')

plt.show()
