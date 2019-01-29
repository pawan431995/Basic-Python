# Python Membership Operators Example
'''
Python’s membership operators test for membership in a sequence,
such as strings, lists, or tuples.
There are two membership operators as explained below −

in
not in

'''

a = 10
b = 20
list = [1, 20, 3, 4, 5 ]

if ( a in list ):
   print ("Line 1 - a is available in the given list")
else:
   print ("Line 1 - a is not available in the given list")

if ( b not in list ):
   print ("Line 2 - b is not available in the given list")
else:
   print ("Line 2 - b is available in the given list")

