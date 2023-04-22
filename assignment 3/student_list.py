s=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    x=input("Enter the name: ")
    s.append(x)

s.sort(key=len)
print("The sorted list is: ",s)



