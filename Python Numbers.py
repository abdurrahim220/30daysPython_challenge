'''
#Python Numbers
 -There are three numeric types in Python:
    --int
    --float
    --complex



x = 1  #Int, or integer, is a whole number, positive or negative,     without decimals, of unlimited length.
y = 1.2 #Float can also be scientific numbers with an "e" to indicate the power of 10.ex:35e3,12E4,-87.7e100

z = 1j #Complex numbers are written with a "j" as the imaginary part:

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

# Type Conversion -- You can convert from one type to another with the int(), float(), and complex() methods:

a = float(x)

b = int(y)

c = complex(x)

d = int(z)

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c)) '''


# Random Number -- Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random
print(random.randrange(1,10))