for letter in 'Python':  # First Example
    if letter == 'h':
        break
    print('Current Letter :', letter)

print("\nContinue Example....\n")

for letter in 'Python':  # First Example
    if letter == 'a':
       continue
    print('Current Letter :', letter)


print("\nPass Example \n")

for letter in 'Python':
   if letter == 'h':
        pass
        print ('This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")