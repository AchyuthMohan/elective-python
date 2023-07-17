import  numpy as np

A=np.array([[1,2,4],[2,3,4],[3,4,5]])
B=np.array([[7,6,5],[3,4,5],[5,6,7],[2,3,4]])
A=np.hstack((A,[[2],[3],[9]]))
print("A: ")
print(A)
print("Altering ")
# print(A)
# print(B)
# sum=A+B
# print(sum)
product=np.dot(A,B)
print(product)