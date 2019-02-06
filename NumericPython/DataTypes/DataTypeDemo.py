
import numpy as np

data1=np.dtype(np.int32)
print("\n Data1 - ",data1)

data2=np.dtype('i4')
print("\n Data2 - ",data2)

data3=np.dtype('<i4')
print("\n Data 3 - ",data3)

data4=np.dtype([('age', np.int32)])
print("\nData4 - ",data4)

data5=np.dtype([('age',np.int8)])
arr1=np.array([1,2,3,4,5,6,7],dtype=data5)

print("\n Array1 -  ",arr1)
print("\nAge=",arr1['age'])

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a)