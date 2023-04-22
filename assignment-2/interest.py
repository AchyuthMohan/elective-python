inv=int(input("Enter the investment amount: "))
y=int(input("Enter the number of years: "))
r=int(input("Enter the rate: "))
rate_in_percent=r/100
print("year\tstart balance\tinterest\tending balance\n")
for i in range(y):
    interest=rate_in_percent*inv
    print(i+1,"\t",inv,"\t",interest,"\t",inv+interest,"\n")
    inv=inv+interest

