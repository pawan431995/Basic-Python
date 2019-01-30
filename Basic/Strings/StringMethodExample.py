import base64
#capitalize()
#Capitalizes first letter of string
'''
var="pawan kumar"
print("capitalizes ", var.capitalize())


#center(width, fillchar)
#Returns a string padded with fillchar with the original string centered to a total of width columns.
print(var.center(40,'*'))


#str.count(sub, start = 0,end = len(string))
#The count() method returns the number of occurrences of substring
# sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.


str = "this is string example....wow!!!"
sub = 'i'
print(str)
print ("str.count('i') : ", str.count(sub))
sub = 'wow'
print ("str.count('wow', 0, 40) : ", str.count(sub,0,len(str)))

'''

Str = "this is string example....wow!!!"
#Str1 = Str.encode('base64','strict')
Str=Str.encode(encoding='UTF-16',errors="strict")


print("Encoded String: " , Str)
print("Decoded String: " , Str.decode('UTF-16','strict'))