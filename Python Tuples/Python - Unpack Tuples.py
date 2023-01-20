# Unpacking a Tuple -- When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

fruits = ("apple","banana","magos","jackfruit","guava","orange")

(green,yello,*red) = fruits #Using Asterisk*
print(green)
print(yello)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

(green,*yello,red) = fruits

print(green)
print(yello)
print(red)