dict={"name":"Pawan","Age":"23","address":"bihar"}
print("Information ",dict)
print("Name" , dict["name"])
print("Age" , dict["Age"])
print("Address" , dict["address"])
print("Updating Age ....")
dict["Age"]=35
print("Age" , dict["Age"])
print("Updating Address")
dict["address"]="Pune"
print("Address ",dict["address"])
print("Deleting Address")
del dict["address"]
print("Address ",dict["address"])#it gives KeyError


