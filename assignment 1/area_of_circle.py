from math import sqrt,pi
xc=float(input("Enter the xc value: "))
yc=float(input("Enter the yc value: "))
xr=float(input("Enter the xr value: "))
yr=float(input("Enter the yr value: "))
r=sqrt(((xr-xc)**2)-((yr-yc)**2))
a=pi*(r**2)

print("area: ",a)
