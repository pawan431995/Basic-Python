
dict={"name":"Pawan","Age":"23","address":"bihar"}
#clear all records from dictionary
#print("Clear ",dict.clear(),dict)

#The method copy() returns a shallow copy of the dictionary.

dict2=dict.copy()
print("Copy ",dict2)

#The method fromkeys() creates a new dictionary with keys
# from seq and values set to value.
seq = ('name', 'age', 'sex')

dict2 = dict.fromkeys(seq)
print ("New Dictionary : %s" %  str(dict2))

dict2 = dict.fromkeys(seq, 10)
print ("New Dictionary : %s" %  str(dict2))


#The method get() returns a value for the given key.
# If key is not available then returns default value None.

print("Get ",dict.get("name"))

print("Item ",dict.items())

print("Keys ",dict.keys())

print("Values ",dict.values())

print("Update dictionary....")
dict.update(dict2)
print("updated dict ",dict)

