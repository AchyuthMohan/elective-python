from math import sqrt
def newton_sqrt(n, x0, eps):
    x = x0
    while True:
        fx = x**2 - n
        if abs(fx) < eps:
            return x
        x = (x + n/x) / 2

n = int(input("Enter the number: "))
x0 = sqrt(n)
eps = 1e-6
sqrt_n = newton_sqrt(n, x0, eps)
print("The square root of", n, "is", sqrt_n)
