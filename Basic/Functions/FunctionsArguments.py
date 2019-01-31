
#Required Arguments

def printmeRequired(string):
    "docs"
    print(string)
    return

printmeRequired("hello pawan")
printmeRequired("hello python")

#keywords Arguments

def printmeKeywords(string,age):
    "docs"
    print(string,age)
    return

printmeKeywords(string="Hello pawan",age=24)
printmeKeywords(age=22,string="Hello python")

#Default Arguments
def prinntMeDefault(name,age=23):
    ""
    print(name,age)
    return
prinntMeDefault(name="Pawan")
prinntMeDefault(name="Kumar",age=24)


#Variable-Length Arguments

def printMeVarAGRS(num=10,*num1):
    ""
    print(num)
    for var in num1:
        print(var)
    print("Good bye..")
    return
printMeVarAGRS()
printMeVarAGRS(12)
printMeVarAGRS(11,34,56,78,34,56,68,8,9)
