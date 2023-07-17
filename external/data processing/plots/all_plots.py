import matplotlib.pyplot as plt
import numpy as np

# single graph and all lines in it

x=np.linspace(0,2*np.pi,100)
y_sin=np.sin(x)
y_cos=np.cos(x)
y_tan=np.tan(x)
plt.plot(x,y_sin,label="sin(x)",color='red')
plt.plot(x,y_cos,color='green',label='cos(x)')
plt.plot(x,y_tan,color='blue',label='tan(x)')
plt.show()