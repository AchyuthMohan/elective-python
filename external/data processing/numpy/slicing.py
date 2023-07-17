import numpy as np
A=np.array([[15,16,17],[25,26,27],[35,36,37],[45,46,47]])
B=np.array([1,2,3,4,5,6,7])
# print(A[:,1:3])
A[:2, 1:] =0
print(A)