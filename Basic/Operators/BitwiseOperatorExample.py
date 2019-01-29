# Python Bitwise Operators

#&
a = 16
b = 13
print(bin(a))
print(bin(b))
c = a & b
print("AND Result ",bin(c))
del(a, b)

# |
a = 15
b = 13
print(bin(a))
print(bin(b))
c = a | b
print("OR Result ", bin(c))
del (a, b, c)


#^

a = 16
b = 13
print(bin(a))
print(bin(b))
c = a ^ b
print("XOR Result ", bin(c))
del(a, b, c)

# ~
a = 4
print(bin(a))
c = ~a
print(c, "NOT Result ", bin(c))
del(a, c)

# << and >>
a=60
print(bin(a))
c=a<<6
print("LEFT SHIFT Result ", bin(c), c)
d=c>>6

print("RIGHT SHIFT Result ", bin(d), d)