import numpy as np

#ndarray.shape

data1=np.array([[1,2,3],[4,5,6],[2,3,1],[1,3,6]])
print("shape=",data1.shape)

data1.shape=(6,2)
print("Data=",data1)
b=data1.reshape(4,3)
print("Reshape ",b)
#ndarray.ndim

data2=np.arange(24)
data2.ndim
print("\n....")
b=data2.reshape(1,1,2,1,2,2,3)
print(b)


#numpy.itemsize

data3=np.array([[1,6,3,4],[1,3,6,9]],dtype=np.int8)
print(data3.itemsize)

#numpy.flags

print("Falg=",data3.flags)