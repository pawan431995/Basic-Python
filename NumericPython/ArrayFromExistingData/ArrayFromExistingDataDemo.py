import numpy as np

x=[(2,3,4,5,1),[1,3,4,5,2]]
data1=np.asarray(x,dtype=complex, order='C')
print(data1)

#===========================


name="Hello Pawan Kumar"
#data2=np.frombuffer(name,dtype='S1')
#print(data2)


list=[1,2,3,4,5]
it=iter(list)
data3=np.fromiter(it,dtype=float)
print(data3)