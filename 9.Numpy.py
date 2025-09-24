import numpy as np
#1d
A1D = np.array([1,2,3,4,5])
print(A1D)
A2D = np.array([[1,2,3],[4,5,6]])
print(A2D)
A =np.array([1,2,3,4,5])
print(A)
print(A.ndim)
print(A2D.ndim)
#shape
print(A2D.shape)
#size
print(A2D.size)
#dtype
print(A2D.dtype)
#creating an array with numpy
#zeros:
import numpy as np
print(np.zeros(12))
print(np.ones(12))
# range
print(np.arange(1,10,1))
print(np.arange(0,11,2))
print(np.arange(1,11,2))
#linspace
print(np.linspace(1,3,7))
#matical operatins 
A = np.array([1,2,3,5])
L = [1,2,3,4,5]
print(A+6)
print(A-1)
print(A*2)
print(A/2)
print(A//2)
print(A**6)
#Aggregate functions
A = np.array([1,2,3,4,5])
#sum
print(np.sum(A))
#mean
print(np.mean(A))
#max
print(np.max(A))
#min
print(np.min(A))
#median
print(np.median(A))
#std
print(np.std(A))
#cumprod
print(np.cumprod(A))
#matrices operations
Mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(Mat1)
Mat2 = np.array([[9,8,7],[5,6,7],[7,9,5]])
print(Mat2)
print(Mat1+Mat2)
print(Mat1*Mat2)
print(Mat1/Mat2)
#dot
print(np.dot(Mat1,Mat2))
#transpose
print(np.transpose(Mat1))










