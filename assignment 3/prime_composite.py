def is_prime(x):
    if x==1:
        return False
    for i in range(2,x//2):
        if x%i==0:
            return False
    return True
l=list()
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    x=int(input("Enter the element:"))
    l.append(x)
print("The list is:",l)
c=[]
p=[]
for i in l:
    if is_prime(i):
        p.append(i)
    else:
        c.append(i)
print("The prime numbers are:",p)
print("The composite numbers are:",c)
