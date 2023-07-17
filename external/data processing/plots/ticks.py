import matplotlib.pyplot as plt
import numpy as np
x=y=np.linspace(0,10,10)
ax=plt.axes()

plt.plot(x,y,color='lime',label='sin wave')
ax.set_xticks([2, 4, 6, 8, 10])
ax.set_yticks([1, 3, 5, 7, 9])
plt.title('trignometry')
ax.set_xlabel('sin')
plt.show()