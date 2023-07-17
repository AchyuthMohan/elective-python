import matplotlib.pyplot as plt
import numpy as np
from numpy import random
x=np.linspace(0,100,100)
y=random.randint(100,size=(100))
plt.scatter(x,y)
plt.show()