def functionName( level ):
   if level <1:
        print("before exception")
        raise Exception(level)
        print("After Exception")
      # The code below to this would not be executed
      # if we raise the exception
   return level



try:
    functionName(12)
except Exception as e:
    print(e.args)
else:
    print("Else block Executed , when all statements of try block is executed successfully")

