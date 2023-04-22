def revere(n):
    s= str(n)
    res=s[::-1]
    return int(res)
def sum(n):
    if n==0:
        return 0
    else:
        return (n%10)+sum(n//10)
    
n=int(input("Enter the number: "))
print("The reverse of the number is: ",revere(n))
print("The sum of the number is: ",sum(n))