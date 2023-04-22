from math import pow
def is_armstrong(m):
    sum=0
    target=m
    n=len(str(m))
    for i in range(n):
        digit=m%10
        sum=sum+pow(digit,n)
        m=m//10
    if sum==target:
        print("is Armstrong")
    else:
        print("is not Armstrong")


x=int(input("Enter the number: "))
is_armstrong(x)