

for var1 in range(1,11):
    for var2 in range(1,11):
        if var1==var2:
            print(var1*var2, end=' ')
        elif var2> var1:
            print(var1*var2,end=" ")
    print()