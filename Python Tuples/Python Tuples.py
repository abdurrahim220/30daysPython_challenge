'''
Tuple -- Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

'''

thistuple = ("apple","banana","banana","cherry") 
print(thistuple)
print(len(thistuple))


'''
Tuple Items -- [0] or [1]

ordered -- it is a order tuple
Unchangeable -- it cannot be changed
allow duplicate -- it can be repeated
'''

# create tuple with 1 item

thistuple1 = ("apple",)
print(type(thistuple1))

# Tuple Items - Data Types

tuple2 = ("apple","banana","cherry","mango")
tuple3 = (1,4,4,3.5,43)
tuple4 = (True,False,False)

tuple5 = ("abcc",43,True,50,"male")

print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)