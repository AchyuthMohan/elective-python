import math

def sin_series(x, n):
    result = 0
    sign = 1

    for i in range(1, n*2, 2):
        term = sign * (x ** i) / math.factorial(i)
        result += term
        sign *= -1

    return result

x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
print(sin_series(x, n)) 
