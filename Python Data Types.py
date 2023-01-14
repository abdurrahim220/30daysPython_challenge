# Built-in Data Types

'''
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type       :	str
Numeric Types   :	int, float, complex
Sequence Types  :	list, tuple, range
Mapping Type    :	dict
Set Types       :	set, frozenset
Boolean Type    :	bool
Binary Types    :	bytes, bytearray, memoryview
None Type       :	NoneType

'''

# Getting the Data Type -- to get data type use type() function

x = 5
print(type(x))

x = "Hello world"

# to display the values
print(x)

# to diaplay the values data type

print(type(x))


x = 5.5

print(x)  # to diaplay the value

print(type(x))  # to diaplay the values data type

x = 1j
print(x)  # to diaplay the value
print(type(x))  # to diaplay the values data type

x = ["apple", "banana", "cherry"]
print(x)
print(type(x))  # to diaplay the values data type

x = ("apple", "banana", "cherry")
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

x = {"name": "John", "age": 36}
print(x)
print(type(x))


x = {"apple", "banana", "cherry"}
print(x)
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x = b"Hello"
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))

x = None
print(x)
print(type(x))
