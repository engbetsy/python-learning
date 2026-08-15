x = 4   # int
y = 2.6  # float
z = 9j   # complex
print(type(x))
print(type(y))
print(type(z))

#int
x = 7
y = 675656222554889
z = -32555567

print(type(x))
print(type(y))
print(type(z))

# float
x = 2.12
y = 1.5
z = -25.57

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z)) #Float can also be scientific numbers with an "e" to indicate the power of 10

#complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Convert from one type to another
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#You cannot convert complex numbers into another number type
