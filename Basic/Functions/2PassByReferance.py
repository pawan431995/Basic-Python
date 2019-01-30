
def printList(list):
    ""
    list[2]=50
    print("Inside function ",list)
    return
list=[10,20,30]
print("outside before calling function ",list)
printList(list)
print("outside after calling function ",list)