import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,100)
y_sin=np.sin(x)
y_cos=np.cos(x)
y_tan=np.tan(x)
y_cot=1/np.tan(x)

fig,(ax1,ax2,ax3,ax4)=plt.subplots(4,1,figsize=(6,12))
ax1.plot(x,y_sin,color='red',label='sin')
ax2.plot(x,y_cos,color='blue',label='cos')
ax3.plot(x,y_tan,color='green',label='tan')
ax4.plot(x,y_cot,color='purple',label='cot')

plt.show()