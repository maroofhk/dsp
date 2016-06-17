# Matrix Algebra
import numpy as np

A = np.array([1,2,3,2,7,4])
A.shape = (2,3)

B = np.array([1,-1,0,1])
B.shape = (2,2)

C = np.array([5,-1,9,1,6,0])
C.shape = (3,2)

D = np.array([3,-2,-1,1,2,3])
D.shape = (2,3)

# ------ 3.1) A+C:
print('--- A+C ------------')
try:
	print(A+C)
except ValueError:
	print('not defined', '\n')

# ------ 3.2) A-transpose(C):
print('--- A-(Ct) ---------')
Ct = np.transpose(C)
print(A-Ct, '\n')

# ------ 3.3) transpose(C)+3D
print('--- (Ct)+3D --------')
print(Ct+3*D, '\n')

# ------ 3.4) BA
print('--- BA -------------')
print(np.dot(B,A), '\n')

# ------ 3.5) BAt
print('--- B(At) ----------')
At = np.transpose(A)
try:
	print(np.dot(B,At))
except ValueError:
	print('not defined', '\n')

# ------ 3.6) BC
print('--- BC -------------')
try:
	print(np.dot(B,C))
except ValueError:
	print('not defined', '\n')

# ------ 3.7) CB
print('--- CB -------------')
print(np.dot(C,B), '\n')

# ------ 3.8) B^4
print('--- B^4 ------------')
B2 = np.dot(B,B)
print(np.dot(B2,B2), '\n')

# ------ 3.9) A*transpose(A)
print('--- AAt ------------')
print(np.dot(A, np.transpose(A)), '\n')

# ------ 3.10) transpose(D)*D
print('--- (Dt)D ----------')
print(np.dot(np.transpose(D),D))
