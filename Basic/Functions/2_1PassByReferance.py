

def printList(list):
    "list is local to function and can't chane the referance value"
    list=[1,2,3,4,5,6]
    print("Inside function ",list)
    return
list=[11,22,33,44,55,66]
print("outside before calling function ",list)
printList(list)
print("outside after calling function ",list)