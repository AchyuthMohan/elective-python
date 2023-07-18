import matplotlib.pyplot as plt

x=list((x for x in range(1,6)))
y=list((x for x in range(1,6)))
plt.title("HEllo graph")
ax=plt.axes()
ax.set_xlabel('magnitude')
ax.set_ylabel('quanrtuty')
plt.plot(x,y,color='red',label='demo')
plt.show()

