list1=[12,34,56,68,8,9]
list2=("abc","xyz","pqr")
print(list1)
print(list1.append(199),list1)
print(list1.count(9))

#print(list1.extend(list2),list1)
print(list1.remove(199),list1)
print("Index= ", list1.index(56))
print("Insert ",list1.insert(0,100),list1)
print("POP ",list1.pop(0))

print("Reverse ",list1.reverse(),list1)
print("Sort ",list1.sort(),list1)