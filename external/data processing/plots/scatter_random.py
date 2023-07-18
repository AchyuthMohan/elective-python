import matplotlib.pyplot as plt
import numpy as np
from numpy import random
x=np.linspace(0,50,50)
y=random.randint(100,size=(50))
plt.scatter(x,y)
plt.show()