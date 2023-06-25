a=5
try:
    z=a/0
    print(z)
except ZeroDivisionError:
    print("Zero division is not possible")
finally:
    print("Completed execution")