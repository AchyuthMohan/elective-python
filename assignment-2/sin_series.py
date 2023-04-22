from math import factorial
n=int(input("Enter the number: "))
t=0
s=1
while t<n:
    print('(x','^',t+1,')/',(t+1),'!')
    if s%2==0:
        print('+')
    else:
        print('-')
    s=s+1
    t=t+2
