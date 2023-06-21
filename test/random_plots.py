import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi,100)
y_sin=np.sin(x)
y_cos=np.cos(x)
y_tan=np.tan(x)
fig,(ax1,ax2,ax3)=plt.subplots(3,1,figsize=(6,12))
ax1.plot(x,y_sin)
ax2.plot(x,y_cos)
ax3.plot(x,y_tan)
plt.show()