class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg

try:
   print("before")
   raise Networkerror("Bad hostname")
   print("After")
except Networkerror as e:
   print(e.args)