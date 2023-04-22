n=int(input("Enter the time in seconds: "))
hr=n//3600
n=n%3600
mn=n//60
n=n%60
sc=n
print("Result: ",hr,":",mn,":",sc)