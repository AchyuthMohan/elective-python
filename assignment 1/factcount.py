num = int(input("Enter a number: "))
while num > 0:
    digit = num % 10
    print("Binary equivalent of", digit, "is", bin(digit)[2:])
    num //= 10
