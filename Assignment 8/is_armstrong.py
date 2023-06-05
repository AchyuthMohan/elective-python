def is_armstrong(n):
    s=0
    x=n
    while n!=0:
        s=s+(n%10)**3
        n=n//10
    if s==x:
        return True
    else:
        return False

n=int(input("Enter the number: "))
if is_armstrong(n):
    print("Its an armstrong number..")
else:
    print("its not an armstrong number")
