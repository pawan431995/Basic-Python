
#fo=open("D:\\PythonDemo.txt","w+",1)
#fo.write("Hello Python")
#fo.close()
f=open("D:\\PythonDemo.txt","r")
f1=f.readlines()
print(f.tell())
for x in f1:
    print(f.tell())
    print(x)

f.close()