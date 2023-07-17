import matplotlib.pyplot as plt
import numpy as np

# sin wave
# x=np.linspace(0,2*np.pi,100)
# y=np.sin(x)

# 45 deg inclined line
# x=np.linspace(0,100,100)
# y=x
x=np.linspace(0,2*np.pi,100)
y=np.tan(x)

plt.plot(x,y,color='red',label='sin plot')
plt.show()