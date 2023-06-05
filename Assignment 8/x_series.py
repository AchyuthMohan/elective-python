def factorial(x):
    if(x<=1):
        return 1
    return x*factorial(x-1)
def series(x,n):
    s=0
    for i in range(n+1):
        s=s+(pow(x,i)/factorial(i))
    return s

x=int(input("Enter the x value: "))
n=int(input("Enter the n values: "))
print("result: ",series(x,n))
