import os
import shutil
'''
shutil is used to 
copy file

'''

#os.rename("D:\\PythonDemo.txt","D:\\Python1Demo.txt")
shutil.copy("D:\\Python1Demo.txt","D:\\PythonDemo.txt")
#os.remove("D:\\PythonDemo.txt")

os.mkdir("D:\\PythonDemoDIR")
print(os.listdir("D:\\"))
os.rmdir("D:\\PythonDemoDIR")
print(os.getcwd())
