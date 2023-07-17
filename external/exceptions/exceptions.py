a = [1, 2, 3, 4]
print(len(a))
a.append(5)
print(a)
index = int(input("Enter the index: "))
try:
    print(a[index])
except ZeroDivisionError:
    print("Zero division not possible")
except IndexError:
    print("index not found")
finally:
    print("Done the execution..")
